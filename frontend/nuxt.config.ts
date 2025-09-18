// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-05-15",
  devtools: { enabled: true },
  modules: ["@nuxt/ui", "@nuxt/icon", '@nuxtjs/i18n'],
  css: ["~/assets/css/main.css"],
  runtimeConfig: {
    API_URL: process.env.API_URL,
  },
  devServer: {
    host: "0.0.0.0",
    port: 3000,
  },
  app: {
    head: {
      link: [
        {
          rel: "icon",
          type: "image/webp",
          href: "logo4.webp",
        },
      ],
    },
  },
  i18n: {
    defaultLocale: 'en',
    locales: [
      { code: 'en', name: 'English', iso: 'en-US', file: 'en.json' },
      { code: 'fr', name: 'Français', iso: 'fr-FR', file: 'fr.json' },
    ],
  },
});
