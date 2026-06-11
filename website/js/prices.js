/* ═══════════════════════════════════════════════════════════════
   ND DERMA MED SPA — Price Configuration
   ────────────────────────────────────────────────────────────────
   THIS IS THE SINGLE SOURCE OF TRUTH FOR ALL PRICES.
   Edit prices here — they automatically update across:
     • services.html  (service price display)
     • memberships.html  (membership plan prices)
     • index.html  (package starting prices)

   Format:  'Exact Service Name': price_in_USD (number, no $ sign)
   ═══════════════════════════════════════════════════════════════ */

const ND_PRICES = {

  /* ── MEMBERSHIP PLANS ─────────────────────────────────────── */
  memberships: {
    bronze: { price: 79,   period: 'month' },
    silver: { price: 149,  period: 'month' },
    gold:   { price: 1299, period: 'year'  }
  },

  /* ── SERVICES ─────────────────────────────────────────────── */
  services: {

    /* Category 1 — Advanced Laser & Energy Devices */
    laser: {
      'Laser Skin Rejuvenation':           450,
      'Laser for Pigmentation':            350,
      'Laser for Acne & Acne Scars':       600,
      'Laser Hair Removal':                120,
      'Ultraformer Full Face Lift (HIFU)': 800,
      'Ultraformer Face + Neck':           1000,
      'Ultraformer Double Chin':           250,
      'Ultraformer Body Tightening':       1000,
      'Morpheus8 Face (RF Microneedling)': 550,
      'Morpheus8 Neck':                    250,
      'Morpheus8 Body':                    600
    },

    /* Category 2 — Facial Treatments */
    facials: {
      'Hydrafacial / Deep Hydration':               250,
      'Chemical Peels':                             350,
      'Microneedling':                              200,
      'Microneedling + Exosomes':                   300,
      'Glass Skin Facial':                          175,
      'Acne Control Facial':                        240,
      'Anti-Aging Facial':                          200,
      'Dermaplaning':                                80,
      'Hydra Lips':                                 100,
      'Smart Microcurrent (Face Lifting & Toning)': 130,
      'Lash Lift & Tint':                           100,
      'Brows Design + Lamination & Tint':           120,
      'Brows Wax + Tint':                            50
    },

    /* Category 3 — Injectables */
    injectables: {
      'Botox — Full Face':               600,
      'Botox — Forehead Lines':          450,
      'Botox — Frown Lines':             450,
      'Botox — Crow\'s Feet':            300,
      'Botox — Lip Flip':                 80,
      'Botox — Masseter / Jaw Slimming': 200,
      'Lip Enhancement':                 500,
      'Jawline Contouring':              400,
      'Chin Projection':                 400,
      'Cheek Volume':                    400,
      'Under Eye (Tear Trough)':         400,
      'Nasolabial Folds':                350,
      'Facial Balance Reset (Hyaluronidase)': 350
    },

    /* Category 4 — Thread Lift */
    threadlift: {
      'Fox Eyes Signature Lift': 750,
      'Jawline Thread Lift':     1100,
      'Midface Lift':            1400,
      'Neck Thread Lift':        1200,
      'Full Face Thread Lift':   1800
    },

    /* Category 5 — Collagen Biostimulators */
    collagen: {
      'Sculptra':                                    650,
      'Radiesse':                                    700,
      'Hyperdilute Radiesse':                        800,
      'Full Face Collagen Therapy':                  1200,
      'Neck Collagen Renewal':                       1200,
      'Non-Surgical Butt Augmentation — Sculptra':   5600,
      'Non-Surgical Butt Augmentation — Radiesse':   6100
    },

    /* Category 6 — Hair Restoration & Scalp Treatments */
    hair: {
      'Hair Loss Treatment':             250,
      'Scalp Microneedling':             200,
      'Exosomes for Hair Restoration':   350,
      'Growth Factor Therapy':           400,
      'Hair Regeneration Therapy':       500,
      'Head Spa':                        200
    },

    /* Category 7 — Body Treatments */
    body: {
      'Radiofrequency Skin Tightening':         80,
      'Radiofrequency Body Tightening':        150,
      'Ultrasound Fat Reduction':              150,
      'Body Sculpting':                        300,
      'Cellulite Reduction':                   250,
      'Skin Tag Removal':                      100,
      'EMS Muscle Stimulation':                200,
      'Spray Tanning (Machine-Based Bronzing)':  59
    },

    /* Category 8 — Vitamin & Wellness Therapy */
    wellness: {
      'Vitamin Injections':             75,
      'IV Therapy':                    150,
      'Anti-Aging Vitamin Protocol':   150,
      'Fat Burning Boosters':          250
    }
  },

  /* ── HOMEPAGE PACKAGES (starting prices) ─────────────────── */
  packages: {
    fullFaceRejuvenation: 450,   // Full Face Rejuvenation starting price
    hairGrowthProgram:    200,   // Hair Growth Program starting price
    bodyContouringProgram: 150   // Body Contouring Program starting price
  }

};
