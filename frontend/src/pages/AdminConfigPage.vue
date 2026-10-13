<template>
  <!-- 22 AdminConfigPage (dc.html L331-337): section nav card left, form card right -->
  <q-page id="config-page" padding>
    <div class="config-layout">
      <nav class="config-nav" :aria-label="$t('TAB_LABEL_CONFIG')">
        <button
          v-for="(label, index) in navLabels"
          :key="`${selected_configuration}-${index}`"
          type="button"
          class="config-nav__item"
          :class="{ 'config-nav__item--active': index == navActive }"
          :aria-current="index == navActive ? 'true' : undefined"
          @click="navActive = index"
        >
          {{ categoryTitle(label) }}
        </button>

        <template v-if="configurables.length > 1">
          <div class="config-nav__heading">{{ $t('TAB_LABEL_CONFIG') }}</div>
          <router-link
            v-for="(element, index) in configurables"
            :key="index"
            v-slot="{ href, navigate }"
            :to="{ name: 'config', params: { section: element } }"
            replace
            custom
          >
            <a
              :href="href"
              class="config-nav__item"
              :class="{ 'config-nav__item--current': element == selected_configuration }"
              :aria-current="element == selected_configuration ? 'page' : undefined"
              @click="navigate"
              >{{ categoryTitle(element.split('.').pop()) }}</a
            >
          </router-link>
        </template>
      </nav>

      <section class="config-card">
        <header class="config-card__head">
          <h2 class="config-card__title">{{ categoryTitle(navLabels[navActive] ?? selected_configuration) }}</h2>
          <div class="config-card__actions">
            <PbPill @click="confirm_reset_config = true">{{ $t('BTN_LABEL_RESET_CONFIG') }}</PbPill>
            <PbPill @click="updateFormSchema()">{{ $t('BTN_LABEL_RELOAD_CONFIG') }}</PbPill>
            <label class="config-card__apply">
              <ToggleSwitch v-model="autoReloadServicesOnSave" />
              {{ $t('Apply') }}
              <q-tooltip>{{ $t('Reload services on save to apply settings. Reloading might take some time.') }} </q-tooltip>
            </label>
            <PbBigButton
              :height="52"
              pill
              padding="0 24px"
              bg="var(--t1)"
              fg="var(--t1i)"
              icon="check"
              :icon-size="20"
              :font-size="17"
              @click="saveConfig()"
            >
              {{ $t('BTN_LABEL_PERSIST_CONFIG') }}
            </PbBigButton>
          </div>
        </header>

        <div class="config-card__body">
          <json-forms
            v-if="!isLoadingState"
            :data="configuration"
            :ajv="ajv"
            :renderers="renderers"
            :schema="schema"
            :uischema="cuischema"
            @change="onChange"
          />

          <div v-else class="config-card__loading">
            <PbSpinner />
          </div>
        </div>
      </section>
    </div>

    <q-dialog v-model="confirm_reset_config">
      <div class="pb-dialog">
        <div class="pb-dialog__body">
          <span class="pb-dialog__icon pb-dialog__icon--danger"><PbIcon name="delete" :size="24" /></span>
          <span>
            {{
              $t('Are you sure that you want to delete the configuration for {selected_configuration} and reset to the defaults?', {
                selected_configuration: selected_configuration,
              })
            }}
          </span>
        </div>
        <div class="pb-dialog__actions">
          <PbPill v-close-popup>{{ $t('BTN_LABEL_CANCEL') }}</PbPill>
          <PbPill
            v-close-popup
            bg="var(--pb-danger-text)"
            fg="var(--pb-bg)"
            @click="[remoteProcedureCall(`/api/admin/config/${selected_configuration}`, 'DELETE'), updateFormSchema()]"
            >{{ $t('yes, reset') }}</PbPill
          >
        </div>
      </div>
    </q-dialog>
  </q-page>
