/* ═══════════════════════════════════════════════════════════════
   ND DERMA MED SPA — Main JavaScript
   Set window.ND_SQUARE_BOOKING_URL (see booking.html) for live Square Appointments.
   ═══════════════════════════════════════════════════════════════ */

'use strict';

/* ─── SERVICES DATA ─────────────────────────────────────────── */
const SERVICES_DATA = {
  laser: {
    label: 'Laser & Energy Devices',
    services: [
      'Laser Skin Rejuvenation',
      'Laser for Pigmentation',
      'Laser for Acne & Acne Scars',
      'Laser Hair Removal',
      'Ultraformer Full Face Lift (HIFU)',
      'Ultraformer Face + Neck',
      'Ultraformer Double Chin',
      'Ultraformer Body Tightening',
      'Morpheus8 Face (RF Microneedling)',
      'Morpheus8 Neck',
      'Morpheus8 Body',
      'Morpheus8 Acne Scars'
    ]
  },
  facials: {
    label: 'Facial Treatments',
    services: [
      'Hydrafacial / Deep Hydration',
      'Chemical Peels',
      'Microneedling',
      'Microneedling + Exosomes',
      'Glass Skin Facial',
      'Acne Control Facial',
      'Anti-Aging Facial',
      'Dermaplaning',
      'Hydra Lips',
      'Smart Microcurrent (Face Lifting & Toning)',
      'Lash Lift',
      'Brows Tint'
    ]
  },
  injectables: {
    label: 'Injectables',
    services: [
      'Botox — Full Face',
      'Botox — Forehead Lines',
      'Botox — Frown Lines',
      'Botox — Crow\'s Feet',
      'Botox — Lip Flip',
      'Botox — Masseter / Jaw Slimming',
      'Lip Enhancement',
      'Jawline Contouring',
      'Chin Projection',
      'Cheek Volume',
      'Under Eye (Tear Trough)',
      'Nasolabial Folds'
    ]
  },
  hair: {
    label: 'Hair Restoration & Scalp Treatments',
    services: [
      'Hair Loss Treatment',
      'Scalp Microneedling',
      'Exosomes for Hair Restoration',
      'Growth Factor Therapy',
      'Hair Regeneration Therapy'
    ]
  },
  body: {
    label: 'Body Treatments',
    services: [
      'Radiofrequency Skin Tightening',
      'Ultrasound Fat Reduction',
      'Body Sculpting',
      'Cellulite Reduction',
      'EMS Muscle Stimulation',
      'Spray Tanning (Machine-Based Bronzing)'
    ]
  },
  wellness: {
    label: 'Vitamin & Wellness Therapy',
    services: [
      'Vitamin Injections',
      'IV Therapy',
      'Anti-Aging Vitamin Protocol',
      'Fat Burning Boosters'
    ]
  }
};

/* ─── MOBILE NAV ─────────────────────────────────────────────── */
const MobileNav = {
  hamburger: null,
  nav: null,

  init() {
    this.hamburger = document.querySelector('.hamburger');
    this.nav = document.getElementById('mobile-nav');
    if (!this.hamburger || !this.nav) return;

    this.hamburger.addEventListener('click', () => this.toggle());
    this.nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => this.close());
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.close();
    });
  },

  toggle() {
    const isOpen = this.nav.classList.contains('open');
    if (isOpen) this.close();
    else this.open();
  },

  open() {
    this.nav.classList.add('open');
    this.hamburger.classList.add('open');
    document.body.classList.add('nav-open');
    this.hamburger.setAttribute('aria-expanded', 'true');
    this.nav.setAttribute('aria-hidden', 'false');
  },

  close() {
    this.nav.classList.remove('open');
    this.hamburger.classList.remove('open');
    document.body.classList.remove('nav-open');
    this.hamburger.setAttribute('aria-expanded', 'false');
    this.nav.setAttribute('aria-hidden', 'true');
  }
};

