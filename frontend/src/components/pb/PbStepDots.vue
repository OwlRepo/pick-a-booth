<!--
  PbStepDots — step progress dots (dc.html L77, L87, L100).
  Props:
    total: number                number of dots
    value: number                number of completed/active dots (first `value` dots render as 44x14 pills)
    color?: string = 'var(--t1)' active colour, any CSS value (approval screen uses 'var(--t2)')
    ariaLabel?: string           accessible name of the progressbar, e.g. "Shot 2 of 4"
  Inactive dots: 14x14 rgba(255,255,255,.18). Gap 8.
-->
<template>
  <div class="pb-step-dots" role="progressbar" aria-valuemin="0" :aria-valuemax="total" :aria-valuenow="value" :aria-label="ariaLabel">
    <span
      v-for="i in total"
      :key="i"
      class="pb-step-dots__dot"
      :class="{ 'pb-step-dots__dot--active': i <= value }"
      :style="i <= value ? { background: color } : undefined"
    />
  </div>
</template>

<script setup lang="ts">
const {
  total,
  value,
  color = 'var(--t1)',
  ariaLabel,
} = defineProps<{
  total: number
  value: number
  color?: string
  ariaLabel?: string
}>()
</script>

<style scoped>
.pb-step-dots {
  display: flex;
  gap: 8px;
}

.pb-step-dots__dot {
  width: 14px;
  height: 14px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.18);
}

.pb-step-dots__dot--active {
  width: 44px;
}
</style>
