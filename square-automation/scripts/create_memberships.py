#!/usr/bin/env python3
"""
Create Square Membership Plans
Sets up 3-tier recurring subscription system (Bronze, Silver, Gold)
"""

import os
import sys
import csv
import uuid
from dotenv import load_dotenv
from square import Square

# Load environment variables
load_dotenv()

# Membership plans from 06-membership-pricing-template.md
MEMBERSHIPS = [
    {
        "name": "Bronze Monthly Membership",
        "description": "Perfect for trying our signature treatments monthly at 20% discount",
        "price": float(os.getenv('BRONZE_MONTHLY_PRICE', '79.00')),
        "billing_cycle": "MONTHLY",
        "billing_cycle_count": 1,
        "services_per_period": 1,
        "discount_percent": 20,
        "benefits": "Priority booking, Email consultation support"
    },
    {
        "name": "Silver Monthly Membership",
        "description": "For consistent aesthetic maintenance and skin health at 25% discount",
        "price": float(os.getenv('SILVER_MONTHLY_PRICE', '149.00')),
        "billing_cycle": "MONTHLY",
        "billing_cycle_count": 1,
        "services_per_period": 2,
        "discount_percent": 25,
        "benefits": "48-hour priority booking, Monthly consultation, Member events"
    },
    {
        "name": "Gold Annual Membership",
        "description": "The ultimate luxury membership for serious aesthetic commitment at 30% discount",
        "price": float(os.getenv('GOLD_ANNUAL_PRICE', '1299.00')),
        "billing_cycle": "ANNUAL",
        "billing_cycle_count": 1,
        "services_per_period": 12,
        "discount_percent": 30,
        "benefits": "VIP booking priority, Quarterly reviews, Complimentary add-ons, Loyalty rewards"
    }
]

def create_memberships():
    """Create membership subscription plans in Square"""

    print("\n" + "="*70)
    print("CREATING MEMBERSHIP PLANS")
    print("="*70 + "\n")

    # Get credentials
    access_token = os.getenv('SQUARE_ACCESS_TOKEN')
    location_id = os.getenv('SQUARE_LOCATION_ID')
    environment = os.getenv('SQUARE_ENVIRONMENT', 'production')

    if not access_token or not location_id:
        print("❌ ERROR: Missing Square credentials in .env")
        return False

    try:
        client = Square(token=access_token)

        created_memberships = []

        print("Creating membership plans...\n")

        for i, plan in enumerate(MEMBERSHIPS, 1):
            try:
                plan_id_key = "#" + plan['name'].replace(' ', '_').lower()
                variation_id_key = plan_id_key + "_var"
                # Cadence mapping
                cadence_map = {"MONTHLY": "MONTHLY", "ANNUAL": "ANNUAL"}
                cadence = cadence_map.get(plan['billing_cycle'], "MONTHLY")

                result = client.catalog.object.upsert(
                    idempotency_key=str(uuid.uuid4()),
                    object={
                        "type": "SUBSCRIPTION_PLAN",
                        "id": plan_id_key,
                        "subscription_plan_data": {
                            "name": plan['name'],
                            "subscription_plan_variations": [
                                {
                                    "type": "SUBSCRIPTION_PLAN_VARIATION",
                                    "id": variation_id_key,
                                    "subscription_plan_variation_data": {
                                        "name": plan['name'],
                                        "phases": [
                                            {
                                                "cadence": cadence,
                                                "pricing": {
                                                    "type": "STATIC",
                                                    "price_money": {
                                                        "amount": int(plan['price'] * 100),
                                                        "currency": "USD"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                )

                if result.errors:
                    print(f"⚠ [{i}] {plan['name']:35s} - Error: {result.errors}\n")
                else:
                    obj_id = result.catalog_object.id if result.catalog_object else plan_id_key
                    print(f"✓ [{i}] {plan['name']:35s} ${plan['price']:8.2f}/{plan['billing_cycle'].lower():6s}")
                    print(f"      Services: {plan['services_per_period']}/period | Discount: {plan['discount_percent']}%")
                    print(f"      Benefits: {plan['benefits']}\n")

                    created_memberships.append({
                        'plan_id': obj_id,
                        'name': plan['name'],
                        'price': plan['price'],
                        'billing_cycle': plan['billing_cycle'],
                        'services_per_period': plan['services_per_period'],
                        'discount_percent': plan['discount_percent'],
                        'benefits': plan['benefits']
                    })

            except Exception as e:
                print(f"❌ [{i}] {plan['name']:35s} - Exception: {str(e)}\n")

        # Save to CSV
        print("="*70)
        csv_filename = "memberships_created.csv"
        if created_memberships:
            with open(csv_filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['plan_id', 'name', 'price', 'billing_cycle', 'services_per_period', 'discount_percent', 'benefits'])
                writer.writeheader()
                writer.writerows(created_memberships)

            print(f"\n✅ Memberships Created: {len(created_memberships)}/{len(MEMBERSHIPS)}")
            print(f"📁 Saved to: {csv_filename}\n")

            # Print summary
            print("MEMBERSHIP SUMMARY")
            print("="*70)
            total_revenue = sum(m['price'] for m in created_memberships)
            print(f"Total Monthly Revenue (if all active): ${total_revenue:.2f}")
            print(f"Annual Member Value (avg): ${(sum([m['price'] * 12 if m['billing_cycle'] == 'MONTHLY' else m['price'] for m in created_memberships]) / len(created_memberships)):.2f}\n")

            return True
        else:
            print(f"\n❌ No memberships created\n")
            return False

    except Exception as e:
        print(f"❌ Error creating memberships: {str(e)}")
        return False

if __name__ == "__main__":
    success = create_memberships()
    sys.exit(0 if success else 1)
