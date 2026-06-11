# Pre-Setup Checklist — Square Automation

**Use this checklist before running the automation to ensure everything is ready.**

---

## ✅ Pre-Setup Verification (Before Running Scripts)

### Square Account Requirements
- [ ] You have a Square merchant account
- [ ] You can log into [Square Dashboard](https://dashboard.squareup.com)
- [ ] Your account is verified and activated
- [ ] You have admin access to create API credentials

### Get Your Credentials (5 minutes)
- [ ] Go to [Square Developer Dashboard](https://developer.squareup.com)
- [ ] Navigate to **API Keys** (left sidebar)
- [ ] Copy your **Production Access Token** (starts with `sq_live_`)
- [ ] Copy your **Application ID**
- [ ] Navigate to **Locations** (left sidebar)
- [ ] Find "ND Derma Med Spa" or your location name
- [ ] Copy the **Location ID**
- [ ] (Optional) Navigate to **Webhooks** and copy **Signature Key** if using webhooks

**You now have:**
```
✓ Access Token: sq_live_...
✓ Application ID: ...
✓ Location ID: ...
```

### Computer Setup Requirements
- [ ] Python 3.8+ installed
  - Verify: Run `python --version`
  - If not installed: Download from [python.org](https://python.org)

- [ ] Terminal/Command Prompt ready
  - Mac/Linux: Use Terminal app
  - Windows: Use Command Prompt or PowerShell

- [ ] You can navigate to the square-automation folder
  - ```bash
    cd /path/to/square-automation
    ```

- [ ] You can open the .env file in a text editor
  - Recommended: VS Code, Sublime Text, or Notepad++

### Files Ready
- [ ] `.env.example` exists in square-automation/ folder
- [ ] `scripts/full_setup.py` exists
- [ ] `scripts/test_connection.py` exists
- [ ] `scripts/create_services.py` exists
- [ ] `scripts/create_memberships.py` exists

---

## ✅ Setup Execution Checklist

### Create .env File
```bash
cp .env.example .env
```
- [ ] Command completed without errors
- [ ] `.env` file now exists in square-automation/ folder

### Edit .env File
```bash
nano .env
# or use your preferred editor
```

Fill in these **REQUIRED** fields:
- [ ] `SQUARE_ACCESS_TOKEN` = `sq_live_...` (your copied token)
- [ ] `SQUARE_APPLICATION_ID` = `...` (your copied ID)
- [ ] `SQUARE_LOCATION_ID` = `...` (your copied ID)
- [ ] `SQUARE_ENVIRONMENT` = `production` (don't change)

Optional fields (use defaults if unsure):
- [ ] `BRONZE_MONTHLY_PRICE` = `79.00`
- [ ] `SILVER_MONTHLY_PRICE` = `149.00`
- [ ] `GOLD_ANNUAL_PRICE` = `1299.00`

**Save and exit the file** (Ctrl+X, Y, Enter if using nano)

### Install Dependencies
```bash
pip install squareup pandas python-dotenv requests
```
- [ ] Installation completed without errors
- [ ] Verify: Run `python -c "import squareup; print('✓ Ready')"`

### Test Connection
```bash
python scripts/test_connection.py
```
- [ ] Command completed
- [ ] Output shows: `✓ Connection successful!`
- [ ] Shows your merchant name and location
- [ ] Shows "✓ Ready to proceed with setup"

**If test fails, troubleshoot before proceeding:**
- [ ] Double-check credentials in .env match Square Dashboard exactly
- [ ] Verify token starts with `sq_live_`
- [ ] Confirm Location ID matches your location in Square
- [ ] Re-save .env file and try test again

### Run Full Setup
```bash
python scripts/full_setup.py
```
- [ ] Script started without errors
- [ ] Watch for progress output showing services being created
- [ ] Watch for membership plans being created
- [ ] Script completed and showed "✅ SETUP COMPLETE!"
- [ ] Note the completion time shown

---

## ✅ Post-Setup Verification (After Running Scripts)

### Check Created Files
```bash
ls -la
```
- [ ] `services_created.csv` exists
- [ ] `memberships_created.csv` exists
- [ ] `setup.log` exists

### View Services Created
```bash
cat services_created.csv | head -5
```
- [ ] Shows service names, durations, prices
- [ ] Contains entries like "Laser Skin Rejuvenation", "Morpheus8 Face", etc.

### View Memberships Created
```bash
cat memberships_created.csv
```
- [ ] Shows 3 memberships:
  - Bronze Monthly ($79.00)
  - Silver Monthly ($149.00)
  - Gold Annual ($1,299.00)

### Verify in Square Dashboard

Go to [Square Dashboard](https://dashboard.squareup.com):

**Check Services**
- [ ] Catalog → Items
- [ ] Count shows 45+ items
- [ ] Services visible: Laser Skin Rejuvenation, Morpheus8, Hydrafacial, etc.
- [ ] Each service has pricing and duration

**Check Memberships**
- [ ] Subscriptions → Plans
- [ ] Shows 3 plans:
  - [ ] Bronze Monthly ($79.00)
  - [ ] Silver Monthly ($149.00)
  - [ ] Gold Annual ($1,299.00)

**Check Webhooks (if configured)**
- [ ] Developers → Webhooks
- [ ] Shows active endpoints (if WEBHOOK_URL was set)

---

## ✅ Common Issues & Solutions

### ❌ "SQUARE_ACCESS_TOKEN not found"
**Solution:**
- [ ] Check `.env` file exists: `ls -la .env`
- [ ] Open file and verify token is there
- [ ] Check for typos (must be `SQUARE_ACCESS_TOKEN=`, not similar)
- [ ] Save file (Ctrl+X, Y, Enter in nano)
- [ ] Run test again

### ❌ "Connection failed: Invalid token"
**Solution:**
- [ ] Go to Square Dashboard → Developers → API Keys
- [ ] Copy the token again (starts with `sq_live_`)
- [ ] Paste into .env file exactly as copied
- [ ] Save file
- [ ] Run test again

### ❌ "Location not found"
**Solution:**
- [ ] Go to Square Dashboard → Locations
- [ ] Find your med-spa location
- [ ] Copy the exact Location ID
- [ ] Update `SQUARE_LOCATION_ID` in .env
- [ ] Save file
- [ ] Run test again

### ❌ "ModuleNotFoundError: No module named 'squareup'"
**Solution:**
```bash
pip install squareup pandas python-dotenv requests
```
- [ ] Installation completed
- [ ] Run test again

### ❌ "python: command not found"
**Solution:**
- [ ] Python not installed or not in PATH
- [ ] Download from [python.org](https://python.org)
- [ ] During installation, select "Add Python to PATH"
- [ ] Restart terminal
- [ ] Verify: `python --version`

### ❌ Services created but not showing in Square Dashboard
**Solution:**
- [ ] Wait 1-2 minutes for sync
- [ ] Refresh the page (Cmd+R / Ctrl+R)
- [ ] Check services_created.csv: `cat services_created.csv`
- [ ] Check logs: `tail setup.log`

### ⚠️ Want to rerun setup?
**Solution:**
- Safe to rerun - won't duplicate services:
```bash
python scripts/full_setup.py
```

---

## ✅ Security Verification

- [ ] `.env` file is secure (not shared with anyone)
- [ ] `.env` file is in `.gitignore` if using Git
- [ ] API credentials are production credentials (not test)
- [ ] You understand webhooks are optional (for automated emails/SMS)
- [ ] You know where .env file is stored and can locate it later

---

## ✅ Next Steps (After Successful Setup)

1. **Document Your Configuration**
   - [ ] Save your Square credentials somewhere secure
   - [ ] Note your membership pricing (Bronze/Silver/Gold)
   - [ ] Save list of all services created

2. **Integrate Into Website**
   - [ ] Copy your Location ID to website booking page
   - [ ] Add Square Appointments widget to website
   - [ ] Set up payment forms on checkout page

3. **Test Full Flow**
   - [ ] Book a test appointment on website
   - [ ] Verify it appears in Square Dashboard
   - [ ] Test payment with Square test card (4111 1111 1111 1111)
   - [ ] Test membership signup

4. **Train Your Team**
   - [ ] Show staff the Square Dashboard
   - [ ] Explain appointment management
   - [ ] Explain membership management
   - [ ] Set up team email notifications

5. **Go Live**
   - [ ] Remove test data from Square
   - [ ] Switch to production mode
   - [ ] Start accepting real bookings

---

## ✅ Success Indicators

You'll know setup worked when:

- [ ] `python scripts/test_connection.py` shows "Connection successful"
- [ ] Services appear in Square Dashboard → Catalog → Items
- [ ] Memberships appear in Square Dashboard → Subscriptions → Plans
- [ ] CSV files are created (services_created.csv, memberships_created.csv)
- [ ] You can see all 45+ services in Square Dashboard
- [ ] You can see 3 membership plans in Square Dashboard

---

## 📞 Support Resources

If you get stuck:
1. Check the **Troubleshooting** section in `SETUP-GUIDE.md`
2. Review `README.md` for detailed explanations
3. Check [Square Documentation](https://developer.squareup.com)
4. Review `setup.log` for error details: `cat setup.log`

---

## 🎉 Congratulations!

If you've checked all boxes, your Square automation setup is complete. You now have:

✅ 45+ aesthetic services ready for booking
✅ 3 membership plans with recurring billing
✅ Secure payment processing set up
✅ Full customer management system in place
✅ Ready to integrate into your website

**Total Time: ~20 minutes**

---

**Last Updated:** March 24, 2026
**Status:** Ready for Production
**Difficulty:** Beginner-friendly (no coding required)
