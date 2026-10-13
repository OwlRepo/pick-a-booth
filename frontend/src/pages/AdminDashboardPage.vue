<template>
  <!-- 21 AdminDashboardPage (dc.html L319-322); cards without an artboard reuse the same card pattern -->
  <q-page id="admin-page" padding>
    <div class="dashboard-grid">
      <!-- Server control -->
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow">
          <span class="pb-admin-card__dot" style="background: var(--pb-live)"></span>{{ $t('TITLE_SERVER_CONTROL') }}
        </div>
        <h2 class="pb-admin-card__title">{{ $t('Booth') }}</h2>
        <div class="pb-admin-actions">
          <button type="button" class="pb-admin-action" @click="confirm_reload_service = true">
            <PbIcon name="rotate-ccw" :size="18" />{{ $t('Reload services') }}
          </button>
          <button type="button" class="pb-admin-action" @click="confirm_reboot_host = true">
            <PbIcon name="rotate-ccw" :size="18" />{{ $t('Reboot Host') }}
          </button>
          <button type="button" class="pb-admin-action pb-admin-action--danger" @click="confirm_shutdown_host = true">
            <PbIcon name="power" :size="18" />{{ $t('Shutdown Host') }}
          </button>
        </div>

        <template v-if="store.information_onetime.platform_system == 'Linux'">
          <div class="pb-admin-card__eyebrow dashboard-subhead">{{ $t('Systemctl (Linux only)') }}</div>
          <div class="pb-admin-actions">
            <button type="button" class="pb-admin-action" @click="confirm_install_systemctl = true">
              <PbIcon name="plus" :size="18" />{{ $t('install systemctl service') }}
            </button>
            <button type="button" class="pb-admin-action" @click="confirm_uninstall_systemctl = true">
              <PbIcon name="x" :size="18" />{{ $t('uninstall systemctl service') }}
            </button>
            <button type="button" class="pb-admin-action" @click="confirm_restart_systemctl = true">
              <PbIcon name="rotate-ccw" :size="18" />{{ $t('restart systemctl service') }}
            </button>
          </div>
        </template>
      </section>

      <!-- Health (system information) -->
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t4)"></span>{{ $t('System') }}</div>
        <h2 class="pb-admin-card__title">{{ $t('Health') }}</h2>

        <div class="pb-admin-meter">
          <div class="pb-admin-meter__head">
            <span class="pb-admin-row__label">{{ $t('cpu load') }}</span>
            <span class="pb-admin-row__value">{{ store.information_interval.cpu_percent }}%</span>
          </div>
          <div class="pb-admin-meter__track">
            <div class="pb-admin-meter__fill" :style="meterFill(store.information_interval.cpu_percent / 100, 'var(--t5)')"></div>
          </div>
        </div>

        <div class="pb-admin-meter">
          <div class="pb-admin-meter__head">
            <span class="pb-admin-row__label">{{ $t('disk space') }}</span>
            <span class="pb-admin-row__value">{{ (store.information_onetime.disk.free / 1024 ** 3).toFixed(1) }} {{ $t('GB available') }}</span>
          </div>
          <div class="pb-admin-meter__track">
            <div
              class="pb-admin-meter__fill"
              :style="meterFill(store.information_onetime.disk.used / store.information_onetime.disk.total, 'var(--t4)')"
            ></div>
          </div>
        </div>

        <div class="pb-admin-meter">
          <div class="pb-admin-meter__head">
            <span class="pb-admin-row__label">{{ $t('memory') }}</span>
            <span class="pb-admin-row__value"
              >{{ (store.information_interval.memory.available / 1024 ** 3).toFixed(1) }} {{ $t('GB available') }}</span
            >
          </div>
          <div class="pb-admin-meter__track">
            <div
              class="pb-admin-meter__fill"
              :style="meterFill(store.information_interval.memory.used / store.information_interval.memory.total, 'var(--t3)')"
            ></div>
          </div>
        </div>

        <div v-if="store.information_interval.battery_percent !== null" class="pb-admin-meter">
          <div class="pb-admin-meter__head">
            <span class="pb-admin-row__label">{{ $t('Battery') }}</span>
            <span class="pb-admin-row__value">{{ store.information_interval.battery_percent.toFixed(0) }}%</span>
          </div>
          <div class="pb-admin-meter__track">
            <div class="pb-admin-meter__fill" :style="meterFill(store.information_interval.battery_percent / 100, 'var(--t2)')"></div>
          </div>
        </div>

        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('app version') }}</span>
          <span class="pb-admin-row__value">{{ store.information_onetime.version }}</span>
        </div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('hostname') }}</span>
          <span class="pb-admin-row__value">{{ store.information_onetime.platform_node }}</span>
        </div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('Frontend build date') }}</span>
          <span class="pb-admin-row__value">{{ builddate }}</span>
        </div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('data directory') }}</span>
          <span class="dashboard-row-end">
            <span class="pb-admin-row__value">{{ store.information_onetime.data_directory }}</span>
            <q-btn flat round class="pb-admin-btn pb-admin-btn--round pb-admin-btn--flat" to="/admin/files" :aria-label="$t('TAB_LABEL_FILES')">
              <PbIcon name="folder" :size="20" />
            </q-btn>
          </span>
        </div>

        <template v-if="Object.keys(store.information_interval.temperatures).length > 0">
          <div class="pb-admin-card__eyebrow dashboard-subhead">{{ $t('System Temperatures') }}</div>
          <div v-for="(value, key) in store.information_interval.temperatures" :key="key" class="pb-admin-row">
            <span class="pb-admin-row__label">{{ key }}</span>
            <span class="pb-admin-row__value">{{ value }}</span>
          </div>
        </template>

        <template v-if="Object.keys(filteredPiThrottledFlags).length > 0">
          <div class="pb-admin-card__eyebrow dashboard-subhead">{{ $t('Pi Throttled Flags') }}</div>
          <div v-for="(value, key) in filteredPiThrottledFlags" :key="key" class="pb-admin-row">
            <span class="pb-admin-row__label">{{ key }}</span>
            <span class="pb-admin-row__value" :class="{ 'dashboard-danger': value }">{{ value }}</span>
          </div>
        </template>
      </section>

      <!-- Media counts -->
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t2)"></span>{{ $t('Media Database') }}</div>
        <h2 class="pb-admin-card__title">{{ $t('Media') }}</h2>

        <div v-if="Object.keys(store.information_interval.mediacollection).length == 0" class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('Currently there is no item to display.') }}</span>
        </div>
        <div v-for="(entry, key) in store.information_interval.mediacollection" :key="key" class="pb-admin-row">
          <span class="pb-admin-row__label">{{ key }}</span>
          <span class="pb-admin-row__value">{{ entry }}</span>
        </div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('Language') }}</span>
          <!-- eslint-disable-next-line @intlify/vue-i18n/no-raw-text -->
          <span class="pb-admin-row__value">{{ getLanguageName(locale) }}, {{ locale }}</span>
        </div>

        <div class="pb-admin-actions dashboard-actions">
          <button type="button" class="pb-admin-action pb-admin-action--danger" @click="confirm_delete_all = true">
            <PbIcon name="trash" :size="18" />{{ $t('BTN_LABEL_DELETE_ALL_MEDIA_FILES') }}
          </button>
          <button type="button" class="pb-admin-action pb-admin-action--danger" @click="confirm_clear_recycle_directory = true">
            <PbIcon name="trash" :size="18" />{{ $t('Clear recycle directory') }}
          </button>
        </div>
      </section>

      <!-- Language -->
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t3)"></span>{{ $t('Language') }}</div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('Selected language') }}</span>
          <!-- eslint-disable-next-line @intlify/vue-i18n/no-raw-text -->
          <span class="pb-admin-row__value">{{ getLanguageName(locale) }}, {{ locale }}</span>
        </div>
        <div class="pb-admin-row dashboard-row-top">
          <span class="pb-admin-row__label">{{ $t('Browsers preferred languages') }}</span>
          <span class="pb-admin-row__value dashboard-list">
            <span v-for="(language, index) in preferredLanguages" :key="language" :class="{ 'text-italic': index == 0 }">{{ language }}</span>
          </span>
        </div>
      </section>

      <!-- Platform -->
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t5)"></span>{{ $t('platform') }}</div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('machine') }}</span>
          <span class="pb-admin-row__value">{{
            $t('{platform_machine}, {cpu_count} cores', {
              platform_machine: store.information_onetime.platform_machine,
              cpu_count: store.information_onetime.platform_cpu_count,
            })
          }}</span>
        </div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('platform system') }}</span>
          <span class="pb-admin-row__value">{{ store.information_onetime.platform_system }} {{ store.information_onetime.platform_release }}</span>
        </div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('computer model') }}</span>
          <span class="pb-admin-row__value">{{ store.information_onetime.model }}</span>
        </div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('python executable') }}</span>
          <span class="pb-admin-row__value">{{ store.information_onetime.python_executable }}</span>
        </div>
        <div class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('python version') }}</span>
          <span class="pb-admin-row__value">{{ store.information_onetime.platform_python_version }}</span>
        </div>
      </section>

      <!-- Backends -->
      <section v-for="(backend_stats, _, index) in store.information_interval.backends" :key="index" class="pb-admin-card">
        <div class="pb-admin-card__eyebrow">
          <span class="pb-admin-card__dot" style="background: var(--t4)"></span>{{ $t('Backend Index: ') }}{{ index }}
        </div>
        <div v-for="(field_value, field_key) in backend_stats" :key="field_key" class="pb-admin-row">
          <span class="pb-admin-row__label">{{ field_key }}</span>
          <span class="pb-admin-row__value">{{ field_value }}</span>
        </div>
      </section>

      <!-- Plugins -->
      <DashboardGenericStatsCard v-for="(entry, key) in store.information_interval.plugins" :key="key" :stats="entry"></DashboardGenericStatsCard>

      <!-- Stats counter -->
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t1)"></span>{{ $t('Stats counter') }}</div>
        <div v-if="store.information_interval.stats_counter.length == 0" class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('Currently there is no item to display.') }}</span>
        </div>
        <div v-for="(entry, index) in store.information_interval.stats_counter" :key="index" class="pb-admin-row dashboard-row-compact">
          <span class="pb-admin-row__label">{{ entry.action }}</span>
          <span class="dashboard-row-end">
            <span class="pb-admin-row__value">
              {{ entry.count }}
              <q-tooltip>{{ $t('Last used at:') }} {{ entry.last_used_at }}</q-tooltip>
            </span>
            <q-btn
              flat
              round
              class="pb-admin-btn pb-admin-btn--round pb-admin-btn--flat"
              :aria-label="$t('yes, reset')"
              @click="displayResetStatsConfirm(entry.action)"
            >
              <PbIcon name="rotate-ccw" :size="20" />
            </q-btn>
          </span>
        </div>
        <div class="pb-admin-actions dashboard-actions">
          <button type="button" class="pb-admin-action" @click="displayResetStatsConfirm('')">
            <PbIcon name="rotate-ccw" :size="18" />{{ $t('Reset all') }}
          </button>
        </div>
      </section>

      <!-- Limits counter -->
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t3)"></span>{{ $t('Limits counter') }}</div>
        <div v-if="store.information_interval.limits_counter.length == 0" class="pb-admin-row">
          <span class="pb-admin-row__label">{{ $t('Currently there is no item to display.') }}</span>
        </div>
        <div v-for="(entry, index) in store.information_interval.limits_counter" :key="index" class="pb-admin-row dashboard-row-compact">
          <span class="pb-admin-row__label">{{ entry.action }}</span>
          <span class="dashboard-row-end">
            <span class="pb-admin-row__value">
              {{ entry.count }}
              <q-tooltip>{{ $t('Last used at:') }} {{ entry.last_used_at }}</q-tooltip>
            </span>
            <q-btn
              flat
              round
              class="pb-admin-btn pb-admin-btn--round pb-admin-btn--flat"
              :aria-label="$t('yes, reset')"
              @click="displayResetLimitsConfirm(entry.action)"
            >
              <PbIcon name="rotate-ccw" :size="20" />
            </q-btn>
          </span>
        </div>
        <div class="pb-admin-actions dashboard-actions">
          <button type="button" class="pb-admin-action" @click="displayResetLimitsConfirm('')">
            <PbIcon name="rotate-ccw" :size="18" />{{ $t('Reset all') }}
          </button>
        </div>
      </section>
    </div>

    <!-- the 10 confirm dialogs -->
    <q-dialog v-for="dialog in confirmDialogs" :key="dialog.message" v-model="dialog.open.value">
      <div class="pb-dialog">
        <div class="pb-dialog__body">
          <span class="pb-dialog__icon" :class="{ 'pb-dialog__icon--danger': dialog.danger }"><PbIcon :name="dialog.icon" :size="24" /></span>
          <span>{{ $t(dialog.message) }}</span>
        </div>
        <div class="pb-dialog__actions">
          <PbPill v-close-popup>{{ $t('BTN_LABEL_CANCEL') }}</PbPill>
          <PbPill
            v-close-popup
            :bg="dialog.danger ? 'var(--pb-danger-text)' : 'var(--t1)'"
            :fg="dialog.danger ? 'var(--pb-bg)' : 'var(--t1i)'"
            @click="dialog.confirm()"
            >{{ $t(dialog.confirmLabel) }}</PbPill
          >
        </div>
      </div>
    </q-dialog>
  </q-page>
