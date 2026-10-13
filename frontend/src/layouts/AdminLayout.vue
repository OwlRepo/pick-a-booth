<template>
  <q-layout id="admin-layout" view="hHh lpR fFf">
    <!-- 21 AdminLayout header (dc.html L316-318) -->
    <q-header class="admin-header">
      <div class="admin-header__bar">
        <div class="admin-header__left">
          <PbPill icon="arrow-left" :icon-size="19" :font-size="16" @click="router.push('/')">{{ $t('Booth') }}</PbPill>

          <nav class="admin-tabs" :aria-label="$t('TITLE_ADMIN_CENTER')">
            <router-link v-for="tab in tabs" :key="tab.label" v-slot="{ href, navigate, isActive }" :to="tab.to" custom>
              <a
                :href="href"
                class="admin-tabs__tab"
                :class="{ 'admin-tabs__tab--active': isActive }"
                :aria-current="isActive ? 'page' : undefined"
                @click="navigate"
              >
                <svg v-if="tab.icon === 'multicam'" v-bind="SVG_ATTRS" aria-hidden="true">
                  <path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z" />
                  <path d="M9 13h6" />
                  <path d="M12 10v6" />
                </svg>
                <PbIcon v-else :name="tab.icon" :size="18" />
                {{ $t(tab.label) }}
              </a>
            </router-link>

            <button type="button" class="admin-tabs__tab admin-tabs__more" :aria-label="$t('More')">
              <PbIcon name="ellipsis" :size="18" />
              <q-menu class="pb-admin-menu" anchor="bottom right" self="top right" :offset="[0, 8]" auto-close>
                <q-list>
                  <q-item to="/admin/1ststart">
                    <q-item-section avatar>
                      <q-icon name="sym_o_info" />
                    </q-item-section>
                    <q-item-section>
                      <q-item-label>{{ $t('1st Start') }}</q-item-label>
                    </q-item-section>
                  </q-item>
                  <q-item to="/admin/help">
                    <q-item-section avatar>
                      <q-icon name="sym_o_help" />
                    </q-item-section>
                    <q-item-section>
                      <q-item-label>{{ $t('TAB_LABEL_HELP') }}</q-item-label>
                    </q-item-section>
                  </q-item>
                  <q-item href="/api/doc" target="_blank">
                    <q-item-section avatar>
                      <q-icon name="sym_o_api" />
                    </q-item-section>
                    <q-item-section>
                      <q-item-label>{{ $t('Rest-API documentation') }}</q-item-label>
                    </q-item-section>
                    <q-item-section side>
                      <q-icon name="sym_o_open_in_new" />
                    </q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </button>
          </nav>
        </div>

        <PbPill icon="log-out" :icon-size="19" :font-size="16" @click="click_logout">{{ $t('Sign out') }}</PbPill>
      </div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { useRouter, type RouteLocationRaw } from 'vue-router'
import { logout } from '@/util/auth'
import PbPill from '@/components/pb/PbPill.vue'
import PbIcon from '@/components/pb/PbIcon.vue'

const router = useRouter()

// Lucide "camera" with a plus (dc.html L317 Multicam tab); not in the shared icon map
const SVG_ATTRS = {
  width: 18,
  height: 18,
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-width': 2,
  'stroke-linecap': 'round',
  'stroke-linejoin': 'round',
  style: 'flex: none',
} as const

const tabs: { to: RouteLocationRaw; icon: string; label: string }[] = [
  { to: '/admin', icon: 'layout-dashboard', label: 'TAB_LABEL_DASHBOARD' },
  // name based so even if children are active, the config tab is highlighted
  { to: { name: 'config' }, icon: 'settings', label: 'TAB_LABEL_CONFIG' },
  { to: '/admin/files', icon: 'folder', label: 'TAB_LABEL_FILES' },
  { to: '/admin/multicam', icon: 'multicam', label: 'TAB_MULTICAM' },
  { to: '/admin/logs', icon: 'list', label: 'Logs' },
]

const click_logout = () => {
  logout()
  router.push('/')
}
</script>

<style scoped>
.admin-header {
  padding: 24px 24px 0;
  background: var(--pb-bg);
  color: var(--pb-text);
}

.admin-header__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  height: 64px;
}

.admin-header__left {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 0;
}

.admin-tabs {
  display: flex;
  gap: 4px;
  min-width: 0;
  padding: 5px;
  border-radius: 999px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  overflow-x: auto;
  scrollbar-width: none;
}

.admin-tabs__tab {
  appearance: none;
  position: relative;
  display: flex;
  align-items: center;
  gap: 8px;
  flex: none;
  height: 42px;
  margin: 0;
  padding: 0 16px;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: var(--pb-muted);
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  white-space: nowrap;
  text-decoration: none;
  cursor: pointer;
}

