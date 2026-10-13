<template>
  <div class="not-found fullscreen">
    <!-- eslint-disable-next-line @intlify/vue-i18n/no-raw-text -->
    <div class="not-found__code">404</div>
    <div class="not-found__message">{{ $t('MSG_ERROR_NOT_FOUND') }}</div>
    <PbPill :size="60" icon="arrow-left" bg="var(--t1)" fg="var(--t1i)" @click="router.push('/')">{{ $t('Go Home') }}</PbPill>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import PbPill from '@/components/pb/PbPill.vue'

const router = useRouter()
</script>

<style scoped>
.not-found {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 24px;
  background: var(--pb-bg);
  color: var(--pb-text);
  text-align: center;
}

.not-found__code {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.04em;
  font-size: 30vh;
  line-height: 0.92;
  color: var(--t1);
}

.not-found__message {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 40px;
  color: var(--pb-muted);
}
</style>