</template>

<script setup lang="ts">
import { computed, ref, type Ref } from 'vue'
import { useMediacollectionStore } from '@/stores/mediacollection-store'
import { useMainStore } from '@/stores/main-store'
import { remoteProcedureCall } from '@/util/fetch_api.js'
import { useI18n } from 'vue-i18n'
import { getLanguageName, preferredLanguages } from '@/boot/i18n'
import DashboardGenericStatsCard from '@/components/DashboardGenericStatsCard.vue'
import PbIcon from '@/components/pb/PbIcon.vue'
import PbPill from '@/components/pb/PbPill.vue'

const { locale } = useI18n({ useScope: 'global' })
const store = useMainStore()
const mediacollectionStore = useMediacollectionStore()
const selected_field = ref('')
const confirm_reset_limits_counter = ref(false)
const confirm_reset_stats_counter = ref(false)
const confirm_reboot_host = ref(false)
const confirm_shutdown_host = ref(false)
const confirm_reload_service = ref(false)
const confirm_restart_systemctl = ref(false)
const confirm_install_systemctl = ref(false)
const confirm_uninstall_systemctl = ref(false)
const confirm_delete_all = ref(false)
const confirm_clear_recycle_directory = ref(false)
const builddate = new Date(import.meta.env.BUILD_DATE).toLocaleString()

