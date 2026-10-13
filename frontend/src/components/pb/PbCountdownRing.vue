<!--
  PbCountdownRing — countdown ring with glass centre (dc.html L74-76, L84-86 "Smile!", L228-229 portrait).
  Props:
    progress: number             0..1 elapsed fraction of the ring (clamped); stroke-dashoffset = 289.03 * (1 - progress)
    color?: string = 'var(--t1)' progress stroke, any CSS value ('var(--t2)' on the capture "Smile!" moment)
    orientation?: 'auto' | 'landscape' | 'portrait' = 'auto'
                                 ring 420px (landscape) / 440px (portrait); glass centre = ring - 48
    fontSize?: number            centre text size; default 230 (landscape) / 220 (portrait); "Smile!" uses 96
  Slots: default = centre content (numeral or message), Sora 600.
-->
<template>
  <div class="pb-countdown-ring" :style="{ width: `${ring}px`, height: `${ring}px` }">
    <svg class="pb-countdown-ring__svg" :width="ring" :height="ring" viewBox="0 0 100 100" aria-hidden="true">
      <circle cx="50" cy="50" r="46" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="3" />
      <circle
        cx="50"
        cy="50"
        r="46"
        fill="none"
        :stroke="color"
        stroke-width="3"
        stroke-linecap="round"
        :stroke-dasharray="CIRCUMFERENCE"
        :stroke-dashoffset="dashOffset"
      />
    </svg>
    <div class="pb-countdown-ring__centre" :style="{ width: `${ring - 48}px`, height: `${ring - 48}px` }">
      <span class="pb-countdown-ring__text" :style="{ fontSize: `${resolvedFontSize}px` }"><slot /></span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useIsPortrait, type PbOrientation } from './orientation'

// 2 * PI * r(46), as in the reference markup
const CIRCUMFERENCE = 289.03

const {
  progress,
  color = 'var(--t1)',
  orientation = 'auto',
  fontSize,
} = defineProps<{
  progress: number
  color?: string
  orientation?: PbOrientation
  fontSize?: number
}>()

const isPortrait = useIsPortrait(() => orientation)
const ring = computed(() => (isPortrait.value ? 440 : 420))
const resolvedFontSize = computed(() => fontSize ?? (isPortrait.value ? 220 : 230))
const dashOffset = computed(() => {
  const clamped = Math.min(1, Math.max(0, Number.isFinite(progress) ? progress : 0))
  return (CIRCUMFERENCE * (1 - clamped)).toFixed(2)
})
</script>

<style scoped>
.pb-countdown-ring {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pb-countdown-ring__svg {
  position: absolute;
  inset: 0;
  transform: rotate(-90deg);
}

.pb-countdown-ring__centre {
  position: relative;
  border-radius: 999px;
  background: var(--pb-glass-bg);
  backdrop-filter: blur(var(--pb-glass-blur));
  -webkit-backdrop-filter: blur(var(--pb-glass-blur));
  border: var(--pb-glass-border);
  display: flex;
  align-items: center;
  justify-content: center;
}

.pb-countdown-ring__text {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1;
}
</style>
