#!/usr/bin/env python3
"""
Create Staff Member and Assign All Appointment Services
Makes services visible on Square Appointments online booking by:
  - enabling the team member booking profile
  - setting available_for_booking and team_member_ids on each service variation (Catalog API)
"""

import copy
import os
import sys
import uuid
from typing import List, Optional

import requests
from dotenv import load_dotenv

load_dotenv()

STAFF = {
    "given_name": "ND Derma",
    "family_name": "Med Spa",
    "email_address": "nddermamedspa@gmail.com",
    "phone_number": "+17864037390",
}

SQUARE_VERSION = os.getenv("SQUARE_VERSION", "2026-01-22")
BATCH_SIZE = int(os.getenv("SQUARE_CATALOG_BATCH_SIZE", "20"))


def _headers(access_token: str) -> dict:
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Square-Version": SQUARE_VERSION,
    }


def fetch_appointment_variation_ids(headers: dict, base: str) -> List[str]:
    service_variation_ids: List[str] = []
    cursor = None
    while True:
        params: dict = {"types": "ITEM"}
        if cursor:
            params["cursor"] = cursor
        r = requests.get(f"{base}/catalog/list", headers=headers, params=params, timeout=60)
        data = r.json()
        if "errors" in data:
            print(f"❌ Catalog error: {data['errors']}")
            sys.exit(1)
        for obj in data.get("objects", []):
            item_data = obj.get("item_data", {})
            if item_data.get("product_type") != "APPOINTMENTS_SERVICE":
                continue
            for var in item_data.get("variations", []):
                service_variation_ids.append(var["id"])
                print(f"  ✓ {item_data['name']}")
        cursor = data.get("cursor")
        if not cursor:
            break
    return service_variation_ids


def build_variation_upsert(catalog_object: dict, team_member_id: str) -> Optional[dict]:
    if catalog_object.get("type") != "ITEM_VARIATION":
        return None
    obj = copy.deepcopy(catalog_object)
    ivd = dict(obj.get("item_variation_data") or {})
    team_ids = list(ivd.get("team_member_ids") or [])
    if team_member_id not in team_ids:
        team_ids.append(team_member_id)
    ivd["team_member_ids"] = team_ids
    ivd["available_for_booking"] = True
    ivd.pop("ordinal", None)
    out: dict = {
        "type": "ITEM_VARIATION",
        "id": obj["id"],
        "version": obj["version"],
        "item_variation_data": ivd,
    }
    for k in (
        "present_at_all_locations",
        "present_at_location_ids",
        "absent_at_location_ids",
    ):
        if k in obj:
            out[k] = obj[k]
    return out


def batch_link_services_to_staff(
    service_variation_ids: List[str],
    team_member_id: str,
    headers: dict,
    base: str,
) -> int:
    to_upsert: List[dict] = []
    for vid in service_variation_ids:
        r = requests.get(
            f"{base}/catalog/object/{vid}",
            headers=headers,
            timeout=60,
        )
        data = r.json()
        if "errors" in data:
            print(f"  ⚠ Skip {vid}: {data['errors']}")
            continue
        obj = data.get("object")
        if not obj:
            continue
        upsert_obj = build_variation_upsert(obj, team_member_id)
        if upsert_obj:
            to_upsert.append(upsert_obj)
    if not to_upsert:
        print("  ⚠ No catalog objects to upsert.")
        return 0
    ok = 0
    for i in range(0, len(to_upsert), BATCH_SIZE):
        chunk = to_upsert[i : i + BATCH_SIZE]
        body = {
            "idempotency_key": str(uuid.uuid4()),
            "batches": [{"objects": chunk}],
        }
        r = requests.post(
            f"{base}/catalog/batch-upsert",
            headers=headers,
            json=body,
            timeout=120,
        )
        data = r.json()
        if "errors" in data:
            print(f"  ❌ batch-upsert ({i + 1}-{i + len(chunk)}): {data['errors']}")
            continue
        ok += len(chunk)
        print(f"  ✓ batch-upsert {i + 1}-{i + len(chunk)} ({len(chunk)} variations)")
    return ok