const displayResetLimitsConfirm = (field: string) => {
  selected_field.value = field
  confirm_reset_limits_counter.value = true
}

const displayResetStatsConfirm = (field: string) => {
  selected_field.value = field
  confirm_reset_stats_counter.value = true
}
const actionResetStatsConfirmed = () => {
  remoteProcedureCall('/api/admin/information/cntr/reset/' + selected_field.value)
  confirm_reset_stats_counter.value = false
}
const actionResetLimitsConfirmed = () => {
  remoteProcedureCall('/api/admin/share/cntr/reset/' + selected_field.value)
  confirm_reset_limits_counter.value = false
}

// message / confirmLabel are i18n keys; icon is a PbIcon name
interface ConfirmDialog {
  open: Ref<boolean>
  icon: string
  message: string
  confirmLabel: string
  danger: boolean
  confirm: () => void
}

const confirmDialogs: ConfirmDialog[] = [
  {
    open: confirm_reboot_host,
    icon: 'restart_alt',
    message: 'MSG_CONFIRM_REBOOT',
    confirmLabel: 'BTN_LABEL_REBOOT',
    danger: false,
    confirm: () => remoteProcedureCall('/api/system/host/reboot'),
  },
  {
    open: confirm_shutdown_host,
    icon: 'power_settings_new',
    message: 'MSG_CONFIRM_SHUTDOWN',
    confirmLabel: 'BTN_LABEL_SHUTDOWN',
    danger: true,
    confirm: () => remoteProcedureCall('/api/system/host/shutdown'),
  },
  {
    open: confirm_reload_service,
    icon: 'restart_alt',
    message: 'You sure to reload the services?',
    confirmLabel: 'BTN_LABEL_RELOAD_SERVICE',
    danger: false,
    confirm: () => remoteProcedureCall('/api/system/service/reload'),
  },
  {
    open: confirm_restart_systemctl,
    icon: 'restart_alt',
    message: 'MSG_CONFIRM_RESTART_SERVICE',
    confirmLabel: 'BTN_LABEL_RESTART_SERVICE',
    danger: false,
    confirm: () => remoteProcedureCall('/api/system/systemctl/restart'),
  },
  {
    open: confirm_install_systemctl,
    icon: 'plus',
    message: 'MSG_CONFIRM_INSTALL_SERVICE',
    confirmLabel: 'BTN_LABEL_INSTALL_SERVICE',
    danger: false,
    confirm: () => remoteProcedureCall('/api/system/systemctl/install'),
  },
  {
    open: confirm_uninstall_systemctl,
    icon: 'cancel',
    message: 'MSG_CONFIRM_UNINSTALL_SERVICE',
    confirmLabel: 'BTN_LABEL_UNINSTALL_SERVICE',
    danger: false,
    confirm: () => remoteProcedureCall('/api/system/systemctl/uninstall'),
  },
  {
    open: confirm_reset_stats_counter,
    icon: 'restart_alt',
    message: 'Are you sure you want to reset the usage statistics counter?',
    confirmLabel: 'yes, reset',
    danger: true,
    confirm: actionResetStatsConfirmed,
  },
  {
    open: confirm_reset_limits_counter,
    icon: 'restart_alt',
    message: 'Are you sure you want to reset the share limits counter?',
    confirmLabel: 'yes, reset',
    danger: true,
    confirm: actionResetLimitsConfirmed,
  },
  {
    open: confirm_delete_all,
    icon: 'delete',
    message: 'MSG_CONFIRM_DELETE_ALL_MEDIA_FILES',
    confirmLabel: 'Yes, delete',
    danger: true,
    confirm: () => mediacollectionStore.deleteAllItems(),
  },
  {
    open: confirm_clear_recycle_directory,
    icon: 'delete',
    message: 'Are you sure to clear the recycle directory?',
    confirmLabel: 'Yes, delete',
    danger: true,
    confirm: () => remoteProcedureCall('/api/admin/files/clearrecycledir'),
  },
]

// meter fill width as a clamped percentage (dc.html L321)
const meterFill = (fraction: number, color: string) => ({
  width: `${Math.min(100, Math.max(0, (Number.isFinite(fraction) ? fraction : 0) * 100))}%`,
  background: color,
})

// Computed filtering logic
const filteredPiThrottledFlags = computed(() => {
  const flags = store.information_interval.pi_throttled_flags
  return Object.fromEntries(Object.entries(flags).filter(([key, value]) => key === 'undervoltage_occurred' || value === true))
})
</script>

<style scoped>
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  align-items: start;
}

.dashboard-subhead {
  margin-top: 14px;
}

.dashboard-actions {
  margin-top: 10px;
}

.dashboard-row-end {
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}

.dashboard-row-compact {
  padding: 0;
}

.dashboard-row-top {
  align-items: flex-start;
}

.dashboard-list {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.dashboard-danger {
  color: var(--pb-danger-text);
}

/* no portrait artboard: 2 columns in portrait, 1 on phones */
@media (orientation: portrait) {
  .dashboard-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .dashboard-grid {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
