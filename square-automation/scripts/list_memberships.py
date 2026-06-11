#!/usr/bin/env python3
"""
List Square Membership Plans
Fetches all existing SUBSCRIPTION_PLAN objects from Square Catalog
and outputs their real IDs — needed to build checkout links for the website.

Checkout link format: https://square.link/u/{SUBSCRIPTION_PLAN_VARIATION_ID}

NOTE on discounts:
Square Subscriptions does not auto-apply service discounts at booking time
without a custom backend/webhook. The recommended approach for a static site
is to create Square Discount objects (20%, 25%, 30%) and have staff apply the
appropriate discount in Square POS when a member books a service.
Run create_discounts() below to set those up in Square Catalog.
"""

import os
import csv
import sys
from dotenv import load_dotenv
from square import Square

load_dotenv()


def list_memberships():
    """Fetch and display all subscription plans from Square Catalog."""

    access_token = os.getenv('SQUARE_ACCESS_TOKEN')
    if not access_token:
        print("ERROR: SQUARE_ACCESS_TOKEN not set in .env")
        return False

    client = Square(token=access_token)

    print("\n" + "="*70)
    print("SQUARE SUBSCRIPTION PLANS")
    print("="*70 + "\n")

    try:
        # Fetch all SUBSCRIPTION_PLAN objects — returns a SyncPager
        pager = client.catalog.list(types=["SUBSCRIPTION_PLAN"])
        objects = list(pager)

        if not objects:
            print("No subscription plans found in Square Catalog.")
            print("Run create_memberships.py first to create them.\n")
            return False

        rows = []

        for obj in objects:
            plan_id = obj.id
            plan_data = obj.subscription_plan_data

            if not plan_data:
                continue

            plan_name = plan_data.name or "(unnamed)"

            variations = plan_data.subscription_plan_variations or []
            for var in variations:
                var_id = var.id
                var_data = var.subscription_plan_variation_data
                if not var_data:
                    continue

                phases = var_data.phases or []
                for phase in phases:
                    cadence = phase.cadence or "UNKNOWN"
                    pm = getattr(phase.pricing, 'price_money', None)
                    amount = pm.amount if pm else 0
                    currency = pm.currency if pm else 'USD'
                    price_usd = (amount or 0) / 100.0
                    checkout_url = f"https://square.link/u/{var_id}"

                    print(f"Plan:          {plan_name}")
                    print(f"Plan ID:       {plan_id}")
                    print(f"Variation ID:  {var_id}")
                    print(f"Cadence:       {cadence}")
                    print(f"Price:         ${price_usd:.2f} {currency}")
                    print(f"Checkout URL:  {checkout_url}")
                    print("-" * 70)

                    rows.append({
                        'plan_name': plan_name,
                        'plan_id': plan_id,
                        'variation_id': var_id,
                        'cadence': cadence,
                        'price_usd': f"{price_usd:.2f}",
                        'checkout_url': checkout_url,
                    })

        if rows:
            csv_path = "memberships_list.csv"
            with open(csv_path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['plan_name', 'plan_id', 'variation_id', 'cadence', 'price_usd', 'checkout_url'])
                writer.writeheader()
                writer.writerows(rows)
            print(f"\nSaved to: {csv_path}")
            print("\nNext step: copy the 'checkout_url' values into website/memberships.html")
            print("           for each membership tier's 'Subscribe Now' button.\n")

        return True

    except Exception as e:
        print(f"Exception: {e}")
        return False


def create_discounts():
    """
    Create 3 Square Catalog Discount objects for member pricing.
    Staff apply these manually in Square POS when a member books a service.
    """
    access_token = os.getenv('SQUARE_ACCESS_TOKEN')
    if not access_token:
        print("ERROR: SQUARE_ACCESS_TOKEN not set in .env")
        return False

    import uuid
    client = Square(token=access_token)

    discounts = [
        {"name": "Member Discount — Bronze (20%)", "percent": "20"},
        {"name": "Member Discount — Silver (25%)", "percent": "25"},
        {"name": "Member Discount — Gold (30%)",   "percent": "30"},
    ]

    print("\n" + "="*70)
    print("CREATING MEMBER DISCOUNT CATALOG ITEMS")
    print("="*70 + "\n")

    for d in discounts:
        try:
            result = client.catalog.object.upsert(
                idempotency_key=str(uuid.uuid4()),
                object={
                    "type": "DISCOUNT",
                    "id": "#" + d["name"].replace(" ", "_").replace("(", "").replace(")", "").replace("%", "pct").lower(),
                    "discount_data": {
                        "name": d["name"],
                        "discount_type": "FIXED_PERCENTAGE",
                        "percentage": d["percent"],
                    }
                }
            )
            if result.errors:
                print(f"Error creating '{d['name']}': {result.errors}")
            else:
                print(f"Created: {d['name']}  (ID: {result.catalog_object.id})")
        except Exception as e:
            print(f"Exception creating '{d['name']}': {e}")

    print("\nDiscounts are now available in Square POS under Discounts.\n")
    return True


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="List Square membership plans or create member discounts")
    parser.add_argument('--create-discounts', action='store_true', help='Also create 20/25/30 pct discount items in Square Catalog')
    args = parser.parse_args()

    success = list_memberships()
    if success and args.create_discounts:
        create_discounts()

    sys.exit(0 if success else 1)
