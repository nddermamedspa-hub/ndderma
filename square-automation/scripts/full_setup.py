#!/usr/bin/env python3
"""
Full Square Setup Automation
Runs all setup steps in sequence
"""

import os
import sys
import time
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def run_script(script_name, description):
    """Run a Python script and report results"""
    print(f"\n{'='*70}")
    print(f"STEP: {description}")
    print('='*70)

    try:
        result = subprocess.run(
            [sys.executable, f"scripts/{script_name}"],
            capture_output=False,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running {script_name}: {str(e)}")
        return False

def full_setup():
    """Run all setup steps"""

    start_time = time.time()

    print("\n" + "╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  ND DERMA MED SPA — COMPLETE SQUARE SETUP AUTOMATION".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝\n")

    # Step 1: Test connection
    if not run_script("test_connection.py", "Testing Square Connection"):
        print("\n❌ Connection test failed. Please check your .env file.")
        return False

    # Step 2: Create services
    if not run_script("create_services.py", "Creating Services Catalog (45+ treatments)"):
        print("\n⚠  Service creation had issues, but continuing...")

    # Step 3: Create memberships
    if not run_script("create_memberships.py", "Creating Membership Plans (Bronze/Silver/Gold)"):
        print("\n⚠  Membership creation had issues, but continuing...")

    # Step 4: Check for staff file and create staff if exists
    if os.path.exists("staff.csv"):
        if not run_script("create_staff.py", "Creating Staff Members"):
            print("\n⚠  Staff creation had issues, but continuing...")
    else:
        print(f"\n{'='*70}")
        print("SKIPPING: Create Staff Members")
        print(f"{'='*70}")
        print("(Create staff.csv in the square-automation directory to add staff)\n")

    # Step 5: Setup webhooks (optional)
    if os.getenv('WEBHOOK_URL'):
        if not run_script("setup_webhooks.py", "Setting Up Webhooks"):
            print("\n⚠  Webhook setup had issues, but continuing...")
    else:
        print(f"\n{'='*70}")
        print("SKIPPING: Setup Webhooks")
        print(f"{'='*70}")
        print("(Add WEBHOOK_URL to .env to enable webhooks)\n")

    # Step 6: Generate report
    if not run_script("generate_report.py", "Generating Setup Report"):
        print("\n⚠  Report generation had issues.")

    # Summary
    end_time = time.time()
    duration = end_time - start_time
    minutes = int(duration // 60)
    seconds = int(duration % 60)

    print("\n" + "╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  ✅ SETUP COMPLETE!".center(68) + "║")
    print("║" + f"  Completed in {minutes}m {seconds}s".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")

    print("\n" + "="*70)
    print("NEXT STEPS:")
    print("="*70)
    print("""
1. ✅ Square Services Created (45+ treatments)
   - View in: Square Dashboard → Catalog → Items

2. ✅ Membership Plans Active (Bronze/Silver/Gold)
   - View in: Square Dashboard → Subscriptions → Plans

3. 📋 Integrate into Website
   - Add Square Appointments widget to booking page
   - Add payment forms to checkout
   - Add membership comparison table

4. 🧪 Test Full Flow
   - Test booking an appointment
   - Test payment processing
   - Test membership signup

5. 🚀 Go Live
   - Switch Square to production mode
   - Monitor first bookings
   - Gather customer feedback

6. 📊 Track Metrics
   - Booking rate
   - Payment success rate
   - Membership adoption

For more details, see:
- 05-square-integration.md (technical guide)
- 06-membership-pricing-template.md (pricing & operations)
""")
    print("="*70 + "\n")

    return True

if __name__ == "__main__":
    try:
        success = full_setup()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed with error: {str(e)}")
        sys.exit(1)
