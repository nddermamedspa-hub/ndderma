tailwind.config = {
  corePlugins: { preflight: false },
  theme: {
    extend: {
      colors: {
        gold: { DEFAULT: '#B9A885', dark: '#AE9581', light: '#DACDC4', cta: '#C9A84C' },
        cream: { DEFAULT: '#EFEBE3', mid: '#E8E1D3', deep: '#DBCFB9' },
        light: '#F5F0E7',
        welcome: '#D0B09C',
        spa: { DEFAULT: '#373435', dark: '#1C1917', charcoal: '#4B4B4D' },
        muted: '#727376',
      },
      borderRadius: {
        'hero-sm': '1.875rem',
        'hero-md': '3.125rem',
        'hero-lg': '3.75rem',
      },
      fontFamily: {
        headline: ['Bonita', 'Playfair Display', 'Didot', 'Georgia', 'serif'],
        title: ['Alta', 'Jost', 'Futura', 'Helvetica', 'sans-serif'],
        body: ['Bodrumsans', 'Jost', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      boxShadow: {
        card: '0 2px 24px rgba(0,0,0,0.07)',
        nav: '0 2px 16px rgba(0,0,0,0.09)',
        glow: '0 8px 40px rgba(0,0,0,0.11)',
      },
    },
  },
};
