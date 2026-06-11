# ND Derma Med Spa — Membership Pricing & Configuration Template

**Status:** Ready for Pricing Configuration
**Last Updated:** March 24, 2026

---

## 💳 Membership Tier Configuration

Use this template to configure membership plans in **Square Subscriptions**.

---

## TIER 1: BRONZE MONTHLY

**Square Configuration:**
```
Plan Name:        Bronze Monthly Membership
Plan ID:          [AUTO-GENERATED]
Description:      Perfect for trying our signature treatments monthly
Price:            $[CLIENT TO SET]
Billing Cycle:    Monthly (every 30 days)
Auto-Renewal:     Enabled
Cancellation:     Cancel anytime (no penalty)
```

**Included Benefits:**
- ✓ 1 service per month at 20% discount
- ✓ Priority booking (standard)
- ✓ Email consultation support
- ✓ Member-only email updates

**Not Included:**
- ✗ Complimentary services
- ✗ VIP booking priority
- ✗ Loyalty rewards

**Member Signup Text:**
> "Try our most popular treatments monthly at a 20% discount. Perfect for maintaining results with regular facials, peels, or maintenance injectables."

---

## TIER 2: SILVER MONTHLY

**Square Configuration:**
```
Plan Name:        Silver Monthly Membership
Plan ID:          [AUTO-GENERATED]
Description:      For consistent aesthetic maintenance and skin health
Price:            $[CLIENT TO SET]
Billing Cycle:    Monthly (every 30 days)
Auto-Renewal:     Enabled
Cancellation:     Cancel anytime (no penalty)
```

**Included Benefits:**
- ✓ 2 services per month at 25% discount
- ✓ Priority booking (48-hour guarantee)
- ✓ Monthly personalized skin consultation
- ✓ Access to exclusive member events
- ✓ Member-only email updates

**Not Included:**
- ✗ Complimentary services
- ✗ VIP booking (upgraded from standard)
- ✗ Annual loyalty rewards

**Member Signup Text:**
> "Ideal for committed skin care and body transformation. Double your monthly treatments at 25% off while receiving expert guidance on your personalized protocol."

---

## TIER 3: GOLD ANNUAL

**Square Configuration:**
```
Plan Name:        Gold Annual Membership
Plan ID:          [AUTO-GENERATED]
Description:      The ultimate luxury membership for serious aesthetic commitment
Price:            $[CLIENT TO SET]
Billing Cycle:    Annual (every 365 days)
Auto-Renewal:     Enabled
Cancellation:     30-day notice required (prorated refund available)
```

**Included Benefits:**
- ✓ 12 services per year (4 per quarter) at 30% discount
- ✓ VIP booking priority (72-hour hold)
- ✓ Quarterly personalized treatment plan review
- ✓ 2 complimentary add-on services per year (valued up to $200)
- ✓ Access to all exclusive member events
- ✓ Member-only email updates
- ✓ Loyalty rewards program (1 point per $1 spent)
- ✓ Concierge appointment scheduling

**Not Included:**
- ✗ Complimentary advanced treatments (Ultraformer, Morpheus8)
- ✗ Price reductions beyond membership discount

**Member Signup Text:**
> "For the dedicated. Commit to 12 treatments yearly at 30% off, gain VIP access, and receive complimentary services + quarterly expert reviews. Build your aesthetic transformation journey with us."

---

## TIER 3B: GOLD QUARTERLY (Alternative)

**Optional 3-month commitment option:**

```
Plan Name:        Gold Quarterly Membership
Plan ID:          [AUTO-GENERATED]
Description:      Try the Gold experience quarterly
Price:            $[CLIENT TO SET] (roughly 1/4 of annual)
Billing Cycle:    Quarterly (every 90 days)
Auto-Renewal:     Enabled
Cancellation:     Cancel anytime (no penalty)
```

**Included Benefits:**
- ✓ 4 services per quarter at 30% discount
- ✓ VIP booking priority (72-hour hold)
- ✓ Quarterly personalized treatment plan review
- ✓ 1 complimentary add-on service per quarter
- ✓ Access to exclusive member events
- ✓ Member-only email updates

---

## 📊 Pricing Strategy Recommendations

### Discount Structure

**Service Baseline Pricing Strategy:**

```
Service Average Price:        $[BASE]

Discount Tiers:
├─ Bronze (20% off):          $[BASE × 0.80]
├─ Silver (25% off):          $[BASE × 0.75]
└─ Gold (30% off):            $[BASE × 0.70]
```

### Membership ROI Calculation

**Example for Silver Member (25% discount):**
- Service average price: $200
- 2 services per month = $400 revenue
- 25% discount = saves member $100/month
- Membership price should be: ~$150-180/month
- Clinic retains: $220-250 monthly revenue (vs. $400 without discount)
- **Break-even:** ~2.5 services per month

**Example for Gold Member (30% discount):**
- 12 services per year @ $200 avg = $2,400 retail
- 30% discount = saves member $720/year
- Annual price should be: ~$1,800-2,000
- Clinic retains: $1,680-1,800 yearly
- Plus add-on services (complimentary) drive upsells
- **Break-even:** ~6 services per year (half of included)

---

## 🎯 Pricing Best Practices

### What to Consider

1. **Your Service Costs:**
   - Staff labor
   - Product/equipment costs
   - Facility overhead
   - Technology (Square, booking system)

2. **Market Comparison:**
   - Competitor med-spas in your area
   - Premium brands (typically 20-30% discounts for members)
   - Industry benchmarks