/* ─── STICKY HEADER ──────────────────────────────────────────── */
const StickyHeader = {
  header: null,
  heroDark: null,
  threshold: 60,

  init() {
    this.header = document.getElementById('site-header');
    this.heroDark = document.querySelector('[data-header-dark]');
    if (!this.header) return;
    window.addEventListener('scroll', () => this.onScroll(), { passive: true });
    this.onScroll();
    requestAnimationFrame(() => this.onScroll());
  },

  onScroll() {
    if (!this.header) return;
    const scrollY = window.scrollY;

    if (this.heroDark) {
      const rect = this.heroDark.getBoundingClientRect();
      const headerH = this.header.offsetHeight || 80;
      if (rect.bottom > headerH + 12) {
        this.header.classList.add('header--on-dark');
        this.header.classList.remove('scrolled');
        return;
      }
      this.header.classList.remove('header--on-dark');
    }

    if (scrollY > this.threshold) {
      this.header.classList.add('scrolled');
    } else {
      this.header.classList.remove('scrolled');
    }
  }
};

/* ─── SERVICES TAB NAV ───────────────────────────────────────── */
const ServiceTabNav = {
  tabs: [],
  sections: [],

  init() {
    const nav = document.querySelector('.services-tab-nav');
    if (!nav) return;

    this.tabs = Array.from(nav.querySelectorAll('a'));
    this.tabs.forEach(tab => {
      tab.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(tab.getAttribute('href'));
        if (!target) return;
        const headerH = parseInt(getComputedStyle(document.documentElement)
          .getPropertyValue('--header-height')) || 80;
        const tabNavH = nav.offsetHeight;
        const top = target.getBoundingClientRect().top + window.scrollY - headerH - tabNavH - 8;
        window.scrollTo({ top, behavior: 'smooth' });
      });
    });

    this.sections = this.tabs.map(tab => document.querySelector(tab.getAttribute('href'))).filter(Boolean);
    window.addEventListener('scroll', () => this.onScroll(), { passive: true });
    this.onScroll();
  },

  onScroll() {
    if (!this.sections.length) return;
    const nav = document.querySelector('.services-tab-nav');
    const headerH = 80;
    const tabNavH = nav ? nav.offsetHeight : 0;
    const scrollY = window.scrollY + headerH + tabNavH + 60;

    let current = 0;
    this.sections.forEach((section, i) => {
      if (section.getBoundingClientRect().top + window.scrollY <= scrollY) {
        current = i;
      }
    });

    this.tabs.forEach((tab, i) => {
      tab.classList.toggle('active', i === current);
    });
  }
};

/* ─── SERVICE ACCORDIONS ─────────────────────────────────────── */
const ServiceAccordions = {
  prefersReduced: false,

  init() {
    const items = document.querySelectorAll('.service-item');
    if (!items.length) return;

    this.prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    items.forEach(item => {
      if (this.prefersReduced) {
        // Native behavior for reduced motion
        item.addEventListener('toggle', () => {
          if (item.open) {
            const category = item.closest('.services-list, .service-subgroup-list');
            if (category) {
              category.querySelectorAll('.service-item').forEach(sibling => {
                if (sibling !== item && sibling.open) sibling.removeAttribute('open');
              });
            }
          }
        });
        return;
      }

      const summary = item.querySelector('summary');
      const body = item.querySelector('.service-item__body');
      if (!summary || !body) return;

      summary.addEventListener('click', (e) => {
        e.preventDefault();
        const isOpen = item.hasAttribute('open');

        // Close all siblings
        const category = item.closest('.services-list, .service-subgroup-list');
        if (category) {
          category.querySelectorAll('.service-item[open]').forEach(sibling => {
            if (sibling !== item) {
              const sibBody = sibling.querySelector('.service-item__body');
              if (sibBody) {
                sibBody.style.maxHeight = sibBody.scrollHeight + 'px';
                requestAnimationFrame(() => {
                  sibBody.style.maxHeight = '0';
                  sibBody.style.paddingTop = '0';
                  sibBody.style.paddingBottom = '0';
                });
              }
              setTimeout(() => sibling.removeAttribute('open'), 450);
            }
          });
        }

        if (isOpen) {
          body.style.maxHeight = body.scrollHeight + 'px';
          requestAnimationFrame(() => {
            body.style.maxHeight = '0';
            body.style.paddingTop = '0';
            body.style.paddingBottom = '0';
          });
          setTimeout(() => item.removeAttribute('open'), 450);
        } else {
          item.setAttribute('open', '');
          body.style.maxHeight = '0';
          requestAnimationFrame(() => {
            requestAnimationFrame(() => {
              body.style.maxHeight = body.scrollHeight + 'px';
              body.style.paddingTop = '';
              body.style.paddingBottom = '';
            });
          });
        }
      });
    });
  }
};