</template>
<script setup lang="ts">
import { ref, provide, onBeforeMount, watch } from 'vue'
import { JsonForms, type JsonFormsChangeEvent } from '@jsonforms/vue'
import { generateDefaultUISchema } from '@jsonforms/core'
import { defaultStyles, mergeStyles, createAjv, quasarRenderers, CONFIG_NAV_KEY, createConfigNavState, categoryTitle } from '@/components/form'
import ToggleSwitch from '@/components/form/controls/ToggleSwitch.vue'
import PbBigButton from '@/components/pb/PbBigButton.vue'
import PbIcon from '@/components/pb/PbIcon.vue'
import PbPill from '@/components/pb/PbPill.vue'
import PbSpinner from '@/components/pb/PbSpinner.vue'
import { remoteProcedureCall, _fetch } from '@/util/fetch_api'
import { useConfigurationStore } from '@/stores/configuration-store'
import { Notify } from 'quasar'
import { useRoute, useRouter } from 'vue-router'
import type { components } from '@/dto/api'
import { useLocalStorage } from '@vueuse/core'
import { UnauthorizedError } from '@/util/auth'

// bind object

const autoReloadServicesOnSave = useLocalStorage('autoReloadServicesOnSave', true)
const route = useRoute()
const router = useRouter()
const configurationStore = useConfigurationStore()
const isLoadingState = ref(true)
const confirm_reset_config = ref(false)

const configurables = ref<string[]>([])
const selected_configuration = ref('')

const configuration = ref({})
const schema = ref({})
const cuischema = ref(generateDefaultUISchema({}))
const ajv = createAjv({
  multipleOfPrecision: 2,
  useDefaults: false,
  removeAdditional: false,
}) // https://ajv.js.org/options.html#usedefaults // https://ajv.js.org/json-schema.html#discriminator use in future?
const renderers = Object.freeze([...quasarRenderers])
const myStyles = mergeStyles(defaultStyles, { control: { label: 'q-label' } })
provide('styles', myStyles)
// section nav state shared with TopLevelNavigationRenderer (it publishes the schema categories)
const configNav = createConfigNavState()
provide(CONFIG_NAV_KEY, configNav)
const { labels: navLabels, active: navActive } = configNav

onBeforeMount(() => {
  const section = (route.params.section as string) || 'app'

  selected_configuration.value = section
  getConfigurables()
  updateFormSchema()
})
watch(route, to => {
  const section = (to.params.section as string) || 'app'
  selected_configuration.value = section

  //TODO: if route different, ask if config if config loss is acceptable if changed. if so, stop router change.

  updateFormSchema()
})
const onChange = (event: JsonFormsChangeEvent) => {
  configuration.value = event.data
}

const getSchema = async () => {
  try {
    const response = await _fetch(`/api/admin/config/${selected_configuration.value}/schema`)
    console.log(response)

    if (!response.ok) {
      throw new Error('Server returned ' + response.status)
    }
    return await response.json()
  } catch (error) {
    console.warn(error)

    Notify.create({
      message: String(error),
      caption: 'Error getting configuration scheme',
      color: 'negative',
    })

    if (error instanceof UnauthorizedError) {
      router.push('/auth/login')
      return
    }
  } finally {
    // commit('setLoading', false);
  }
}
const updateFormSchema = async () => {
  //loadscreen on
  isLoadingState.value = true
  // the form remounts with its first category, as before
  navActive.value = 0

  schema.value = await getSchema()
  cuischema.value = generateDefaultUISchema(schema.value, 'TopLevelNavigation')

  configuration.value = await getConfig() //reload because store could have all data but with usercontext so secrets hidden

  isLoadingState.value = false
}

const getConfigurables = async () => {
  try {
    const response = await _fetch('/api/admin/config/list')

    configurables.value = await response.json()
    console.log(configurables.value)
  } catch (error) {
    console.warn(error)

    Notify.create({
      message: String(error),
      caption: 'Error getting configurables!',
      color: 'red',
    })

    if (error instanceof UnauthorizedError) {
      router.push('/auth/login')
      return
    }
  } finally {
    // commit('setLoading', false);
  }
}

const getConfig = async () => {
  try {
    const response = await _fetch(`/api/admin/config/${selected_configuration.value}`)

    console.log(response)

    return await response.json()
  } catch (error) {
    console.warn(error)

    Notify.create({
      message: String(error),
      caption: 'Error getting config!',
      color: 'red',
    })

    if (error instanceof UnauthorizedError) {
      router.push('/auth/login')
      return
    }
  } finally {
    // commit('setLoading', false);
  }
}

