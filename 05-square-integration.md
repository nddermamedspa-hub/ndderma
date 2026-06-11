# Square Integration Guide — ND Derma Med Spa

**Status:** Implementation Guide
**Last Updated:** March 24, 2026

---

## 📋 Overview

This guide covers the complete integration of **Square** into the ND Derma Med Spa website for:
- **Online Appointment Booking**
- **Payment Processing** (deposits, full payments, memberships)
- **Membership Management** (recurring subscriptions)
- **Client Management** (customer database)

---

## 🔧 Square Setup — Prerequisites

Before integrating Square into your Elementor site, complete these steps:

### 1. Create Square Account
- Go to [squareup.com](https://squareup.com)
- Sign up for a merchant account
- Verify your business information
- Enable payment processing

### 2. Gather API Credentials
From your Square Dashboard:
1. Go to **Developers** → **API Keys**
2. Copy your **Production Access Token**
3. Copy your **Application ID**
4. Note your **Location ID** (under Locations)
5. Generate an **API Key** for webhooks (if needed)

### 3. Configure Payment Settings
1. Go to **Settings** → **Payment Methods**
2. Enable online payments
3. Set up payment processing fees (if applicable)
4. Configure payment receipt settings

---

## 📅 Square Appointments Integration

### A. Set Up Location & Staff in Square

1. **Create Location:**
   - Go to **Locations** in Square Dashboard
   - Create location: "ND Derma Med Spa"
   - Add business phone, address, hours

2. **Create Staff Members:**
   - Go to **Staff** in Square Dashboard
   - Add your practitioners/aestheticians
   - Assign roles (e.g., "Aesthetician," "Consultant")

3. **Create Service Categories:**
   - Advanced Laser & Energy Devices
   - Facial Treatments
   - Injectables
   - Hair Restoration & Scalp Treatments
   - Body Treatments
   - Vitamin & Wellness Therapy

### B. Create Services in Square

For each service, configure:
- **Service Name** (e.g., "Laser Skin Rejuvenation")
- **Description** (short copy from 04-service-descriptions.md)
- **Duration** (30 min, 60 min, 90 min, etc.)
- **Price** (base service price)
- **Category** (from above)
- **Staff Assignment** (who can provide this service)
- **Color Code** (for calendar visibility)

**Example Service Configuration:**

```
Service: Morpheus8 Face
Description: A powerful RF microneedling combination that remodels collagen, 
             tightens skin, and improves texture for a refined, lifted appearance.
Duration: 60 minutes
Price: $[TO BE SET]
Category: Advanced Laser & Energy Devices
Staff: All aestheticians
Color: Gold
```

### C. Enable Appointments on Website

**Using Elementor Pro + Square Appointments Widget:**

1. Install **Square** payment plugin in WordPress
2. Go to your Elementor **Booking Page** (03-booking.md)
3. Add a new widget: **Square Appointments**
4. Configure:
   - **Location:** ND Derma Med Spa
   - **Display Mode:** Embedded calendar
   - **Services:** Show all services
   - **Staff:** Show staff bios
5. Set appointment confirmation email settings
6. Enable SMS reminders (optional)

**Alternative: Embedded Appointments Link**

If using a simple button approach:
- Generate Square Appointments link: `https://squareup.com/appointments/[BUSINESS_ID]`
- Create "Book Now" button linking to this URL

### D. Booking Flow (Client Perspective)

1. Client clicks "Book Now"
2. Square Appointments opens
3. Client selects:
   - Service category
   - Specific service
   - Preferred practitioner (optional)
   - Date & time from available calendar
4. Client enters:
   - Name
   - Email
   - Phone
   - Notes (treatment goals, concerns)
5. Client pays deposit or full amount
6. Confirmation sent (email + SMS)
7. Calendar invite generated

---

## 💳 Payment Integration

### A. Set Up Square Payments in Elementor

1. Install **Square for WooCommerce** (if using WooCommerce) OR
2. Use **Elementor Payment Forms** with Square gateway

### B. Payment Points of Integration

**1. Booking Confirmation Page**
- Charge booking deposit
- Default: 50% of service price OR flat rate
- Payment form embedded in confirmation page

**2. Service Packages Page**
- Display package pricing
- "Add to Cart" or "Purchase Now" button
- Links to checkout page with Square payment

**3. Membership Page**
- Display monthly/annual membership plans
- "Subscribe Now" buttons
- Recurring payment setup

**4. Gift Card Purchase**
- Optional: Sell gift certificates
- Integrate Square Gift Cards

### C. Payment Configuration Example

**Service: Full Face Rejuvenation Consultation**
- Service Price: $[TO BE SET]
- Booking Deposit: 50% (non-refundable)
- Deposit Amount: Calculated automatically
- Payment Gateway: Square (PCI compliant)
- Accepted Cards: Visa, Mastercard, Amex, Discover

---

## 🏆 Membership/Subscription Setup

### A. Create Membership Plans in Square

**Using Square Subscriptions API:**

#### Bronze Membership — Monthly
- **Name:** "Bronze Monthly Membership"
- **Price:** $[TO BE SET]
- **Billing Cycle:** Monthly
- **Services Included:**
  - 1 service per month at 20% discount
  - Priority booking access
  - Email consultation support
- **Auto-Renewal:** Yes
- **Cancellation Policy:** Cancel anytime

#### Silver Membership — Monthly
- **Name:** "Silver Monthly Membership"
- **Price:** $[TO BE SET]
- **Billing Cycle:** Monthly
- **Services Included:**
  - 2 services per month at 25% discount
  - Priority booking (48-hour guarantee)
  - Monthly skin consultation
  - Access to exclusive member events
- **Auto-Renewal:** Yes
- **Cancellation Policy:** Cancel anytime

#### Gold Membership — Quarterly/Annual
- **Name:** "Gold Annual Membership"
- **Price:** $[TO BE SET]
- **Billing Cycle:** Quarterly or Annual
- **Services Included:**
  - 4 services per quarter (12 per year) at 30% discount
  - VIP booking priority
  - Quarterly personalized treatment plan
  - Complimentary add-on services
  - Loyalty rewards program
- **Auto-Renewal:** Yes
- **Cancellation Policy:** 30-day notice for annual plan

### B. Membership Page Layout

**Membership Page CTA Elements:**

```
[Membership Comparison Table]
├─ Bronze | Silver | Gold
├─ Price | Benefits | CTA Button
└─ "Subscribe Now" (links to payment)

[Member Benefits Section]
├─ Priority Booking
├─ Service Discounts
├─ Exclusive Events
├─ Concierge Support

[FAQ Section]
├─ How to Cancel
├─ Pausing Membership
├─ Transferring Credits
├─ Rewards Program Details
```

### C. Member Portal Access

**Square Customer Portal Features:**
- View upcoming appointments
- Cancel/reschedule appointments
- View purchase history
- Manage payment method
- View membership status
- Loyalty points balance

**Integration:** Provide login link on website (Members Only section)

---

## 👥 Customer Management

### A. Customer Database in Square

All customers automatically added with:
- Full name
- Email address
- Phone number
- Appointment history
- Purchase history
- Membership status
- Lifetime customer value

### B. Customer Segments (for marketing)

Create segments in Square for:
- **New Customers** (booked first appointment)
- **Active Members** (current membership)
- **Lapsed Members** (membership expired)
- **High-Value Customers** ($5,000+ lifetime)
- **Service-Specific** (e.g., "Laser Customers")

### C. Email Marketing Integration

- Export customer list to email platform (Mailchimp, Klaviyo, etc.)
- Send appointment reminders 48 hours before
- Send post-appointment follow-ups
- Send membership renewal reminders
- Send exclusive member offers

---

## 📊 Reporting & Analytics

### Square Dashboard Reports

1. **Revenue Dashboard**
   - Total revenue by month/quarter
   - Revenue by service category
   - Revenue by staff member
   - Membership revenue vs. one-time payments

2. **Appointment Analytics**
   - Total appointments booked
   - No-show rate
   - Average booking window (days in advance)
   - Busiest times/days

3. **Customer Analytics**
   - Total customers
   - Repeat customer rate
   - Customer lifetime value
   - Membership adoption rate

4. **Payment Analytics**
   - Payment success rate
   - Refunds/cancellations
   - Chargeback rate
   - Average transaction value

### Custom Reporting

- Export data to Google Sheets or Excel
- Create dashboard in Elementor (if desired)
- Monthly reconciliation with bank statements

---

## 🔒 Security & Compliance

### A. PCI Compliance

- **Square Payment Gateway:** PCI Level 1 certified
- **Never store full credit card numbers** on your website
- **Use Square's hosted payment forms** for checkout
- **Enable SSL certificate** on your domain

### B. Data Protection

- Enable **two-factor authentication** on Square account
- Restrict staff dashboard access by role
- Regular password updates required
- Enable API key rotation (quarterly minimum)

### C. Customer Privacy

- Comply with **GDPR/CCPA** data privacy laws
- Clear privacy policy on website
- Opt-in for email marketing (required)
- Allow customers to request/delete data

---

## 🚀 Implementation Timeline

### Phase 1: Setup (Week 1)
- [ ] Create Square merchant account
- [ ] Gather API credentials
- [ ] Set up location & staff in Square
- [ ] Create service catalog in Square

### Phase 2: Booking Integration (Week 2)
- [ ] Install Square Appointments widget in Elementor
- [ ] Configure appointment types (consultation, single session, package)
- [ ] Set up automated confirmations & reminders
- [ ] Test booking flow end-to-end

### Phase 3: Payment Setup (Week 3)
- [ ] Configure payment forms in Elementor
- [ ] Set up deposit/full payment options
- [ ] Test payment processing (test mode first)
- [ ] Configure payment receipts & invoicing

### Phase 4: Memberships (Week 4)
- [ ] Create membership plans in Square
- [ ] Build membership page in Elementor
- [ ] Set up recurring payment processing
- [ ] Configure member portal access

### Phase 5: Testing & Training (Week 5)
- [ ] Full end-to-end testing (booking → payment)
- [ ] Test cancellations & refunds
- [ ] Test membership renewals
- [ ] Train staff on Square Dashboard
- [ ] Test customer support workflows

### Phase 6: Launch (Week 6)
- [ ] Switch from test mode to live
- [ ] Monitor first week of transactions
- [ ] Gather customer feedback
- [ ] Make adjustments as needed

---

## 📱 Mobile Optimization

Square Appointments & Payment Forms are **fully responsive:**
- Mobile-optimized booking calendar
- One-click payment on mobile
- SMS appointment reminders
- Mobile-accessible member portal

**Test on:**
- iPhone (iOS 14+)
- Android devices
- Tablets

---

## 🆘 Troubleshooting & Support

### Common Issues

**Issue:** "Payment declined"
- Solution: Check card details, enable 3D Secure, contact customer

**Issue:** "Appointment not appearing on calendar"
- Solution: Verify staff assignment, check service duration, refresh browser

**Issue:** "Customer not receiving confirmation email"
- Solution: Check email settings in Square, verify email address, add to whitelist

### Support Resources

- **Square Help Center:** [help.squareup.com](https://help.squareup.com)
- **Square Developer Docs:** [developer.squareup.com](https://developer.squareup.com)
- **Elementor + Square Integration:** Contact Elementor support
- **ND Derma Med Spa Support:** [Contact form on website]

---

## 📞 Next Steps

1. **Set up Square account** (if not already done)
2. **Configure location, staff, and services** in Square Dashboard
3. **Test Square Appointments** widget in Elementor staging site
4. **Add service pricing** and membership rates
5. **Test full booking + payment flow**
6. **Train staff** on Square Dashboard
7. **Launch live** and monitor

---

**Questions?** Contact Square support or Elementor support for technical assistance.

**Last Updated:** March 24, 2026
**Next Review:** After first month of launch
