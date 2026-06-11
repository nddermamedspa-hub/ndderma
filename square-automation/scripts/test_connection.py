#!/usr/bin/env python3
"""
Test Square API Connection
Verifies that your credentials are valid and ready for setup
"""

import os
import sys
from dotenv import load_dotenv
from square import Square

# Load environment variables
load_dotenv()

def test_connection():
    """Test connection to Square API"""

    print("\n" + "="*70)
    print("ND DERMA MED SPA — SQUARE CONNECTION TEST")
    print("="*70 + "\n")

    # Get credentials
    access_token = os.getenv('SQUARE_ACCESS_TOKEN')
    app_id = os.getenv('SQUARE_APPLICATION_ID')
    location_id = os.getenv('SQUARE_LOCATION_ID')
    environment = os.getenv('SQUARE_ENVIRONMENT', 'production')

    # Validate credentials exist
    print("Checking credentials...")
    if not access_token:
        print("❌ ERROR: SQUARE_ACCESS_TOKEN not found in .env")
        return False
    if not app_id:
        print("❌ ERROR: SQUARE_APPLICATION_ID not found in .env")
        return False
    if not location_id:
        print("❌ ERROR: SQUARE_LOCATION_ID not found in .env")
        return False

    print(f"✓ Access Token: {access_token[:20]}...{access_token[-5:]}")
    print(f"✓ Application ID: {app_id}")
    print(f"✓ Location ID: {location_id}")
    print(f"✓ Environment: {environment}\n")

    # Create client
    try:
        print("Connecting to Square API...")
        client = Square(token=access_token)

        # Test API call - get location details
        result = client.locations.get(location_id=location_id)

        if result.errors:
            print(f"❌ API Error: {result.errors}")
            return False

        location = result.location
        print("✓ Connection successful!\n")
        print(f"✓ Merchant: {location.name}")
        print(f"✓ Location: {location.name}")
        print(f"✓ Address: {location.address.address_line1 if location.address else 'N/A'}")
        print(f"✓ Phone: {location.phone_number or 'N/A'}")
        print(f"✓ Status: {location.status}\n")

        # Test catalog access
        print("Checking catalog access...")
        catalog_result = client.catalog.list(types="ITEM")
        item_count = len(list(catalog_result)) if catalog_result else 0
        print(f"✓ Catalog accessible ({item_count} existing items)\n")

        # Test customer access
        print("Checking customer access...")
        customers_result = client.customers.list()
        customer_count = len(list(customers_result)) if customers_result else 0
        print(f"✓ Customers accessible ({customer_count} customers)\n")

        print("="*70)
        print("✅ ALL CHECKS PASSED - READY FOR SETUP!")
        print("="*70)
        print("\nNext steps:")
        print("1. venv/bin/python scripts/create_services.py")
        print("2. venv/bin/python scripts/create_memberships.py")
        print("3. venv/bin/python scripts/full_setup.py\n")

        return True

    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        print("\nTroubleshooting:")
        print("• Verify SQUARE_ACCESS_TOKEN is correct")
        print("• Verify SQUARE_LOCATION_ID exists")
        print("• Check internet connection")
        print("• Ensure .env file is in the square-automation directory\n")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