/* ─── CALENDAR WIDGET ────────────────────────────────────────── */
const CalendarWidget = {
  state: {
    displayDate: new Date(),
    selectedDate: null,
    minDate: new Date()
  },
  onSelect: null,

  init(onSelect) {
    this.onSelect = onSelect;
    const widget = document.getElementById('calendar-widget');
    if (!widget) return;

    // Set to beginning of today
    this.state.minDate.setHours(0, 0, 0, 0);
    this.state.displayDate = new Date();

    this.render();

    widget.querySelector('.cal-prev').addEventListener('click', () => {
      this.state.displayDate.setMonth(this.state.displayDate.getMonth() - 1);
      this.render();
    });

    widget.querySelector('.cal-next').addEventListener('click', () => {
      this.state.displayDate.setMonth(this.state.displayDate.getMonth() + 1);
      this.render();
    });
  },

  render() {
    const { displayDate, selectedDate, minDate } = this.state;
    const year = displayDate.getFullYear();
    const month = displayDate.getMonth();

    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
      'July', 'August', 'September', 'October', 'November', 'December'];

    const title = document.getElementById('cal-month-label');
    if (title) title.textContent = `${monthNames[month]} ${year}`;

    const grid = document.getElementById('calendar-grid');
    if (!grid) return;

    const weekdays = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'];
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    let html = '<div class="calendar-weekdays">';
    weekdays.forEach(d => { html += `<div class="calendar-weekday">${d}</div>`; });
    html += '</div><div class="calendar-days">';

    for (let i = 0; i < firstDay; i++) {
      html += '<div class="calendar-day empty"></div>';
    }

    for (let day = 1; day <= daysInMonth; day++) {
      const date = new Date(year, month, day);
      date.setHours(0, 0, 0, 0);
      const isToday = date.getTime() === today.getTime();
      const isDisabled = date < minDate;
      const isSelected = selectedDate && date.getTime() === selectedDate.getTime();
      const isSunday = date.getDay() === 0;

      let classes = 'calendar-day';
      if (isToday) classes += ' today';
      if (isDisabled || isSunday) classes += ' disabled';
      if (isSelected) classes += ' selected';

      if (!isDisabled && !isSunday) {
        html += `<div class="${classes}" data-date="${date.toISOString()}">${day}</div>`;
      } else {
        html += `<div class="${classes}">${day}</div>`;
      }
    }

    html += '</div>';
    grid.innerHTML = html;

    grid.querySelectorAll('.calendar-day:not(.disabled):not(.empty)').forEach(el => {
      el.addEventListener('click', () => {
        const dateVal = new Date(el.getAttribute('data-date'));
        this.selectDay(dateVal);
      });
    });
  },

  selectDay(date) {
    this.state.selectedDate = date;
    this.render();
    this.renderTimeSlots(date);
    const slotsContainer = document.getElementById('time-slots');
    if (slotsContainer) slotsContainer.style.display = 'block';
  },

  renderTimeSlots(date) {
    const grid = document.getElementById('time-slots-grid');
    if (!grid) return;

    const times = [];
    for (let h = 9; h <= 17; h++) {
      times.push(`${h === 12 ? 12 : h % 12 || 12}:00 ${h < 12 ? 'AM' : 'PM'}`);
      if (h < 17) times.push(`${h === 12 ? 12 : h % 12 || 12}:30 ${h < 12 ? 'AM' : 'PM'}`);
    }
    times.push('6:00 PM');

    // Deterministically mark some slots as unavailable
    const dateSeed = date.getDate() + date.getMonth() * 7;
    const unavailableIndices = [dateSeed % times.length, (dateSeed + 3) % times.length,
      (dateSeed + 6) % times.length, (dateSeed + 9) % times.length];

    let html = '';
    times.forEach((time, i) => {
      const unavailable = unavailableIndices.includes(i);
      html += `<button class="time-slot${unavailable ? ' unavailable' : ''}"
        ${unavailable ? 'disabled' : ''} data-time="${time}">${time}</button>`;
    });

    grid.innerHTML = html;

    grid.querySelectorAll('.time-slot:not(.unavailable)').forEach(btn => {
      btn.addEventListener('click', () => {
        grid.querySelectorAll('.time-slot').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
        if (this.onSelect) this.onSelect(btn.getAttribute('data-time'));
      });
    });
  }
};

