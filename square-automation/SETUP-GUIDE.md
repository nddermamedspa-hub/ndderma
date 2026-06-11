# Complete Setup Guide — Square Automation for ND Derma Med Spa

**Time Required:** 20 minutes
**Difficulty:** Beginner-friendly
**Prerequisites:** Python 3.8+, Square merchant account

---

## 📋 Step-by-Step Setup

### Phase 1: Prepare Your Square Account (5 minutes)

#### Step 1: Create a Square Merchant Account

If you don't have one:
1. Go to [squareup.com](https://squareup.com)
2. Click "Sign Up"
3. Fill in your business information
4. Verify your email
5. Complete identity verification

#### Step 2: Get Your API Credentials

1. **Sign into Square Dashboard:** [dashboard.squareup.com](https://dashboard.squareup.com)
2. **Navigate to Developers:**
   - Click your profile icon (top right)
   - Select "Developer Dashboard" or go to [developer.squareup.com](https://developer.squareup.com)

3. **Copy Your Production Credentials:**
   - Click "API Keys" (left sidebar)
   - Under "Production Credentials," you'll see:
     - **Access Token** (starts with `sq_live_`)
     - **Application ID**
   - Copy both values to a text file temporarily

4. **Get Your Location ID:**
   - Click "Locations" (left sidebar)
   - Find "ND Derma Med Spa" or your med-spa location
   - Copy the Location ID

5. **Optional - Get Webhook Signature Key:**
   - Click "Webhooks" (left sidebar)
   - Copy your Signature Key (if you want automated emails/SMS)

**You now have:**
- ✅ Access Token
- ✅ Application ID
- ✅ Location ID
- ✅ (Optional) Webhook Signature Key

---

### Phase 2: Prepare Your Computer (5 minutes)

#### Step 1: Verify Python Installation

Open terminal/command prompt and run:

```bash
python --version
```

Should show Python 3.8 or higher. If not:
- Download from [python.org](https://python.org)
- Install (select "Add Python to PATH" during installation)

#### Step 2: Navigate to square-automation Directory

```bash
# Mac/Linux
cd ~/path/to/square-automation

# Windows
cd C:\path\to\square-automation
```

#### Step 3: Install Dependencies

```bash
pip install squareup pandas python-dotenv requests
```

Verify:
```bash
python -c "import squareup; print('✓ Ready')"
```

Should print: `✓ Ready`

---

### Phase 3: Configure Credentials (3 minutes)

#### Step 1: Create .env File

In the `square-automation` directory:

```bash
cp .env.example .env
```

#### Step 2: Edit .env File

Open `.env` in your text editor and fill in these fields:

```env
# Required - from Square Dashboard
SQUARE_ACCESS_TOKEN=sq_live_[PASTE YOUR TOKEN HERE]
SQUARE_APPLICATION_ID=[PASTE YOUR APP ID HERE]
SQUARE_LOCATION_ID=[PASTE YOUR LOCATION ID HERE]
SQUARE_ENVIRONMENT=production

# Optional pricing - change if desired
BRONZE_MONTHLY_PRICE=79.00
SILVER_MONTHLY_PRICE=149.00
GOLD_ANNUAL_PRICE=1299.00

# Optional - for webhooks
WEBHOOK_URL=https://yourdomain.com/webhooks/square
WEBHOOK_SIGNATURE_KEY=[IF USING WEBHOOKS]
```

**⚠️ Important Security Notes:**
- Never share this file
- Never commit to Git
- Keep the `SQUARE_ACCESS_TOKEN` private
- This file won't be committed (added to .gitignore)

#### Step 3: Save the File

Save the changes (Ctrl+S, Cmd+S, etc.)

---

### Phase 4: Test Your Setup (2 minutes)

Run the connection test:

```bash
python scripts/test_connection.py
```

**Expected Output:**
```
✓ Connection successful!
✓ Merchant: ND Derma Med Spa
✓ Location: New York
✓ Ready to proceed with setup
```

If you see errors:
- ❌ "SQUARE_ACCESS_TOKEN not found" → Check .env file
- ❌ "Location not found" → Verify SQUARE_LOCATION_ID is correct
- ❌ "Invalid token" → Copy token again from Square Dashboard

**Once test passes, proceed to Phase 5.**

---

### Phase 5: Run the Full Setup (5 minutes)

Now run the complete automation:

```bash
python scripts/full_setup.py
```

**What it does (automatically):**
1. Tests connection ✓
2. Creates 45+ aesthetic services ✓
3. Creates 3 membership plans (Bronze/Silver/Gold) ✓
4. Creates staff (if staff.csv exists)
5. Sets up webhooks (if WEBHOOK_URL is set)
6. Generates completion report ✓

**You'll see output like:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ND DERMA MED SPA — COMPLETE SQUARE SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Laser Skin Rejuvenation (60 min, $200.00)
✓ Morpheus8 Face (60 min, $350.00)
...
✓ Bronze Monthly Membership ($79.00/month)
✓ Silver Monthly Membership ($149.00/month)
✓ Gold Annual Membership ($1,299.00/year)

✅ SETUP COMPLETE! (2m 15s)
```

**That's it! Your Square account is fully configured.**

---

## ✅ Verification Checklist

### In Square Dashboard

Check that everything was created:

#### Services Created
```
Square Dashboard → Catalog → Items
☐ 45+ items shown (Laser, Morpheus8, Facials, etc.)
☐ Each has pricing and duration
☐ All 6 categories represented
```

#### Memberships Created
```
Square Dashboard → Subscriptions → Plans
☐ Bronze Monthly ($79.00)
☐ Silver Monthly ($149.00)
☐ Gold Annual ($1,299.00)
```

#### Webhooks (if configured)
```
Square Dashboard → Developers → Webhooks
☐ Endpoints active
☐ appointment.created webhook
☐ payment.created webhook
```

### In Your Directory

Check that files were created:

```
square-automation/
☐ .env (your credentials file)
☐ services_created.csv (list of all services)
☐ memberships_created.csv (list of memberships)
☐ setup.log (detailed log of everything)
```

View the created services:
```bash
cat services_created.csv
```

---

## 🎯 Optional Additions

### Add Your Staff Members

Create `staff.csv`:

```csv
name,email,phone,role
Sarah Johnson,sarah@nddermamedspa.com,555-0001,Aesthetician
Dr. Michael Chen,michael@nddermamedspa.com,555-0002,Consultant
Emma Rodriguez,emma@nddermamedspa.com,555-0003,Aesthetician
```

Run:
```bash
python scripts/create_staff.py --staff-file staff.csv
```

### Enable Automatic Confirmations

Add to `.env`:
```env
WEBHOOK_URL=https://yourdomain.com/webhooks/square
WEBHOOK_SIGNATURE_KEY=your_key_from_square
```

Run:
```bash
python scripts/setup_webhooks.py
```

### Change Membership Prices

Edit `.env`:
```env
BRONZE_MONTHLY_PRICE=99.00
SILVER_MONTHLY_PRICE=199.00
GOLD_ANNUAL_PRICE=1599.00
```

Rerun:
```bash
python scripts/create_memberships.py
```

---

## 🚀 Next Steps After Setup

### 1. Integrate Into Your Website

Add Square Appointments widget to your booking page:

```html
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

Replace `YOUR_LOCATION_ID` with your actual location ID.

### 2. Test Booking Flow

1. Go to your website booking page
2. Book a test appointment
3. Check that confirmation email arrives
4. Verify appointment appears in Square Dashboard

### 3. Test Payment Processing

1. Use Square test card: `4111 1111 1111 1111`
2. Any future date and CVC
3. Verify payment shows in Square Dashboard

### 4. Test Membership Signup

1. Have a customer sign up for membership
2. Verify first charge is processed
3. Set reminder to check next month's renewal

### 5. Monitor Metrics

After going live, track:
- Booking rate per day
- Payment success rate
- Membership adoption
- Customer satisfaction

### 6. Optimize & Improve

- Adjust prices if needed
- Add more services based on demand
- Gather customer feedback
- Update promotions seasonally

---

## 🐛 Troubleshooting

### Problem: "python: command not found"

**Solution:**
- Python not installed or not in PATH
- Reinstall Python from [python.org](https://python.org)
- Make sure to check "Add Python to PATH"

### Problem: "ModuleNotFoundError: No module named 'squareup'"

**Solution:**
```bash
pip install squareup pandas python-dotenv
```

### Problem: "SQUARE_ACCESS_TOKEN not found in .env"

**Solution:**
1. Make sure you copied `.env.example` to `.env`
2. Open `.env` and verify it has your token
3. Check for typos in file name (must be exactly `.env`)

### Problem: "Connection failed: Invalid token"

**Solution:**
1. Go back to Square Dashboard → API Keys
2. Copy the exact token (including `sq_live_` prefix)
3. Paste into `.env` file
4. Run `python scripts/test_connection.py` again

### Problem: "Location not found"

**Solution:**
1. Square Dashboard → Locations
2. Find your med-spa location
3. Copy the exact Location ID
4. Update `SQUARE_LOCATION_ID` in `.env`

### Problem: Services created but not showing in Square Dashboard

**Solution:**
- Wait 1-2 minutes for sync
- Refresh the page
- Check `.csv` file: `cat services_created.csv`
- Check logs: `tail setup.log`

### Problem: Want to rerun setup?

**Solution:**
Safe to rerun - won't duplicate services:
```bash
python scripts/full_setup.py
```

If you want to start fresh:
1. Delete services from Square Dashboard
2. Rerun setup script

---

## 📞 Support & Documentation

### Square Documentation
- [Square Developers](https://developer.squareup.com)
- [Appointments API](https://developer.squareup.com/docs/appointments-api)
- [Subscriptions API](https://developer.squareup.com/docs/subscriptions-api)

### ND Derma Documentation
- `SKILL.md` — Claude skill documentation
- `README.md` — Quick reference
- `05-square-integration.md` — Full technical guide
- `06-membership-pricing-template.md` — Pricing & operations

### Contact
For issues:
1. Check troubleshooting section above
2. Review Square documentation
3. Check your `.env` file configuration
4. Review setup logs: `cat setup.log`

---

## ✨ Success Indicators

You'll know setup worked when:

✅ `python scripts/test_connection.py` shows "Connection successful"
✅ Services appear in Square Dashboard → Catalog
✅ Memberships appear in Square Dashboard → Subscriptions
✅ `.csv` files are created in square-automation directory
✅ You can see appointment booking calendar in Square Dashboard

---

## 🎉 Congratulations!

Your Square setup is complete. You now have:

- 45+ aesthetic services ready for booking
- 3 membership plans with recurring billing
- Secure payment processing
- Automated confirmations (optional)
- Full customer management system

**Ready to integrate into your website and start taking bookings!**

For integration instructions, see: `05-square-integration.md`

---

**Last Updated:** March 24, 2026
**Status:** Ready for Production
**Estimated Time:** 20 minutes
**Difficulty:** Beginner-friendly
