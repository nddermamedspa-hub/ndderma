# Booking Page — ND Derma Med Spa

**Referenced in:** [claude.md](./claude.md)

---

## BOOKING PAGE HERO

**Headline:** Book Your Appointment

**Subheadline:**
> Select your desired service and request your appointment in just a few steps.

**Layout:** Centered text over premium background

---

## BOOKING FLOW — 6-STEP PROCESS

### STEP 1 — CHOOSE A CATEGORY

**Instruction Text:** Select the treatment category that interests you.

**Category Options:**
- 🔴 **Laser & Energy Devices**
- ✨ **Facial Treatments**
- 💉 **Injectables**
- 🧬 **Hair Restoration**
- ⚡ **Body Treatments**
- 💊 **Vitamin & Wellness**

**Element Type:** Radio buttons or clickable cards (visual selection preferred for UX)

**Next Button:** "Continue to Services"

---

### STEP 2 — CHOOSE A SERVICE

**Instruction Text:** Select your specific treatment.

**Dynamic Content:** Service list populates based on Category selection from Step 1.

**Example - If "Laser & Energy Devices" selected:**
- Laser Skin Rejuvenation
- Laser for Pigmentation
- Laser for Acne & Acne Scars
- Laser Hair Removal
- Ultraformer Full Face Lift
- Ultraformer Face + Neck
- Ultraformer Double Chin
- Ultraformer Body Tightening
- Morpheus8 Face
- Morpheus8 Neck
- Morpheus8 Body
- Morpheus8 Acne Scars

**Element Type:** Dropdown menu or scrollable list

**Next Button:** "Continue to Appointment Type"

---

### STEP 3 — CHOOSE APPOINTMENT TYPE

**Instruction Text:** What type of appointment are you looking for?

**Appointment Type Options:**
- 📋 **Consultation** — Initial consultation to discuss goals and treatment options
- 🏥 **Single Session** — One-time treatment
- 📦 **Package Inquiry** — Interest in a curated package or program
- ↩️ **Follow-Up Appointment** — Return visit or treatment continuation

**Element Type:** Radio buttons or clickable cards

**Next Button:** "Continue to Date & Time"

---

### STEP 4 — CHOOSE PREFERRED DATE & TIME

**Instruction Text:** Select your preferred appointment date and time.

**Elements:**
- **Calendar Picker:** Display 30-60 days of available dates
- **Time Slots:** Show available times based on selected date
  - Format: 9:00 AM, 9:30 AM, 10:00 AM, etc. (15-30 min increments)
  - Gray out unavailable slots

**Availability Note:**
> Our team schedules appointments based on your preferred time. If your requested time isn't available, we'll contact you with alternative options.

**Next Button:** "Continue to Your Information"

---

### STEP 5 — CLIENT INFORMATION FORM

**Instruction Text:** Please provide your contact and treatment information.

**Form Fields:**

| Field | Type | Required |
|-------|------|----------|
| Full Name | Text Input | Yes |
| Phone Number | Phone Input | Yes |
| Email Address | Email Input | Yes |
| Preferred Contact Method | Dropdown (Phone / Email) | Yes |
| Main Concern / Goal | Text Area | Yes |
| Notes (Additional Information) | Text Area | No |

**Optional Additional Fields (to consider):**
- Have you had this treatment before? (Yes/No)
- Are you a new or returning client? (New/Returning)
- Referral source (How did you hear about us?) (Dropdown)

**Privacy Notice:**
> Your information is secure and will only be used to confirm your appointment. See our Privacy Policy.

**Next Button:** "Review & Confirm"

---

### STEP 6 — CONFIRMATION

**Confirmation Message (On-Screen):**

> **Thank you for choosing ND Derma Med Spa!**
> Your appointment request has been received. Our team will confirm your booking shortly.

**Email Confirmation:**

Subject: Appointment Request Confirmation — ND Derma Med Spa

Body (Example):
```
Hello [Client Name],

Thank you for scheduling with ND Derma Med Spa!

📅 Appointment Details:
Service: [Service Selected]
Appointment Type: [Consultation/Single Session/etc.]
Preferred Date: [Date Selected]
Preferred Time: [Time Selected]

We will contact you within 24 hours to confirm your appointment or suggest alternative times if needed.

Contact: [Phone] | [Email]

Best regards,
ND Derma Med Spa Team
Where elegance meets aesthetics.
```

**Next Steps:**
- Display booking confirmation number
- Offer downloadable confirmation PDF
- Provide phone number and email for questions
- Link to FAQ or policies page

---

## BOOKING CTA BOX (Sidebar or Below Form)

**Headline:** Need Help Choosing a Service?

**Copy:**
> Start with a consultation and let our team guide you to the best protocol for your goals.

**Button:**
- **Text:** Book a Free Consultation
- **Action:** Pre-select "Consultation" in Step 3

---

## 📱 RESPONSIVE DESIGN NOTES

- **Desktop:** Side-by-side layout (form left, info box right)
- **Tablet:** Stacked layout, form full-width
- **Mobile:** Full-width form, info box below, mobile-optimized inputs

---

## 🔧 TECHNICAL INTEGRATION

**Backend Integration Required:**
- Calendar system (integration with scheduling software: Calendly, Acuity, Vagaro, etc.)
- Email confirmation system
- Client data storage (CRM/Database)
- Admin notification on new bookings

**Third-Party Services (Optional):**
- Calendly, Acuity Scheduling, or Vagaro for appointment management
- Formspree, Gravity Forms, or native solution for form handling

**Form Validation:**
- All required fields must be filled
- Email format validation
- Phone number format validation (optional country selection)
- Date must be in future

---

## 📋 BOOKING POLICIES (Link at Footer)

Create separate page with:
- Cancellation Policy
- Rescheduling Policy
- Late Arrival Policy
- Payment Terms (if applicable)
- Consultation Fees (if applicable)
- Age/Consent Requirements

---

## ⏱️ BOOKING FLOW DIAGRAM

```
START
  ↓
Step 1: Select Category
  ↓
Step 2: Select Service (dynamic list)
  ↓
Step 3: Select Appointment Type
  ↓
Step 4: Select Date & Time
  ↓
Step 5: Enter Client Information
  ↓
Step 6: Confirmation
  ↓
Email Sent + On-Screen Message
  ↓
END (Await Admin Confirmation)
```

---

## 💬 FAQ - BOOKING HELP

Consider adding collapsible FAQ section on page:

**Q: How long does each appointment take?**
A: Treatment duration varies by service. Our team will discuss expected appointment length during your consultation confirmation.

**Q: What if my preferred time isn't available?**
A: We'll contact you with alternative options within 24 hours of your booking request.

**Q: Can I reschedule or cancel my appointment?**
A: Yes, with [X] hours notice. See our Cancellation Policy.

**Q: Do I need to prepare anything for my appointment?**
A: Preparation varies by treatment. We'll send pre-appointment care instructions via email.

**Q: What should I expect during a consultation?**
A: Your consultant will discuss your goals, assess your needs, and create a personalized treatment plan. No commitment required.

---

**Referenced in:** [claude.md](./claude.md)
**Previous:** [02-services.md](./02-services.md)
**Next:** [04-service-descriptions.md](./04-service-descriptions.md)