def resolve_team_member_id(
    headers: dict,
    base: str,
    location_id: str,
) -> str:
    payload = {
        "idempotency_key": str(uuid.uuid4()),
        "team_member": {
            "given_name": STAFF["given_name"],
            "family_name": STAFF["family_name"],
            "email_address": STAFF["email_address"],
            "phone_number": STAFF["phone_number"],
            "assigned_locations": {
                "assignment_type": "EXPLICIT_LOCATIONS",
                "location_ids": [location_id],
            },
        },
    }
    r = requests.post(f"{base}/team-members", headers=headers, json=payload, timeout=60)
    data = r.json()
    if "errors" not in data:
        tm = data["team_member"]
        print(f"  ✓ Created: {tm['given_name']} {tm['family_name']} (ID: {tm['id']})")
        return tm["id"]
    if not any(e.get("code") == "CONFLICT" for e in data["errors"]):
        print(f"❌ Error creating team member: {data['errors']}")
        sys.exit(1)
    print("  ℹ Team member already exists — searching...")
    r2 = requests.post(
        f"{base}/team-members/search",
        headers=headers,
        json={
            "query": {
                "filter": {
                    "location_ids": [location_id],
                    "status": "ACTIVE",
                }
            }
        },
        timeout=60,
    )
    members = r2.json().get("team_members", [])
    if not members:
        print("❌ Could not find an active team member for this location.")
        sys.exit(1)
    email = STAFF["email_address"].lower()
    for m in members:
        if (m.get("email_address") or "").lower() == email:
            tid = m["id"]
            print(
                f"  ✓ Using team member: {m.get('given_name', '')} {m.get('family_name', '')} (ID: {tid})"
            )
            return tid
    m = members[0]
    tid = m["id"]
    print(
        f"  ✓ Using first active member: {m.get('given_name', '')} {m.get('family_name', '')} (ID: {tid})"
    )
    print(f"     (No match for email {STAFF['email_address']}; set STAFF in script if wrong.)")
    return tid


def main():
    access_token = os.getenv("SQUARE_ACCESS_TOKEN")
    location_id = os.getenv("SQUARE_LOCATION_ID")
    environment = (os.getenv("SQUARE_ENVIRONMENT") or "production").lower()

    if not access_token or not location_id:
        print("❌ Missing SQUARE_ACCESS_TOKEN or SQUARE_LOCATION_ID in .env")
        sys.exit(1)

    base = (
        "https://connect.squareupsandbox.com/v2"
        if environment == "sandbox"
        else "https://connect.squareup.com/v2"
    )
    headers = _headers(access_token)

    print("\n" + "=" * 60)
    print("STEP 1 — Appointment service variations from catalog")
    print("=" * 60)
    service_variation_ids = fetch_appointment_variation_ids(headers, base)
    print(f"\n  Found {len(service_variation_ids)} variation(s).")
    if not service_variation_ids:
        print("\n⚠ No APPOINTMENTS_SERVICE items. Run create_services.py first.")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("STEP 2 — Team member")
    print("=" * 60)
    team_member_id = resolve_team_member_id(headers, base, location_id)

    print("\n" + "=" * 60)
    print("STEP 3 — Booking profile (online bookable)")
    print("=" * 60)
    r = requests.put(
        f"{base}/bookings/team-member-booking-profiles/{team_member_id}",
        headers=headers,
        json={
            "team_member_booking_profile": {
                "display_name": f"{STAFF['given_name']} {STAFF['family_name']}",
                "is_bookable": True,
                "booking_enabled": True,
            }
        },
        timeout=60,
    )
    data = r.json()
    if "errors" in data:
        print(f"  ⚠ Booking profile: {data['errors']}")
    else:
        print("  ✓ Booking profile updated.")

    print("\n" + "=" * 60)
    print("STEP 4 — Link services to staff (catalog batch-upsert)")
    print("=" * 60)
    linked = batch_link_services_to_staff(
        service_variation_ids, team_member_id, headers, base
    )

    print("\n" + "=" * 60)
    print("✅ DONE")
    print("=" * 60)
    print(f"\n  Team member ID     : {team_member_id}")
    print(f"  Location ID        : {location_id}")
    print(f"  Variations updated : {linked}")
    print("\n  Son kontrol: Square Panel → Appointments → Staff → ilgili personel →")
    print("    çalışma saatleri / hizmetler ekranında hizmetlerin açık olduğundan emin olun.")
    print("  Rezervasyon linki: Panel → Appointments → Online booking / Settings.\n")


if __name__ == "__main__":
    main()
