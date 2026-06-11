---
name: square-setup-automation
description: Fully automates Square merchant setup for med-spa bookings, payments, and memberships. Use this skill whenever you need to: create a Square services catalog from documentation, set up 24+ aesthetic treatments with pricing, configure 3-tier membership plans (Bronze/Silver/Gold) with recurring billing, create staff members and locations, set up payment forms and webhooks, bulk import services via CSV, or query Square data. This skill is essential for med-spa websites integrating Square Appointments (booking calendar), Square Payments (deposits and checkouts), and Square Subscriptions (membership recurring revenue). Trigger on any request involving Square merchant setup, service creation, membership configuration, or API automation for appointment/payment systems.
compatibility: "Python 3.8+, squareup SDK, pandas, python-dotenv"
---

# Square Setup Automation Skill

## Overview

This skill automates the complete Square merchant setup for **ND Derma Med Spa**, including:
- ✅ 24+ aesthetic services (with pricing & duration)
- ✅ 3-tier membership plans (Bronze, Silver, Gold)
- ✅ Staff members & locations
- ✅ Payment forms & webhooks
- ✅ Customer database initialization
- ✅ Full reporting

## Quick Start

### Prerequisites
1. **Square Merchant Account** — Created at [squareup.com](https://squareup.com)
2. **API Credentials** — Access token, location ID, application ID
3. **Environment File** — `.env` with credentials (see below)
4. **Python 3.8+** with required packages

### Installation

```bash
# Clone or download the automation scripts
cd square-automation

# Install dependencies
pip install squareup pandas python-dotenv requests

# Create .env file with your credentials
cp .env.example .env
# Edit .env and add your Square API keys
```

### Running the Setup

```bash
# 1. Test your connection
python scripts/test_connection.py

# 2. Create all services (24+ treatments)
python scripts/create_services.py

# 3. Create membership plans
python scripts/create_memberships.py

# 4. Create staff members
python scripts/create_staff.py

# 5. Set up payment webhooks
python scripts/setup_webhooks.py

# 6. Generate a setup report
python scripts/generate_report.py
```

**Or run everything at once:**
```bash
python scripts/full_setup.py
```

---

## Environment Setup

### .env File Format

Create a `.env` file in the `square-automation/` directory:

```env
# Square API Credentials
SQUARE_ACCESS_TOKEN=sq_live_your_access_token_here
SQUARE_APPLICATION_ID=your_application_id_here
SQUARE_LOCATION_ID=your_location_id_here
SQUARE_ENVIRONMENT=production

# Webhook Configuration (optional)
WEBHOOK_URL=https://yourdomain.com/webhooks/square
WEBHOOK_SIGNATURE_KEY=your_signature_key

# Merchant Details
MERCHANT_NAME=ND Derma Med Spa
MERCHANT_EMAIL=owner@nddermamedspa.com
MERCHANT_PHONE=+1-555-0000
MERCHANT_ADDRESS=123 Luxury Lane, City, ST 12345

# Membership Pricing (set your prices here)
BRONZE_MONTHLY_PRICE=79.00
SILVER_MONTHLY_PRICE=149.00
GOLD_ANNUAL_PRICE=1299.00

# Service Pricing Multiplier (optional)
DEFAULT_SERVICE_PRICE=200.00
```

**⚠️ Security Warning:** Never commit `.env` to Git. Add to `.gitignore`:
```
.env
.env.local
*.env
```

---

## Available Scripts

### 1. `test_connection.py`
**Purpose:** Verify your Square credentials work

**Usage:**
```bash
python scripts/test_connection.py
```

**Output:**
```
✓ Connection successful!
✓ Merchant: ND Derma Med Spa
✓ Location: New York
✓ Ready to proceed with setup
```

---

### 2. `create_services.py`
**Purpose:** Create all 24+ aesthetic services in Square

**Services Created:**
- Advanced Laser & Energy Devices (12 services)
- Facial Treatments (12 services)
- Injectables (6 services)
- Hair Restoration (5 services)
- Body Treatments (6 services)
- Vitamin & Wellness (4 services)

**Usage:**
```bash
python scripts/create_services.py
```

**Output:**
```
Creating services...
✓ Laser Skin Rejuvenation (60 min, $200)
✓ Morpheus8 Face (60 min, $350)
✓ Hydrafacial (45 min, $150)
...
Created 45 services successfully!
Services saved to services_created.csv
```

---

### 3. `create_memberships.py`
**Purpose:** Set up 3 membership subscription plans

**Plans Created:**
- **Bronze Monthly:** 1 service/month @ 20% off
- **Silver Monthly:** 2 services/month @ 25% off
- **Gold Annual:** 12 services/year @ 30% off

**Usage:**
```bash
python scripts/create_memberships.py
```

**Output:**
```
Creating memberships...
✓ Bronze Monthly Membership ($79.00/month)
✓ Silver Monthly Membership ($149.00/month)
✓ Gold Annual Membership ($1,299.00/year)

Memberships created successfully!
```

---

### 4. `create_staff.py`
**Purpose:** Create staff members (aestheticians, consultants)

**Usage:**
```bash
python scripts/create_staff.py --staff-file staff.csv
```

**staff.csv Format:**
```csv
name,email,phone,role
Sarah Johnson,sarah@nddermamedspa.com,555-0001,Aesthetician
Dr. Michael Chen,michael@nddermamedspa.com,555-0002,Consultant
Emma Rodriguez,emma@nddermamedspa.com,555-0003,Aesthetician
```

**Output:**
```
✓ Sarah Johnson (Aesthetician)
✓ Dr. Michael Chen (Consultant)
✓ Emma Rodriguez (Aesthetician)

3 staff members created!
```

---

### 5. `setup_webhooks.py`
**Purpose:** Configure webhooks for automated email/SMS

**Webhooks Created:**
- Appointment confirmations
- Payment processing
- Membership renewals
- Customer notifications

**Usage:**
```bash
python scripts/setup_webhooks.py
```

**Output:**
```
Setting up webhooks...
✓ appointment.created
✓ payment.created
✓ subscription.updated
✓ customer.created

Webhooks configured successfully!
```

---

### 6. `generate_report.py`
**Purpose:** Generate a setup summary report

**Usage:**
```bash
python scripts/generate_report.py --output setup_report.html
```

**Report Includes:**
- Total services created
- Membership plans configured
- Staff members added
- Revenue projections
- Next steps

---

### 7. `full_setup.py`
**Purpose:** Run all setup steps in sequence

**Usage:**
```bash
python scripts/full_setup.py
```

**What It Does:**
1. Tests connection
2. Creates all 45 services
3. Creates 3 membership plans
4. Creates staff (if staff.csv exists)
5. Sets up webhooks
6. Generates report
7. Outputs summary

**Output:**
```
╔════════════════════════════════════════════╗
║   ND DERMA MED SPA - SQUARE SETUP COMPLETE ║
╚════════════════════════════════════════════╝

✓ 45 services created
✓ 3 memberships configured
✓ Webhooks active
✓ Staff: 3 members
✓ Revenue ready: $XX,XXX/month

Setup completed in 2m 15s
```

---

## Step-by-Step Setup Guide

### Phase 1: Prepare (5 minutes)

1. **Create Square Account**
   ```
   Go to https://squareup.com
   Sign up for merchant account
   Complete business verification
   ```

2. **Get API Credentials**
   ```
   Square Dashboard → Developers → API Keys
   Copy: Access Token, Application ID, Location ID
   ```

3. **Create .env File**
   ```bash
   cp .env.example .env
   # Edit with your credentials
   nano .env  # or vi, code, etc.
   ```

### Phase 2: Test Connection (2 minutes)

```bash
python scripts/test_connection.py
# Should output: ✓ Connection successful!
```

### Phase 3: Create Services (5 minutes)

```bash
python scripts/create_services.py
# Creates 45 aesthetic services from documentation
```

### Phase 4: Create Memberships (2 minutes)

```bash
python scripts/create_memberships.py
# Creates 3 recurring membership plans
```

### Phase 5: Add Staff (2 minutes - Optional)

```bash
# Create staff.csv with your team members
python scripts/create_staff.py --staff-file staff.csv
```

### Phase 6: Setup Webhooks (2 minutes - Optional)

```bash
python scripts/setup_webhooks.py
# Configures automated confirmations & reminders
```

### Phase 7: Generate Report (1 minute)

```bash
python scripts/generate_report.py
# Creates setup summary and next steps
```

**Total Setup Time: ~20 minutes**

---

## Configuration Files

### services.csv
Auto-generated file with all created services:
```csv
service_id,name,duration_minutes,price,category
L001,Laser Skin Rejuvenation,60,200.00,Advanced Laser
M001,Morpheus8 Face,60,350.00,Advanced Laser
H001,Hydrafacial,45,150.00,Facial Treatments
...
```

### memberships.csv
Auto-generated file with membership configuration:
```csv
plan_id,name,price,billing_cycle,discount_percent
BRONZE_MONTHLY,Bronze Monthly,79.00,monthly,20
SILVER_MONTHLY,Silver Monthly,149.00,monthly,25
GOLD_ANNUAL,Gold Annual,1299.00,annual,30
```

### staff.csv (Input)
File you create with your team:
```csv
name,email,phone,role
Sarah Johnson,sarah@nddermamedspa.com,555-0001,Aesthetician
Dr. Michael Chen,michael@nddermamedspa.com,555-0002,Consultant
```

---

## Troubleshooting

### Error: "Invalid API Token"
- **Cause:** Wrong access token in .env
- **Fix:** Verify token in Square Dashboard → Developers → API Keys
- **Try:** `python scripts/test_connection.py`

### Error: "Location not found"
- **Cause:** Location ID doesn't exist for your merchant
- **Fix:** Go to Square Dashboard → Locations, copy correct ID
- **Try:** Update .env with correct SQUARE_LOCATION_ID

### Error: "Service already exists"
- **Cause:** Services were created in a previous run
- **Fix:** Check Square Dashboard → Catalog → Services
- **Options:**
  - Run script again (it skips duplicates)
  - Delete existing services and rerun
  - Use `--force` flag: `python scripts/create_services.py --force`

### Services didn't create
- **Check logs:** `tail -f setup.log`
- **Verify:** Go to Square Dashboard → Catalog → Services
- **Rerun:** `python scripts/create_services.py --verbose`

### Memberships not showing in Square
- **Check:** Square Dashboard → Subscriptions → Plans
- **Verify:** Correct pricing in .env file
- **Debug:** `python scripts/create_memberships.py --verbose`

---

## What Gets Created in Square

### Services Catalog
- 45 total services across 6 categories
- Pricing from $75 to $500
- Durations: 30-90 minutes
- Ready for online booking

### Membership Plans
- 3 subscription types
- Recurring monthly/annual billing
- Automatic customer charging
- Member portal access

### Staff Directory
- Team members added
- Availability scheduling ready
- Service assignments
- Customer booking preferences

### Payment Processing
- Deposits configuration (50% default)
- Full payment options
- Refund handling
- Payment forms ready

---

## Integration with Website

### Embed Square Appointments Widget
```html
<!-- Add to your booking page -->
<div id="square-appointments"></div>
<script src="https://web.squarecdn.com/v1/square.js"></script>
<script>
  const appointments = new sq.appointments.AppointmentsPlus({
    locationId: "YOUR_LOCATION_ID",
    containerId: "square-appointments"
  });
  appointments.mount();
</script>
```

### Embed Payment Form
```html
<!-- Add to checkout/payment page -->
<form id="sq-payment-form">
  <div id="sq-card-element"></div>
  <button type="submit">Pay Now</button>
</form>
<script src="https://web.squarecdn.com/v1/square.js"></script>
```

### Connect to Elementor
1. Go to Elementor Page Editor
2. Add "HTML" widget
3. Paste the appointment widget code
4. Configure with your location ID
5. Publish and test

---

## Next Steps After Setup

1. **Test Booking Flow**
   - Go to Square Appointments
   - Book a test appointment
   - Verify confirmation email

2. **Test Payment Processing**
   - Use Square test card: 4111 1111 1111 1111
   - Verify payment shows in dashboard

3. **Add Member Testimonials**
   - Collect feedback from test bookings
   - Add to website

4. **Go Live**
   - Switch Square to production
   - Remove test data
   - Enable live payments

5. **Monitor & Optimize**
   - Track booking rate
   - Monitor payment success
   - Gather customer feedback

---

## Support & Documentation

**Square Resources:**
- [Square API Docs](https://developer.squareup.com)
- [Appointments API](https://developer.squareup.com/docs/appointments-api)
- [Subscriptions API](https://developer.squareup.com/docs/subscriptions-api)
- [Webhooks](https://developer.squareup.com/docs/webhooks)

**ND Derma Med Spa Docs:**
- `05-square-integration.md` — Complete technical guide
- `06-membership-pricing-template.md` — Pricing & operations
- `04-service-descriptions.md` — Service copy for import

---

## Tips & Best Practices

### Best Practices

✅ **DO:**
- Test with test credentials first
- Keep .env file secure (gitignore)
- Create staff before assigning services
- Set up webhooks for confirmations
- Generate reports after setup

❌ **DON'T:**
- Hardcode API tokens
- Commit .env to GitHub
- Use production credentials for testing
- Skip webhook setup
- Leave test data in production

### Optimization Tips

- **Bulk import:** Use CSV files for large datasets
- **Batch operations:** Run `full_setup.py` once instead of individually
- **Archive old services:** Keep production clean
- **Monitor usage:** Check Square Dashboard for API limits

---

## File Structure

```
square-automation/
├── SKILL.md (this file)
├── .env.example
├── scripts/
│   ├── test_connection.py
│   ├── create_services.py
│   ├── create_memberships.py
│   ├── create_staff.py
│   ├── setup_webhooks.py
│   ├── generate_report.py
│   └── full_setup.py
├── references/
│   ├── service_catalog.csv
│   ├── membership_plans.csv
│   └── webhook_events.json
└── assets/
    ├── .env.example
    └── staff.csv.example
```

---

**Status:** Ready to deploy
**Last Updated:** March 24, 2026
**Next Step:** Create .env file and run `python scripts/test_connection.py`
