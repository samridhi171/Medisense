/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./dist/*html"],
  theme: {
    FontFamliy :{
      jockey: ['Jockey One', 'sans-serif'], // Add Jockey One here
    },
    extend: {
      animation: {
        'translate-y-up-down': 'translateYUpDown 3s ease-in-out infinite',
        zoomIn: 'zoomIn 0.5s ease-out',
        raiseUp: 'raiseUp 1s ease-out',
        slideInSideBySide: 'slideInSideBySide 0.9s ease-out',
      },
      keyframes: {
        zoomIn: {
          '0%': { transform: 'scale(1)', opacity: '0' },
          '100%': { transform: 'scale(3)', opacity: '1' },
        },
        raiseUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        translateYUpDown: {
          '0%, 100%': { transform: 'translateY(15px)' },
          '50%': { transform: 'translateY(-15px)' }, // Adjust the value as needed
        },
        slideInSideBySide: {
          '0%': { transform: 'translateX(-100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
