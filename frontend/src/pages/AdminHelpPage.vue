<template>
  <q-page id="admin-help-page" padding>
    <h1 class="help-title">{{ $t('Getting started?') }}</h1>
    <p class="help-intro">{{ $t('You made it here, so the booth is running on this computer. Here is how to continue.') }}</p>

    <div class="help-grid">
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t1)"></span>{{ $t('Camera setup') }}</div>
        <p>{{
          $t(
            'Open the configuration and pick the cameras section to choose and set up your camera backend. Check the live preview on the start screen afterwards.'
          )
        }}</p>
        <p>{{ $t('Mount the camera so it cannot move, light your guests evenly from the front and avoid bright windows behind them.') }}</p>
        <div class="pb-admin-actions">
          <router-link :to="{ name: 'config' }" class="pb-admin-action"
            ><PbIcon name="settings" :size="18" />{{ $t('TAB_LABEL_CONFIG') }}</router-link
          >
        </div>
      </section>

      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t2)"></span>{{ $t('Extras') }}</div>
        <p>{{
          $t(
            'Plugins add extras such as LED light effects, syncing files to another location and more. Enable and configure them in the plugins section of the configuration.'
          )
        }}</p>
        <p>{{ $t('A multicamera setup needs a calibration before it creates wigglegrams. The Multicamera page walks you through it.') }}</p>
        <div class="pb-admin-actions">
          <router-link to="/admin/multicam" class="pb-admin-action"><PbIcon name="camera" :size="18" />{{ $t('TAB_MULTICAM') }}</router-link>
        </div>
      </section>

      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t3)"></span>{{ $t('Troubleshooting') }}</div>
        <p>{{
          $t(
            'If the preview stays empty, check that the camera is connected and not used by another program, then reload the services from the dashboard.'
          )
        }}</p>
        <p>{{ $t('If a changed setting has no effect, save it again with Apply switched on so the services reload.') }}</p>
        <div class="pb-admin-actions">
          <router-link to="/admin" class="pb-admin-action"><PbIcon name="layout-dashboard" :size="18" />{{ $t('TAB_LABEL_DASHBOARD') }}</router-link>
        </div>
      </section>

      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t4)"></span>{{ $t('Where to find logs') }}</div>
        <p>{{ $t('The Logs page lists the latest log messages and lets you download the full log file. Include it when you ask for help.') }}</p>
        <div class="pb-admin-actions">
          <router-link to="/admin/logs" class="pb-admin-action"><PbIcon name="list" :size="18" />{{ $t('Logs') }}</router-link>
        </div>
      </section>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import PbIcon from '@/components/pb/PbIcon.vue'
</script>

<style scoped>
.help-title {
  margin: 0 0 8px;
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 40px;
  line-height: 1.1;
}

.help-intro {
  margin: 0 0 20px;
  font-size: 17px;
  color: var(--pb-muted);
}

.help-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
  align-items: start;
}

.help-grid p {
  margin: 6px 0 0;
  font-size: 15px;
  line-height: 1.5;
  color: var(--pb-muted-2);
}

@media (max-width: 640px) {
  .help-grid {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
