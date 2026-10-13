<!--
  PbSpinner — 3x3 pulsing processing grid, replaces QSpinnerGrid (dc.html L379-380).
  Props:
    label?: string               accessible status text (role="status"); omit for a purely decorative spinner
  Cells: 56px, radius 18, gap 14; colour p[i % 5] (t1..t4 appear, centre #f4f5f8),
  glow 0 0 24px -4px <colour>, pbPulse 1.2s with delays [0,.1,.3,.6,.8,.4,.7,.5,.2]s.
-->
<template>
  <div class="pb-spinner" :role="label ? 'status' : undefined" :aria-label="label" :aria-hidden="label ? undefined : 'true'">
    <span v-for="cell in CELLS" :key="cell.index" class="pb-spinner__cell" :style="cell.style" />
  </div>
</template>

<script setup lang="ts">
const { label } = defineProps<{
  label?: string
}>()

const DELAYS = [0, 0.1, 0.3, 0.6, 0.8, 0.4, 0.7, 0.5, 0.2]
const CENTRE = '#f4f5f8'

const CELLS = DELAYS.map((delay, index) => {
  const color = index === 4 ? CENTRE : `var(--t${(index % 5) + 1})`
  return {
    index,
    style: { background: color, boxShadow: `0 0 24px -4px ${color}`, animationDelay: `${delay}s` },
  }
})
</script>

<style scoped>
.pb-spinner {
  display: grid;
  grid-template-columns: repeat(3, 56px);
  gap: 14px;
}

.pb-spinner__cell {
  width: 56px;
  height: 56px;
  border-radius: 18px;
  animation: pbPulse 1.2s ease-in-out infinite;
}

@media (prefers-reduced-motion: reduce) {
  .pb-spinner__cell {
    animation: none;
  }
}
</style>