/* 42px pill, 52px hit target (the group's 5px padding) */
.admin-tabs__tab::before {
  content: '';
  position: absolute;
  inset: -5px 0;
}

.admin-tabs__tab:hover {
  color: var(--pb-text);
}

.admin-tabs__tab--active,
.admin-tabs__tab--active:hover {
  background: var(--pb-text);
  color: var(--pb-bg);
}

.admin-tabs__tab:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: -3px;
}

.admin-tabs__more {
  padding: 0 12px;
}
</style>

<style lang="scss">
// Shared admin patterns (dc.html L316-337), used by every page rendered inside this layout.
// Unscoped on purpose: q-dialog / q-menu content is teleported to <body>, outside #admin-layout.

#admin-layout {
  background: var(--pb-bg);
  color: var(--pb-text);

  .q-layout-padding {
    padding: 20px 24px 24px;
  }
}

// card (L320)
.pb-admin-card {
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 0;
  padding: 24px;
  border-radius: 28px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  color: var(--pb-text);
  overflow: hidden;
}

.pb-admin-card__eyebrow {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--pb-muted);
}

.pb-admin-card__dot {
  flex: none;
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: var(--pb-live);
}

.pb-admin-card__title {
  margin: 0 0 8px;
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 26px;
  line-height: normal;
}

// key / value row (L321-322)
.pb-admin-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  padding: 11px 0;
  border-top: var(--pb-line);
  font-size: 15px;
}

.pb-admin-row__label {
  color: var(--pb-muted);
}

.pb-admin-row__value {
  min-width: 0;
  font-weight: 700;
  text-align: right;
  overflow-wrap: anywhere;
}

// meter row (L321)
.pb-admin-meter {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 11px 0;
  border-top: var(--pb-line);
}

.pb-admin-meter__head {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  font-size: 15px;
}

.pb-admin-meter__track {
  height: 8px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
}

.pb-admin-meter__fill {
  height: 100%;
  max-width: 100%;
  border-radius: 999px;
}

// action rows (L320, L322)
.pb-admin-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 6px;
}

.pb-admin-action {
  appearance: none;
  position: relative;
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  height: 48px;
  margin: 0;
  padding: 0 16px;
  border: 0;
  border-radius: 14px;
  background: var(--pb-surface-2);
  color: var(--pb-text);
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  text-align: left;
  text-decoration: none;
  cursor: pointer;
}

// 48px row, 52px hit target (fits in the 10px gap)
.pb-admin-action::before {
  content: '';
  position: absolute;
  inset: -2px 0;
}

.pb-admin-action:hover:not(:disabled) {
  background: var(--pb-surface-2-hover);
}

.pb-admin-action:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 2px;
}

.pb-admin-action:disabled {
  cursor: default;
  opacity: 0.5;
}

.pb-admin-action--danger {
  color: var(--pb-danger-text);
}

// q-btn restyled as a 52px pill (no-artboard pages)
.q-btn.pb-admin-btn {
  min-height: 52px;
  padding: 0 21px;
  border-radius: 999px;
  background: var(--pb-surface-2);
  color: var(--pb-text);
  font-size: 16px;
  font-weight: 700;
}

.q-btn.pb-admin-btn--primary {
  background: var(--t1);
  color: var(--t1i);
}

.q-btn.pb-admin-btn--danger {
  color: var(--pb-danger-text);
}

.q-btn.pb-admin-btn--flat {
  background: transparent;
}

.q-btn.pb-admin-btn--round {
  min-width: 52px;
  padding: 0;
}

// confirm dialogs
.pb-dialog {
  display: flex;
  flex-direction: column;
  gap: 24px;
  width: min(520px, 92vw);
  max-width: 92vw;
  padding: 28px;
  border-radius: 28px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  color: var(--pb-text);
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.5);
}

.pb-dialog__body {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 17px;
  line-height: 1.4;
}

.pb-dialog__icon {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: none;
  width: 52px;
  height: 52px;
  border-radius: 999px;
  background: var(--pb-surface-2);
  color: var(--t1);
}

.pb-dialog__icon--danger {
  color: var(--pb-danger-text);
}

.pb-dialog__title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 22px;
}

.pb-dialog__actions {
  display: flex;
  justify-content: flex-end;
  flex-wrap: wrap;
  gap: 10px;
}

// ⋯ menu
.pb-admin-menu {
  padding: 8px;
  border-radius: 20px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  color: var(--pb-text);

  .q-item {
    min-height: 52px;
    border-radius: 14px;
    font-weight: 700;
  }

  .q-item__section--side {
    color: var(--pb-muted);
  }
}
</style>
