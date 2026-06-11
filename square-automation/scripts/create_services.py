#!/usr/bin/env python3
"""
Create Square Services Catalog
Creates all 45+ aesthetic services from ND Derma Med Spa documentation
"""

import os
import sys
import csv
import json
import uuid
from pathlib import Path
from dotenv import load_dotenv
from square import Square

# Load environment variables
load_dotenv()

# ── Load prices from prices.json (single source of truth) ────────────────────
_PRICES_FILE = Path(__file__).parent.parent / 'prices.json'

def _load_prices():
    """Return a flat dict: service_name → {price, duration} from prices.json."""
    if _PRICES_FILE.exists():
        with open(_PRICES_FILE, 'r') as f:
            data = json.load(f)
        flat = {}
        for category_services in data.get('services', {}).values():
            for name, info in category_services.items():
                flat[name] = info
        return flat
    return {}

_PRICE_OVERRIDES = _load_prices()

def _price(service_name, default_price, default_duration):
    """Return (price, duration) from prices.json override, or fall back to defaults."""
    override = _PRICE_OVERRIDES.get(service_name)
    if override:
        return float(override.get('price', default_price)), int(override.get('duration', default_duration))
    return default_price, default_duration

# Service catalog — descriptions stay here; prices/durations come from prices.json
_RAW_SERVICES = [
    # Advanced Laser & Energy Devices (12 services)
    {"name": "Laser Skin Rejuvenation", "description": "Refine, renew, and restore your skin with advanced laser technology designed to improve tone, texture, and radiance.", "duration": 60, "price": 200.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Laser for Pigmentation", "description": "Target dark spots, melasma, and sun damage with precision-based laser technology.", "duration": 45, "price": 175.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Laser for Acne & Acne Scars", "description": "A results-driven solution to reduce active acne, calm inflammation, and soften the appearance of scars.", "duration": 60, "price": 200.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Laser Hair Removal", "description": "Experience long-term hair reduction with advanced laser systems designed for comfort and efficiency.", "duration": 45, "price": 150.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Ultraformer Full Face Lift", "description": "A non-invasive lifting treatment that reaches deep structural layers of the skin.", "duration": 60, "price": 350.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Ultraformer Face + Neck", "description": "Extended HIFU treatment for full facial and neck rejuvenation.", "duration": 75, "price": 400.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Ultraformer Double Chin", "description": "Targeted HIFU for jawline definition and double chin reduction.", "duration": 45, "price": 250.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Ultraformer Body Tightening", "description": "Non-invasive body contouring and skin tightening with HIFU technology.", "duration": 60, "price": 300.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Morpheus8 Face", "description": "Powerful RF microneedling that remodels collagen and tightens skin for refined appearance.", "duration": 60, "price": 350.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Morpheus8 Neck", "description": "RF microneedling treatment specifically designed for neck tightening and rejuvenation.", "duration": 45, "price": 250.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Morpheus8 Body", "description": "Full body RF microneedling for texture improvement and tightening.", "duration": 75, "price": 400.00, "category": "Advanced Laser & Energy Devices"},
    {"name": "Morpheus8 Acne Scars", "description": "Specialized treatment for acne scar improvement through RF microneedling.", "duration": 60, "price": 300.00, "category": "Advanced Laser & Energy Devices"},

    # Facial Treatments (12 services)
    {"name": "Hydrafacial / Deep Hydration", "description": "Multi-step facial with deep cleansing, exfoliation, and intense hydration infusion.", "duration": 45, "price": 150.00, "category": "Facial Treatments"},
    {"name": "Chemical Peels", "description": "Advanced exfoliation treatments designed to improve skin texture and reveal brighter complexion.", "duration": 45, "price": 125.00, "category": "Facial Treatments"},
    {"name": "Microneedling", "description": "Stimulates natural collagen production to improve skin firmness, texture, and quality.", "duration": 60, "price": 200.00, "category": "Facial Treatments"},
    {"name": "Microneedling + Exosomes", "description": "Next-level regenerative treatment that accelerates healing and enhances results.", "duration": 60, "price": 300.00, "category": "Facial Treatments"},
    {"name": "Glass Skin Facial", "description": "Signature treatment focused on hydration, smoothness, and luminous glow.", "duration": 60, "price": 175.00, "category": "Facial Treatments"},
    {"name": "Acne Control Facial", "description": "Specialized treatment targeting active acne, inflammation, and breakouts.", "duration": 50, "price": 125.00, "category": "Facial Treatments"},
    {"name": "Anti-Aging Facial", "description": "Comprehensive anti-aging protocol with targeted treatments for fine lines and wrinkles.", "duration": 75, "price": 200.00, "category": "Facial Treatments"},
    {"name": "Dermaplaning", "description": "Gentle exfoliation that removes dead skin cells and fine hair for instant smoothness.", "duration": 30, "price": 75.00, "category": "Facial Treatments"},
    {"name": "Hydra Lips", "description": "Targeted lip treatment that hydrates, smooths, and enhances lip texture and fullness.", "duration": 30, "price": 100.00, "category": "Facial Treatments"},
    {"name": "Smart Microcurrent", "description": "Non-invasive lifting treatment that tones facial muscles and delivers instant tightening effect.", "duration": 45, "price": 150.00, "category": "Facial Treatments"},
    {"name": "Lash Lift", "description": "Enhance your natural lashes with lifted, longer, and more defined appearance.", "duration": 45, "price": 75.00, "category": "Facial Treatments"},
    {"name": "Brows Tint", "description": "Define and enhance your brows with customized tinting for fuller look.", "duration": 30, "price": 50.00, "category": "Facial Treatments"},

    # Injectables (6 services)
    {"name": "Full Face Botox", "description": "Smooth fine lines and prevent deeper wrinkles while maintaining natural expression.", "duration": 30, "price": 200.00, "category": "Injectables"},
    {"name": "Forehead Lines", "description": "Target forehead wrinkles with precision Botox injection.", "duration": 20, "price": 100.00, "category": "Injectables"},
    {"name": "Frown Lines", "description": "Smooth frown lines between eyebrows for refreshed appearance.", "duration": 20, "price": 100.00, "category": "Injectables"},
    {"name": "Crow's Feet", "description": "Address fine lines around eyes for brighter, more youthful look.", "duration": 20, "price": 100.00, "category": "Injectables"},
    {"name": "Lip Enhancement", "description": "Create balanced, soft, naturally enhanced lips tailored to your facial harmony.", "duration": 30, "price": 250.00, "category": "Injectables"},
    {"name": "Jawline Contouring", "description": "Define and sculpt the jawline for more structured and elegant facial profile.", "duration": 30, "price": 300.00, "category": "Injectables"},

    # Hair Restoration & Scalp Treatments (5 services)
    {"name": "Hair Loss Treatment", "description": "Personalized approach to reduce hair thinning and support stronger, healthier hair growth.", "duration": 60, "price": 250.00, "category": "Hair Restoration"},
    {"name": "Scalp Microneedling", "description": "Stimulates the scalp and improves circulation, enhancing hair growth potential.", "duration": 45, "price": 150.00, "category": "Hair Restoration"},
    {"name": "Exosomes for Hair Restoration", "description": "Regenerative treatment that supports follicle health and promotes visible hair density.", "duration": 60, "price": 400.00, "category": "Hair Restoration"},
    {"name": "Growth Factor Therapy", "description": "Advanced bio-stimulation designed to reactivate hair follicles and improve scalp health.", "duration": 60, "price": 350.00, "category": "Hair Restoration"},
    {"name": "Hair Regeneration Therapy", "description": "Comprehensive protocol combining multiple technologies for maximum hair restoration.", "duration": 90, "price": 500.00, "category": "Hair Restoration"},

    # Body Treatments (6 services)
    {"name": "Radiofrequency Skin Tightening", "description": "Improves skin laxity and firmness by stimulating collagen production.", "duration": 60, "price": 300.00, "category": "Body Treatments"},
    {"name": "Ultrasound Fat Reduction", "description": "Targets localized fat deposits using advanced technology to contour and refine body shape.", "duration": 60, "price": 350.00, "category": "Body Treatments"},
    {"name": "Body Sculpting", "description": "Non-invasive solution to shape, tone, and enhance body contours.", "duration": 60, "price": 300.00, "category": "Body Treatments"},
    {"name": "Cellulite Reduction", "description": "Improves the appearance of cellulite by smoothing and firming the skin.", "duration": 60, "price": 250.00, "category": "Body Treatments"},
    {"name": "EMS Muscle Stimulation", "description": "Enhances muscle tone and definition through advanced stimulation technology.", "duration": 45, "price": 200.00, "category": "Body Treatments"},
    {"name": "Spray Tanning (Machine-Based Bronzing)", "description": "Achieve a flawless, sun-kissed glow with an even, natural-looking finish.", "duration": 30, "price": 75.00, "category": "Body Treatments"},

    # Vitamin & Wellness Therapy (4 services)
    {"name": "Vitamin Injections", "description": "Targeted nutrient support to enhance energy, metabolism, and overall vitality.", "duration": 15, "price": 75.00, "category": "Vitamin & Wellness"},
    {"name": "IV Therapy", "description": "Powerful infusion of vitamins and antioxidants for hydration, immunity, and glow.", "duration": 45, "price": 150.00, "category": "Vitamin & Wellness"},
    {"name": "Anti-Aging Vitamin Protocol", "description": "Support skin health and longevity from within with advanced nutrient combinations.", "duration": 30, "price": 125.00, "category": "Vitamin & Wellness"},
    {"name": "Fat Burning Boosters", "description": "Optimize metabolism and support body composition with targeted injectable support.", "duration": 20, "price": 100.00, "category": "Vitamin & Wellness"},
]