/* ─── BOOKING WIZARD ─────────────────────────────────────────── */
const BookingWizard = {
  state: {
    currentStep: 1,
    category: null,
    categoryLabel: null,
    service: null,
    appointmentType: null,
    date: null,
    time: null,
    name: null
  },

  init() {
    const section = document.querySelector('.booking-section');
    if (!section) return;

    // Init calendar
    CalendarWidget.init((time) => {
      this.state.time = time;
      this.updateSummary();
      this.checkStep4();
    });

    // Category selection (step 1)
    document.querySelectorAll('.selection-card input[name="category"]').forEach(radio => {
      radio.addEventListener('change', () => {
        this.state.category = radio.value;
        this.state.categoryLabel = SERVICES_DATA[radio.value]?.label || radio.value;
        this.populateServiceDropdown(radio.value);
        this.updateSummary();
        this.enableNextBtn(1);
      });
    });

    // Service select (step 2)
    const serviceSelect = document.getElementById('service-select');
    if (serviceSelect) {
      serviceSelect.addEventListener('change', () => {
        this.state.service = serviceSelect.value || null;
        this.updateSummary();
        this.enableNextBtn(2);
      });
    }

    // Appointment type (step 3)
    document.querySelectorAll('.selection-card input[name="appt-type"]').forEach(radio => {
      radio.addEventListener('change', () => {
        this.state.appointmentType = radio.value;
        this.updateSummary();
        this.enableNextBtn(3);
      });
    });

    // Step next buttons
    document.querySelectorAll('.step-next').forEach(btn => {
      btn.addEventListener('click', () => {
        const next = parseInt(btn.getAttribute('data-next'));
        this.goToStep(next);
      });
    });

    // Step back buttons
    document.querySelectorAll('.step-back').forEach(btn => {
      btn.addEventListener('click', () => {
        const back = parseInt(btn.getAttribute('data-back'));
        this.goToStep(back);
      });
    });

    // Submit booking
    const submitBtn = document.getElementById('submit-booking');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => this.submitBooking());
    }

    // Preset consultation (sidebar)
    const presetBtn = document.getElementById('preset-consultation');
    if (presetBtn) {
      presetBtn.addEventListener('click', () => {
        this.goToStep(3);
        const consultRadio = document.querySelector('.selection-card input[value="consultation"]');
        if (consultRadio) {
          consultRadio.checked = true;
          this.state.appointmentType = 'consultation';
          this.updateSummary();
          this.enableNextBtn(3);
        }
      });
    }
  },

  goToStep(n) {
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const currentActive = document.querySelector('.booking-step.active');

    const doTransition = () => {
      document.querySelectorAll('.booking-step').forEach(s => s.classList.remove('active', 'is-leaving'));
      const target = document.getElementById(`step-${n}`);
      if (target) target.classList.add('active');
      this.state.currentStep = n;

      // Update progress bar
      document.querySelectorAll('.progress-step').forEach(el => {
        const stepNum = parseInt(el.getAttribute('data-step'));
        el.classList.remove('active', 'completed');
        if (stepNum === n) el.classList.add('active');
        if (stepNum < n) el.classList.add('completed');
      });

      // Scroll to top of booking
      const bookingSection = document.querySelector('.booking-section');
      if (bookingSection) {
        const top = bookingSection.getBoundingClientRect().top + window.scrollY - 100;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    };

    if (currentActive && !prefersReduced) {
      currentActive.classList.add('is-leaving');
      setTimeout(doTransition, 250);
    } else {
      doTransition();
    }
  },

  enableNextBtn(step) {
    const panel = document.getElementById(`step-${step}`);
    if (!panel) return;
    const btn = panel.querySelector('.step-next');
    if (!btn) return;

    let enabled = false;
    if (step === 1) enabled = !!this.state.category;
    if (step === 2) enabled = !!this.state.service;
    if (step === 3) enabled = !!this.state.appointmentType;
    if (step === 4) enabled = !!(this.state.date && this.state.time);

    btn.disabled = !enabled;
    btn.style.opacity = enabled ? '1' : '0.5';
  },

  checkStep4() {
    this.state.date = CalendarWidget.state.selectedDate;
    this.enableNextBtn(4);
  },

  populateServiceDropdown(category) {
    const select = document.getElementById('service-select');
    if (!select) return;
    const data = SERVICES_DATA[category];
    if (!data) return;

    let html = '<option value="">Choose a service...</option>';
    data.services.forEach(service => {
      html += `<option value="${service}">${service}</option>`;
    });
    select.innerHTML = html;
    this.state.service = null;

    const btn = document.querySelector('#step-2 .step-next');
    if (btn) { btn.disabled = true; btn.style.opacity = '0.5'; }
  },

  updateSummary() {
    const panel = document.getElementById('booking-summary-panel');
    const dl = document.getElementById('booking-summary-dl');
    if (!panel || !dl) return;

    const { category, categoryLabel, service, appointmentType, date, time } = this.state;
    if (!category) { panel.style.display = 'none'; return; }

    panel.style.display = 'block';

    const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    let html = '';
    if (categoryLabel) {
      html += `<div><dt>Category</dt><dd>${categoryLabel}</dd></div>`;
    }
    if (service) {
      html += `<div><dt>Service</dt><dd>${service}</dd></div>`;
    }
    if (appointmentType) {
      const typeLabels = {
        consultation: 'Consultation',
        single: 'Single Session',
        package: 'Package Inquiry',
        followup: 'Follow-Up'
      };
      html += `<div><dt>Type</dt><dd>${typeLabels[appointmentType] || appointmentType}</dd></div>`;
    }
    if (date) {
      const d = new Date(date);
      html += `<div><dt>Date</dt><dd>${monthNames[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}</dd></div>`;
    }
    if (time) {
      html += `<div><dt>Time</dt><dd>${time}</dd></div>`;
    }

    dl.innerHTML = html;
  },

  submitBooking() {
    const form = document.getElementById('booking-form');
    if (!form) return;

    const requiredFields = form.querySelectorAll('[required]');
    let valid = true;

    requiredFields.forEach(field => {
      const errorEl = field.parentElement.querySelector('.form-error');
      if (!field.value.trim()) {
        field.classList.add('error');
        if (errorEl) errorEl.classList.add('visible');
        valid = false;
      } else {
        field.classList.remove('error');
        if (errorEl) errorEl.classList.remove('visible');
      }
    });

    // Email validation
    const emailField = document.getElementById('email');
    if (emailField && emailField.value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailField.value)) {
        emailField.classList.add('error');
        const errorEl = emailField.parentElement.querySelector('.form-error');
        if (errorEl) { errorEl.textContent = 'Please enter a valid email.'; errorEl.classList.add('visible'); }
        valid = false;
      }
    }

    if (!valid) return;

    const phoneField = document.getElementById('phone');
    if (phoneField && phoneField.value.trim()) {
      const digits = phoneField.value.replace(/\D/g, '');
      if (digits.length < 10) {
        phoneField.classList.add('error');
        const errorEl = phoneField.parentElement.querySelector('.form-error');
        if (errorEl) {
          errorEl.textContent = 'Please enter a valid phone number.';
          errorEl.classList.add('visible');
        }
        return;
      }
    }

    // Get form values
    this.state.name = document.getElementById('full-name')?.value;

    // Render confirmation
    const summary = document.getElementById('confirmation-summary');
    if (summary) {
      const { categoryLabel, service, appointmentType, date, time, name } = this.state;
      const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'];
      const typeLabels = {
        consultation: 'Consultation',
        single: 'Single Session',
        package: 'Package Inquiry',
        followup: 'Follow-Up'
      };

      let dateStr = '';
      if (date) {
        const d = new Date(date);
        dateStr = `${monthNames[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}`;
      }

      summary.innerHTML = `<dl>
        ${name ? `<dt>Name</dt><dd>${name}</dd>` : ''}
        ${categoryLabel ? `<dt>Category</dt><dd>${categoryLabel}</dd>` : ''}
        ${service ? `<dt>Service</dt><dd>${service}</dd>` : ''}
        ${appointmentType ? `<dt>Type</dt><dd>${typeLabels[appointmentType] || appointmentType}</dd>` : ''}
        ${dateStr ? `<dt>Date</dt><dd>${dateStr}</dd>` : ''}
        ${time ? `<dt>Time</dt><dd>${time}</dd>` : ''}
      </dl>`;
    }

    this.goToStep(6);
    this.applySquareBookingLink();
  },

  applySquareBookingLink() {
    const url = window.ND_SQUARE_BOOKING_URL;
    const link = document.getElementById('square-booking-link');
    const pending = document.getElementById('square-booking-pending');
    if (url && link) {
      link.href = url;
      link.removeAttribute('hidden');
      if (pending) pending.hidden = true;
    }
  }
};

