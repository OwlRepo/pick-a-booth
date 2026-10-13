<!--
  PbAutoReturnBar — "Photo X of Y · Back to start in Ns" bar (dc.html L118).
  Props:
    progress: number             0..1 fill fraction (clamped); drive it from the existing HeaderCountdownTimer value
    color?: string = 'var(--t3)' fill colour, any CSS value
    left?: string                left caption, e.g. "Photo 12 of 48" (or #left slot)
    right?: string               right caption, e.g. "Back to start in 14s" (or #right slot)
  Captions: 14px / 600 / muted. Track: 6px, rgba(255,255,255,.1).
-->
<template>
  <div class="pb-auto-return-bar">
    <div class="pb-auto-return-bar__captions">
      <span
        ><slot name="left">{{ left }}</slot></span
      >
      <span
        ><slot name="right">{{ right }}</slot></span
      >
    </div>
    <div class="pb-auto-return-bar__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" :aria-valuenow="percent">
      <div class="pb-auto-return-bar__fill" :style="{ width: `${percent}%`, background: color }" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const {
  progress,
  color = 'var(--t3)',
  left,
  right,
} = defineProps<{
  progress: number
  color?: string
  left?: string
  right?: string
}>()

const percent = computed(() => Math.round(Math.min(1, Math.max(0, Number.isFinite(progress) ? progress : 0)) * 100))
</script>

<style scoped>
.pb-auto-return-bar {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.pb-auto-return-bar__captions {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  font-weight: 600;
  color: var(--pb-muted);
}

.pb-auto-return-bar__track {
  height: 6px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.1);
  overflow: hidden;
}

.pb-auto-return-bar__fill {
  height: 100%;
  border-radius: 999px;
}
</style>
