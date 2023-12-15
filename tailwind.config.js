/** @type {import("tailwindcss").Config} */
export default {
  content: ["./src/**/*.{html,css,svelte,ts}"],
  daisyui: {
    theme: ["night", "dark"]
  },
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui")
  ],
}