# Apply prices.json overrides
SERVICES = []
for s in _RAW_SERVICES:
    price, duration = _price(s['name'], s['price'], s['duration'])
    SERVICES.append({**s, 'price': price, 'duration': duration})

def create_services():
    """Create all services in Square"""

    print("\n" + "="*70)
    print("CREATING SQUARE SERVICES CATALOG")
    print("="*70 + "\n")

    # Get credentials
    access_token = os.getenv('SQUARE_ACCESS_TOKEN')
    location_id = os.getenv('SQUARE_LOCATION_ID')
    environment = os.getenv('SQUARE_ENVIRONMENT', 'production')

    if not access_token or not location_id:
        print("❌ ERROR: Missing Square credentials in .env")
        return False

    try:
        client = Square(token=access_token)

        created_services = []
        skipped = 0
        failed = 0

        print(f"Creating {len(SERVICES)} services...\n")

        for i, service in enumerate(SERVICES, 1):
            try:
                item_id = "#" + service['name'].replace(' ', '_').replace("'", "").lower()[:50]
                result = client.catalog.object.upsert(
                    idempotency_key=str(uuid.uuid4()),
                    object={
                        "type": "ITEM",
                        "id": item_id,
                        "present_at_all_locations": True,
                        "item_data": {
                            "name": service['name'],
                            "description": service['description'],
                            "product_type": "APPOINTMENTS_SERVICE",
                            "variations": [
                                {
                                    "type": "ITEM_VARIATION",
                                    "id": "#Standard",
                                    "present_at_all_locations": True,
                                    "item_variation_data": {
                                        "item_id": item_id,
                                        "name": "Standard",
                                        "pricing_type": "FIXED_PRICING",
                                        "price_money": {
                                            "amount": int(service['price'] * 100),
                                            "currency": "USD"
                                        },
                                        "service_duration": service['duration'] * 60000,
                                        "available_for_booking": True,
                                    }
                                }
                            ]
                        }
                    }
                )

                if result.errors:
                    print(f"⚠ [{i:2d}/{len(SERVICES)}] {service['name']:40s} - {result.errors}")
                    skipped += 1
                else:
                    print(f"✓ [{i:2d}/{len(SERVICES)}] {service['name']:40s} ({service['duration']} min, ${service['price']:7.2f})")
                    created_services.append({
                        'name': service['name'],
                        'duration': service['duration'],
                        'price': service['price'],
                        'category': service['category']
                    })

            except Exception as e:
                print(f"❌ [{i:2d}/{len(SERVICES)}] {service['name']:40s} - Error: {str(e)}")
                failed += 1

        # Save to CSV
        print("\n" + "="*70)
        csv_filename = "services_created.csv"
        with open(csv_filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'duration', 'price', 'category'])
            writer.writeheader()
            writer.writerows(created_services)

        print(f"✅ Services Created: {len(created_services)}")
        print(f"⚠  Skipped/Failed: {skipped + failed}")
        print(f"📊 Total: {len(SERVICES)}")
        print(f"\n📁 Saved to: {csv_filename}\n")

        return True

    except Exception as e:
        print(f"❌ Error creating services: {str(e)}")
        return False

if __name__ == "__main__":
    success = create_services()
    sys.exit(0 if success else 1)