/* ─── SCROLL REVEAL ──────────────────────────────────────────── */
const ScrollReveal = {
  observer: null,

  init() {
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReduced) {
      document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-visible'));
      return;
    }

    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const el = entry.target;
            const delay = el.getAttribute('data-reveal-delay');
            if (delay) {
              el.style.transitionDelay = (parseFloat(delay) * 0.1) + 's';
            }
            el.classList.add('is-visible');
            this.observer.unobserve(el);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: '-60px 0px -40px 0px'
      }
    );

    document.querySelectorAll('[data-reveal]').forEach(el => this.observer.observe(el));
  }
};

/* ─── PARALLAX HERO ──────────────────────────────────────────── */
const ParallaxHero = {
  layers: [],
  rafId: null,
  ratio: 0.28,

  init() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    this.layers = Array.from(document.querySelectorAll('.parallax-bg-layer'));
    if (!this.layers.length) return;

    window.addEventListener('scroll', () => {
      if (this.rafId) cancelAnimationFrame(this.rafId);
      this.rafId = requestAnimationFrame(() => {
        const scrollY = window.scrollY;
        this.layers.forEach((layer) => {
          const section = layer.closest('section');
          if (!section) return;
          const heroEnd = section.offsetTop + section.offsetHeight;
          if (scrollY > heroEnd) {
            layer.style.transform = '';
            return;
          }
          layer.style.transform = `translateY(${scrollY * this.ratio}px)`;
        });
      });
    }, { passive: true });
  }
};

