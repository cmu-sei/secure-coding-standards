// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  extends: '@cmu-sei/sds-documentation-site',
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  app: {
    baseURL: '/secure-coding-standards/',
    // TODO: Remove the following meta tag once the site is ready to be indexed by search engines
    head: {
      meta: [
        { name: 'robots', content: 'noindex, nofollow' }
      ]
    }
  }
})
