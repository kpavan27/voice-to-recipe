/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        saffron: {
          400: '#FB923C',
          500: '#F97316',
          600: '#EA6C00',
        },
        cream: {
          50:  '#FFFBF5',
          100: '#FEF3C7',
        },
        espresso: {
          900: '#1C0A00',
        },
        herb: {
          400: '#4ADE80',
          500: '#22C55E',
        },
      },
      fontFamily: {
        display: ['"Playfair Display"', 'Georgia', 'serif'],
        body:    ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
