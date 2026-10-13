<template>
  <div class="connection-overlay">
    <div class="connection-overlay__body">
      <q-spinner class="connection-overlay__spinner" size="2em" />
      <span>{{ $t('MSG_CONNECTING_TO_BACKEND') }}</span>
    </div>

    <div class="connection-overlay__actions">
      <PbPill v-close-popup bg="var(--t1)" fg="var(--t1i)" @click="reloadPage">{{ $t('BTN_LABEL_RELOAD_PAGE') }}</PbPill>
    </div>
  </div>
</template>

<script setup lang="ts">
import PbPill from '@/components/pb/PbPill.vue'

const reloadPage = () => {
  window.location.reload()
}
</script>

<style scoped>
/* rendered inside App.vue's q-dialog; same card pattern as the admin dialogs */
.connection-overlay {
  display: flex;
  flex-direction: column;
  gap: 24px;
  width: min(520px, 92vw);
  padding: 28px;
  border-radius: 28px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  color: var(--pb-text);
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.5);
}

.connection-overlay__body {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 17px;
  line-height: 1.4;
}

.connection-overlay__spinner {
  flex: none;
  color: var(--pb-danger-text);
}

.connection-overlay__actions {
  display: flex;
  justify-content: flex-end;
}
</style>
