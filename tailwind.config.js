/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        // Add your custom colors here
        "custom-1-sand": "#e2c8bb",
        "custom-2": "#7fcdff",
        "custom-3": "#1da2d8",
        "custom-4": "#00b3b3",
      },
    },
  },
  plugins: [],
};
