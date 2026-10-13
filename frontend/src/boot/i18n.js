import { createI18n } from 'vue-i18n'
import { default as messages } from '@/i18n'
import { usePreferredLanguages } from '@vueuse/core'

const preferredLanguages = usePreferredLanguages()
const i18n = createI18n({
  locale: resolvePreferredLocale(preferredLanguages.value[0]),
  fallbackLocale: 'en-US',
  legacy: false, // comment this out if not using Composition API
  fallbackWarn: false,
  missingWarn: false,
  messages,
})

const getLanguageName = locale => {
  const localeName = new Intl.DisplayNames([locale], {
    type: 'language',
    languageDisplay: 'standard',
  })
  return localeName.of(locale)
}
function resolvePreferredLocale(preferredLocale) {
  // exact match avail?
  if (Object.keys(messages).includes(preferredLocale)) return preferredLocale

  // if no exact match, maybe at least the base lang is avail?
  const baseLang = preferredLocale.split('-')[0]
  const fallbackLang = Object.keys(messages).find(key => key.startsWith(baseLang))
  if (fallbackLang) return fallbackLang

  return 'en-US' // final fallback
}

export default ({ app }) => {
  console.log(
    `preferred languages configured in the browser: ${preferredLanguages.value.join(', ')}.,
     best match for ${preferredLanguages.value[0]} found is ${i18n.global.locale.value}, otherwise fallback to en-US`
  )

  // Tell app to use the I18n instance
  app.use(i18n)
}
export { getLanguageName, preferredLanguages }