/* ─── WELCOME COLLAGE PARALLAX (subtle) ──────────────────────── */
const CollageParallax = {
  section: null,
  tiles: [],
  rafId: null,

  init() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    this.section = document.getElementById('hero-welcome');
    this.tiles = Array.from(document.querySelectorAll('.hero-collage__tile[data-parallax]'));
    if (!this.section || !this.tiles.length) return;

    window.addEventListener('scroll', () => this.onScroll(), { passive: true });
    this.onScroll();
  },

  onScroll() {
    if (this.rafId) cancelAnimationFrame(this.rafId);
    this.rafId = requestAnimationFrame(() => {
      const scrollY = window.scrollY;
      const wTop = this.section.offsetTop;
      const wH = this.section.offsetHeight;
      const vh = window.innerHeight;
      const start = wTop - vh;
      const end = wTop + wH;

      this.tiles.forEach((tile) => {
        const ratio = parseFloat(tile.getAttribute('data-parallax') || '0.06');
        if (scrollY < start || scrollY > end) {
          tile.style.transform = '';
          return;
        }
        const local = scrollY - (wTop - vh * 0.35);
        const y = Math.max(-32, Math.min(32, local * ratio * 0.045));
        tile.style.transform = `translate3d(0, ${y}px, 0)`;
      });
    });
  }
};

/* ─── SPOTLIGHT GLOW CARDS ───────────────────────────────────── */
/*
 * Vanilla JS port of the GlowCard (spotlight-card) React component.
 * Tracks the global pointer position and pushes --glow-x / --glow-y /
 * --glow-xp CSS custom properties onto every [data-glow] element so the
 * radial-gradient spotlight follows the cursor across the page.
 */
const SpotlightCards = {
  cards: [],

  init() {
    this.cards = Array.from(document.querySelectorAll('[data-glow]'));
    if (!this.cards.length) return;

    // Use pointermove for both mouse and touch
    document.addEventListener('pointermove', (e) => {
      this._update(e.clientX, e.clientY);
    }, { passive: true });

    // On touch start / move keep it smooth
    document.addEventListener('touchmove', (e) => {
      const t = e.touches[0];
      if (t) this._update(t.clientX, t.clientY);
    }, { passive: true });
  },

  _update(clientX, clientY) {
    const xp = (clientX / window.innerWidth).toFixed(4);

    this.cards.forEach((card) => {
      card.style.setProperty('--glow-x',  clientX.toFixed(2));
      card.style.setProperty('--glow-y',  clientY.toFixed(2));
      card.style.setProperty('--glow-xp', xp);
    });
  }
};

/* ─── INIT ───────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  MobileNav.init();
  StickyHeader.init();
  ServiceTabNav.init();
  ServiceAccordions.init();
  BookingWizard.init();
  ScrollReveal.init();
  ParallaxHero.init();
  CollageParallax.init();
  SpotlightCards.init();
});
