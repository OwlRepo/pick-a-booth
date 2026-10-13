<!--
  PbStopSquare — "stop" glyph used by the Stop recording button (dc.html L110): rect x6 y6 w12 h12 rx2.
  Lucide's Square is larger (x3 y3 w18 h18), so this one is custom.
  Props:
    size?: number = 24         px
    strokeWidth?: number = 2.2
  Decorative: aria-hidden.
-->
<template>
  <svg
    class="pb-stop-square"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="strokeWidth"
    stroke-linecap="round"
    stroke-linejoin="round"
    aria-hidden="true"
  >
    <rect x="6" y="6" width="12" height="12" rx="2" />
  </svg>
</template>

<script setup lang="ts">
const { size = 24, strokeWidth = 2.2 } = defineProps<{
  size?: number
  strokeWidth?: number
}>()
</script>

<style scoped>
.pb-stop-square {
  flex: none;
}
</style>