3. **Customer Lifetime Value:**
   - Members spend 2-4x more over time
   - Membership creates loyalty
   - Higher customer retention rates

4. **Unit Economics:**
   - Target: 70-80% gross margin on member services
   - Membership fees should cover overhead
   - Discounts absorbed by volume

### Pricing Formula

```
Monthly Membership Price = 
  (Average Service Price × Services Included × Discount Absorption) 
  - (Variable Costs × Services Included)
  + (Fixed Overhead Allocation)
```

**Example Calculation:**

```
Service Average:          $200
Silver Services/Month:    2
Discount (25%):           0.75x
Variable Cost/Service:    $60

= ($200 × 2 × 0.75) - ($60 × 2) + (Overhead Allocation)
= $300 - $120 + $X
= $180-220 suggested price range
```

---

## 🔄 Membership Lifecycle & Operations

### Signup Process

1. Member selects tier on website
2. Square collects payment info
3. First charge processed immediately
4. Confirmation email sent
5. Member portal access granted
6. Welcome package sent (email + instructions)

### Recurring Billing Dates

**Bronze & Silver:** Same date each month (automatic)
**Gold Annual:** Automatic anniversary date
**Gold Quarterly:** Every 3 months from signup date

### Cancellation & Pausing

**Cancelation Options:**
- Full cancellation (can rejoin later)
- Pause membership (freeze for 1 month, no charge)
- Downgrade tier (Silver → Bronze, etc.)

**Refund Policy:**
- Monthly plans: Cancel anytime
- Annual plans: 30-day notice, prorated refund available
- Unused services: Not refundable (membership is ongoing access)

### Member Communication Timeline

| Timing | Action |
|--------|--------|
| Day 0 | Signup confirmation + member portal access |
| Day 7 | "Welcome, let's book your first appointment" |
| Day 21 | Remind about complimentary consultation |
| Day 28 | "You have 2 days left in billing cycle" |
| Day 30 | Renewal notification + next bill amount |
| Day 45 | Exclusive member offer (bonus points, special service) |

---

## 🎁 Add-On Services & Upsells

**Complimentary Add-Ons (included in Gold):**
- Lip hydration enhancement ($100 value)
- Dermaplaning add-on ($50 value)
- Smart Microcurrent treatment ($75 value)
- Premium serum upgrade (during facial)

**Recommended Upsells for Members:**
- Pre-treatment packages (prep for major service)
- Post-treatment care products
- Gift memberships (referral bonus)
- Seasonal specials (+ treatments beyond allocation)

**Loyalty Rewards Program:**
- 1 point per $1 spent
- 50 points = $25 off service
- Annual bonus (100 points for Gold members)

---

## 📱 Member Portal Features

**In Square Customer Portal:**
- [ ] View membership details (start date, renewal date)
- [ ] See complimentary services remaining
- [ ] Book appointments
- [ ] View appointment history
- [ ] See purchase history
- [ ] Manage payment method
- [ ] View loyalty points balance
- [ ] Access to exclusive member offers

**Custom Website Member Page:**
- [ ] Login area (linked to Square portal)
- [ ] Member-only content (guides, tips, testimonials)
- [ ] Exclusive event calendar
- [ ] Referral program information
- [ ] Contact concierge button

---

## ⚙️ Configuration Checklist

Before launching memberships, complete:

- [ ] Finalize pricing for all 3 tiers
- [ ] Set discount percentages in Square
- [ ] Create membership service items in Square
- [ ] Configure auto-renewal settings
- [ ] Set billing cycle dates
- [ ] Create email templates for confirmations
- [ ] Build membership page in Elementor
- [ ] Create membership comparison table
- [ ] Test signup flow (test mode)
- [ ] Test cancellation process
- [ ] Train staff on membership management
- [ ] Create member onboarding email series
- [ ] Set up loyalty rewards in Square (if using)

---

## 🎯 Membership Marketing

### Website Copy Examples

**Bronze Tier:**
> "Start your transformation with a monthly beauty investment. Try our signature treatments at 20% off while building your ideal routine."

**Silver Tier:**
> "Double down on results. Two treatments monthly, prioritized booking, and expert guidance make this our most popular choice."

**Gold Tier:**
> "The VIP experience. Commit to your transformation with four quarterly treatments, complimentary services, and white-glove concierge scheduling."

### Email Campaign Ideas

1. **Launch Announcement** — "Introducing Membership Benefits"
2. **Social Proof** — "Member Transformation Stories"
3. **Limited-Time Offer** — "First 50 Members Get 10% Extra Off"
4. **Referral Program** — "Get $50 Credit for Each Friend Who Joins"
5. **Seasonal Upsell** — "Gift a Membership This Holiday"

---

## 📊 Success Metrics

Track these KPIs monthly:

- **Member Acquisition Rate:** New memberships/month
- **Member Retention Rate:** % active vs. cancelled
- **Average Member Lifetime Value:** Total revenue per member
- **Service Booking Rate:** How often members book
- **Revenue Comparison:** Member vs. non-member revenue
- **Churn Rate:** % memberships cancelled monthly
- **Customer Satisfaction:** NPS from member feedback

**Target Goals (Year 1):**
- 50+ active members by end of year
- 80%+ retention rate
- $150+ average member LTV
- 2+ services booked per member per month

---

**Ready to configure?** Use the Square Configuration section above and update pricing based on your service costs and market research.

**Last Updated:** March 24, 2026