// actions
const saveConfig = async () => {
  console.log('sync config to server')
  console.log(configuration.value)

  try {
    const response = await _fetch(`/api/admin/config/${selected_configuration.value}?reload=${autoReloadServicesOnSave.value}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(configuration.value),
    })

    if (response.ok) {
      // if HTTP-status is 200-299
      // reload configuration again because some default values could be set by server during processing
      configuration.value = await getConfig()

      if (selected_configuration.value == 'app') {
        // 'app' means AppConfig is selected. For AppConfig the data is stored in the pinia store and updated here.
        configurationStore.configuration = configuration.value as components['schemas']['AppConfig']
        configurationStore.postConfigchanged()
      }

      let message = 'Configuration saved.'
      if (autoReloadServicesOnSave.value) {
        message = 'Configuration saved and applied by reloading services.'
      }
      Notify.create({
        message: message,
        color: 'positive',
      })
    } else {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      interface ResponseErrorData {
        detail: {
          loc: string[]
          msg: string
        }[]
      }
      // https://kentcdodds.com/blog/using-fetch-with-type-script
      const json: ResponseErrorData = await response.json()

      let notify_msg = ''
      Object.values(json.detail).forEach(detail => {
        notify_msg += `${detail['msg']}: ${detail['loc'].join('→')}<br/>`
      })

      Notify.create({
        caption: 'Configuration Validation Error',
        icon: 'sym_o_error',
        html: true,
        message: notify_msg,
        color: 'negative',
      })
      return
    }
  } catch (error) {
    console.error(error)
    Notify.create({
      message: String(error),
      caption: 'Error saving config',
      color: 'negative',
    })
  }
}
</script>
<style scoped>
.config-layout {
  display: grid;
  grid-template-columns: 250px minmax(0, 1fr);
  gap: 16px;
  /* viewport minus the admin header (24 + 64), the 20px gap and the 24px bottom padding */
  height: calc(100vh - 132px);
  min-height: 480px;
}

.config-nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-height: 0;
  padding: 12px;
  border-radius: 28px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  overflow-y: auto;
}

.config-nav__item {
  appearance: none;
  position: relative;
  flex: none;
  margin: 0;
  padding: 13px 16px;
  border: 0;
  border-radius: 14px;
  background: transparent;
  color: var(--pb-muted);
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  text-align: left;
  text-decoration: none;
  text-transform: capitalize;
  cursor: pointer;
}

/* ~46px row, 52px hit target */
.config-nav__item::before {
  content: '';
  position: absolute;
  inset: -3px 0;
}

.config-nav__item:hover,
.config-nav__item--current {
  color: var(--pb-text);
}

.config-nav__item--active {
  background: var(--pb-surface-2);
  color: var(--pb-text);
}

.config-nav__item:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: -3px;
}

.config-nav__heading {
  margin: 14px 16px 4px;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--pb-muted);
}

.config-card {
  display: flex;
  flex-direction: column;
  min-width: 0;
  min-height: 0;
  padding: 8px 32px 20px;
  border-radius: 28px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  overflow: hidden;
}

.config-card__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  padding: 16px 0;
}

.config-card__title {
  margin: 0;
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 26px;
  line-height: normal;
  text-transform: capitalize;
}

.config-card__actions {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

.config-card__apply {
  display: flex;
  align-items: center;
  gap: 10px;
  padding-right: 6px;
  font-size: 15px;
  font-weight: 700;
  color: var(--pb-muted);
  cursor: pointer;
}

.config-card__body {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
}

.config-card__loading {
  display: flex;
  justify-content: center;
  padding: 64px 0;
}

/* no portrait artboard: nav stacks above the form and wraps */
@media (orientation: portrait) {
  .config-layout {
    grid-template-columns: minmax(0, 1fr);
    height: auto;
    min-height: 0;
  }

  .config-nav {
    flex-direction: row;
    flex-wrap: wrap;
  }

  .config-nav__heading {
    flex-basis: 100%;
  }

  .config-card__body {
    overflow-y: visible;
  }
}
</style>

<style lang="scss">
#config-page .array-list-description {
  color: var(--pb-muted);
}
</style>
