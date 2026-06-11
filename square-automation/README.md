# Square Automation Setup — ND Derma Med Spa

Complete automation system to set up your Square merchant account with all aesthetic services, membership plans, and payment systems.

**Status:** ✅ Ready to Deploy
**Time to Complete:** ~20 minutes
**Difficulty:** Beginner-friendly (no coding required)

---

## 🚀 Quick Start (5 Minutes)

### 1. Get Your Square Credentials

Go to **[Square Dashboard](https://squareup.com)**:

```
1. Sign in to your merchant account
2. Navigate to: Developers → API Keys
3. Copy these three values:
   • Production Access Token (starts with 'sq_')
   • Application ID
4. Navigate to: Locations
5. Copy Location ID for your med-spa location
```

### 2. Create .env File

```bash
# In the square-automation directory:
cp .env.example .env

# Edit the file (nano, vi, or your editor):
nano .env

# Paste your credentials (replace placeholders)
# Then save (Ctrl+X, Y, Enter if using nano)
```

### 3. Test Connection

```bash
python scripts/test_connection.py
```

Should output:
```
✓ Connection successful!
✓ Merchant: ND Derma Med Spa
✓ Ready to proceed with setup
```

### 4. Run Full Setup

```bash
python scripts/full_setup.py
```

**That's it!** Your Square account is now fully configured.

---

## 📋 Installation Instructions

### Prerequisites

- Python 3.8 or higher
- pip (comes with Python)
- Square merchant account
- ~5 MB disk space

### Step 1: Install Python Dependencies

```bash
# Navigate to square-automation directory
cd square-automation

# Install required packages
pip install squareup pandas python-dotenv requests
```

Verify installation:
```bash
python -c "import squareup; print('✓ Dependencies installed')"
```

### Step 2: Set Up Environment File

```bash
# Copy example to actual file
cp .env.example .env

# Open in text editor (choose one)
nano .env           # Linux/Mac
code .env           # VS Code
# or open in any text editor
```

**Fill in these required fields:**
```env
SQUARE_ACCESS_TOKEN=sq_live_...      # From API Keys
SQUARE_APPLICATION_ID=...             # From API Keys
SQUARE_LOCATION_ID=...                # From Locations
SQUARE_ENVIRONMENT=production          # (don't change)
```

**Optional pricing fields (use defaults if unsure):**
```env
BRONZE_MONTHLY_PRICE=79.00
SILVER_MONTHLY_PRICE=149.00
GOLD_ANNUAL_PRICE=1299.00
```

### Step 3: Test Your Setup

```bash
# Test connection
python scripts/test_connection.py

# Should show:
# ✓ Connection successful!
# ✓ Merchant: ND Derma Med Spa
# ✓ Ready to proceed with setup
```

---

## 🎯 Running the Setup

### Option A: Full Automation (Easiest)

Run everything in one command:

```bash
python scripts/full_setup.py
```

**What it does:**
1. Tests connection
2. Creates 45+ aesthetic services
3. Creates 3 membership plans
4. Sets up staff (if you have staff.csv)
5. Configures webhooks (if WEBHOOK_URL is set)
6. Generates completion report

**Time:** ~5-10 minutes

### Option B: Step-by-Step (More Control)

Run each script individually:

```bash
# 1. Test connection (2 min)
python scripts/test_connection.py

# 2. Create services (3 min)
python scripts/create_services.py

# 3. Create memberships (2 min)
python scripts/create_memberships.py

# 4. Optional: Add staff (2 min)
# First create staff.csv, then:
python scripts/create_staff.py --staff-file staff.csv

# 5. Optional: Setup webhooks (1 min)
# First set WEBHOOK_URL in .env, then:
python scripts/setup_webhooks.py

# 6. Generate report (1 min)
python scripts/generate_report.py
```

---

## 📁 File Structure

```
square-automation/
├── README.md (this file)
├── SKILL.md (Claude skill documentation)
├── .env.example (copy to .env and fill in)
├── scripts/
│   ├── test_connection.py ............. Test your credentials
│   ├── create_services.py ............. Create 45+ treatments
│   ├── create_memberships.py .......... Create 3 membership plans
│   ├── create_staff.py ................ Add your team members
│   ├── setup_webhooks.py .............. Configure automations
│   ├── generate_report.py ............. Create summary report
│   └── full_setup.py .................. Run everything
├── references/
│   ├── service_catalog.csv ............ All 45 services
│   ├── membership_plans.csv ........... Membership configuration
│   └── webhook_events.json ............ Available webhook types
└── assets/
    └── staff.csv.example .............. Template for your staff
```

---

## 📊 What Gets Created

### 45+ Aesthetic Services

Organized in 6 categories:

```
✓ Advanced Laser & Energy Devices (12 services)
  └─ Ultraformer, Morpheus8, Laser treatments

✓ Facial Treatments (12 services)
  └─ Hydrafacial, Peels, Microneedling, etc.

✓ Injectables (6 services)
  └─ Botox, Fillers, Lip enhancement

✓ Hair Restoration (5 services)
  └─ Scalp treatment, Hair growth protocols

✓ Body Treatments (6 services)
  └─ Sculpting, Tightening, Cellulite reduction

✓ Vitamin & Wellness (4 services)
  └─ IV therapy, Vitamin injections
```

### 3 Membership Tiers

```
✓ Bronze Monthly: $79/month
  └─ 1 service/month @ 20% off

✓ Silver Monthly: $149/month
  └─ 2 services/month @ 25% off

✓ Gold Annual: $1,299/year
  └─ 12 services/year @ 30% off
```

### Automatic Webhooks

- Appointment confirmations (email + SMS)
- Payment processing notifications
- Membership renewal reminders
- Customer database updates

---

## 🔧 Customization

### Change Membership Prices

Edit `.env` file:
```env
BRONZE_MONTHLY_PRICE=99.00      # Change to your price
SILVER_MONTHLY_PRICE=199.00
GOLD_ANNUAL_PRICE=1599.00
```

Then rerun:
```bash
python scripts/create_memberships.py
```

### Add Your Staff Members

Create `staff.csv`:
```csv
name,email,phone,role
Sarah Johnson,sarah@nddermamedspa.com,555-0001,Aesthetician
Dr. Michael Chen,michael@nddermamedspa.com,555-0002,Consultant
Emma Rodriguez,emma@nddermamedspa.com,555-0003,Aesthetician
```

Then run:
```bash
python scripts/create_staff.py --staff-file staff.csv
```

### Enable Webhooks

Add to `.env`:
```env
WEBHOOK_URL=https://yourdomain.com/webhooks/square
```

Then run:
```bash
python scripts/setup_webhooks.py
```

---

## ✅ Verification

After setup, verify everything in **Square Dashboard**:

### Check Services Created
```
Square Dashboard → Catalog → Items
Should show 45+ items like:
✓ Laser Skin Rejuvenation
✓ Morpheus8 Face
✓ Hydrafacial
... (42 more)
```

### Check Membership Plans
```
Square Dashboard → Subscriptions → Plans
Should show 3 plans:
✓ Bronze Monthly ($79.00)
✓ Silver Monthly ($149.00)
✓ Gold Annual ($1,299.00)
```

### Check Webhooks (if configured)
```
Square Dashboard → Developers → Webhooks
Should show active webhooks for:
✓ appointment.created
✓ payment.created
✓ subscription.updated
```

---

## 🐛 Troubleshooting

### "Connection failed - Invalid API Token"

**Solution:**
1. Go to Square Dashboard → Developers → API Keys
2. Copy the exact access token (starts with `sq_`)
3. Update `.env` file
4. Run `python scripts/test_connection.py` again

### "Location not found"

**Solution:**
1. Go to Square Dashboard → Locations
2. Find your med-spa location
3. Copy the exact Location ID
4. Update `SQUARE_LOCATION_ID` in `.env`

### "Service already exists"

**Solution:**
- This is normal if you ran setup before
- Services won't be duplicated
- Or delete old services and rerun

### Scripts won't run

**Check:**
- Python 3.8+: `python --version`
- Dependencies: `pip install squareup pandas python-dotenv`
- .env file exists: `ls -la .env`
- In correct directory: `pwd` (should end in square-automation)

---

## 📞 Support

### Square Documentation
- [Square API Docs](https://developer.squareup.com)
- [Appointments API](https://developer.squareup.com/docs/appointments-api)
- [Subscriptions API](https://developer.squareup.com/docs/subscriptions-api)

### ND Derma Med Spa Docs
- `05-square-integration.md` — Complete technical guide
- `06-membership-pricing-template.md` — Pricing & operations
- `04-service-descriptions.md` — Service descriptions

### Common Issues
- Webhook not working? Check WEBHOOK_URL in .env
- Membership not showing? Try logging out of Square Dashboard
- Services appear empty? Allow 1-2 minutes for sync

---

## 🔐 Security Best Practices

✅ **DO:**
- Keep `.env` file secure
- Never commit `.env` to Git
- Use production credentials only
- Rotate API keys monthly

❌ **DON'T:**
- Hardcode credentials in scripts
- Share .env file via email
- Use same key for dev/prod
- Commit credentials to GitHub

Add to `.gitignore`:
```
.env
.env.local
*.env
secrets.json
```

---

## 📈 After Setup

### Test the Integration

1. **Test Booking:**
   - Go to your website booking page
   - Book an appointment
   - Verify confirmation email

2. **Test Payment:**
   - Use Square test card: 4111 1111 1111 1111
   - Verify payment appears in dashboard

3. **Test Membership:**
   - Sign up for membership
   - Verify recurring charge next month

### Go Live

1. Switch Square from test to production
2. Remove test data
3. Enable live payments
4. Start accepting bookings!

### Monitor & Optimize

- Track booking rate weekly
- Monitor payment success rate
- Gather customer feedback
- Adjust pricing if needed

---

## 💡 Tips & Tricks

### Run Full Setup Again?
Safe to rerun - it won't duplicate services:
```bash
python scripts/full_setup.py
```

### Check Recent Activity?
```bash
tail -f setup.log
```

### View Created Services?
```bash
cat services_created.csv
```

### Bulk Update Prices?
Edit and rerun:
```bash
# Edit .env file with new prices
python scripts/create_memberships.py --force
```

---

## 📊 Timeline

| Step | Time | What Happens |
|------|------|-------------|
| Credentials | 5 min | Copy API keys from Square |
| Setup .env | 2 min | Fill in credentials |
| Test | 1 min | Verify connection works |
| Services | 3 min | Create 45+ treatments |
| Memberships | 2 min | Create 3 plans |
| Webhooks | 1 min | Optional automation |
| Report | 1 min | Summary of setup |
| **Total** | **~20 min** | **Fully operational** |

---

## ✨ You're All Set!

Your Square merchant account is now ready for:
- ✅ Online appointment booking
- ✅ Secure payment processing
- ✅ Membership management
- ✅ Automated confirmations
- ✅ Customer analytics

**Next:** Integrate into your website and start taking bookings!

For detailed integration instructions, see:
- `05-square-integration.md` — Technical integration
- `06-membership-pricing-template.md` — Operations guide

---

**Last Updated:** March 24, 2026
**Status:** Ready for Production
**Support:** See Square docs and ND Derma documentation
