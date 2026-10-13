<!--
  PbPill — pill button / status pill (dc.html L73, L117, L42 Live, L109 REC).
  Props:
    variant?: 'solid' | 'glass' | 'tint' = 'solid'
              solid = surface-2; glass = blurred glass on camera; tint = rgba(255,255,255,.25) on coloured cards
    size?: 60 | 56 | 52 | 40 = 52     height px; padding 24 / 22 / 21 / 16
    icon?: string                     PbIcon name, rendered before the label (or use the #icon slot)
    iconSize?: number                 default 60: 22 (glass 24), 56: 22, 52: 20, 40: 18
    fontSize?: number                 default 60: 18 (glass 20), 56: 20, 52: 17, 40: 15
    dot?: string                      CSS colour of a leading status dot (Live: 10px, glow 12)
    dotBlink?: boolean                REC dot style: 16px, glow 14, pbBlink 1s steps(1)
    bg?: string / fg?: string         override background / text colour (any CSS value, e.g. 'var(--t1)')
    tag?: 'button' | 'div' = 'button' use 'div' for non-interactive pills (Live, REC); no hover/active then
    disabled?: boolean
  Slots: default = label, icon = custom icon.
  Native listeners (@click) fall through to the root element.
-->
<template>
  <component
    :is="tag"
    :type="isButton ? 'button' : undefined"
    :disabled="isButton ? disabled : undefined"
    class="pb-pill"
    :class="[`pb-pill--${variant}`, { 'pb-pill--interactive': isButton }]"
    :style="rootStyle"
  >
    <span v-if="dot" class="pb-pill__dot" :class="{ 'pb-pill__dot--blink': dotBlink }" :style="{ '--pb-dot': dot }" aria-hidden="true" />
    <slot name="icon">
      <PbIcon v-if="icon" :name="icon" :size="resolvedIconSize" />
    </slot>
    <span v-if="$slots.default" class="pb-pill__label" :style="{ fontSize: `${resolvedFontSize}px` }"><slot /></span>
  </component>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import PbIcon from './PbIcon.vue'

type PillSize = 60 | 56 | 52 | 40

const PRESETS: Record<PillSize, { padding: number; icon: number; font: number }> = {
  60: { padding: 24, icon: 22, font: 18 },
  56: { padding: 22, icon: 22, font: 20 },
  52: { padding: 21, icon: 20, font: 17 },
  40: { padding: 16, icon: 18, font: 15 },
}

const {
  variant = 'solid',
  size = 52,
  icon,
  iconSize,
  fontSize,
  dot,
  dotBlink = false,
  bg,
  fg,
  tag = 'button',
  disabled = false,
} = defineProps<{
  variant?: 'solid' | 'glass' | 'tint'
  size?: PillSize
  icon?: string
  iconSize?: number
  fontSize?: number
  dot?: string
  dotBlink?: boolean
  bg?: string
  fg?: string
  tag?: 'button' | 'div'
  disabled?: boolean
}>()

const isButton = computed(() => tag === 'button')
const preset = computed(() => PRESETS[size])
// the 60px glass pill on the camera view uses a larger icon and label (dc.html L73)
const largeGlass = computed(() => size === 60 && variant === 'glass')
const resolvedIconSize = computed(() => iconSize ?? (largeGlass.value ? 24 : preset.value.icon))
const resolvedFontSize = computed(() => fontSize ?? (largeGlass.value ? 20 : preset.value.font))

const rootStyle = computed(() => ({
  height: `${size}px`,
  padding: `0 ${preset.value.padding}px`,
  ...(bg ? { background: bg } : {}),
  ...(fg ? { color: fg } : {}),
}))
</script>

<style scoped>
.pb-pill {
  appearance: none;
  margin: 0;
  border: 0;
  font: inherit;
  display: flex;
  align-items: center;
  gap: 12px;
  flex: none;
  border-radius: 999px;
  -webkit-tap-highlight-color: transparent;
}

.pb-pill--solid {
  background: var(--pb-surface-2);
  color: var(--pb-text);
}

.pb-pill--glass {
  background: var(--pb-glass-bg);
  backdrop-filter: blur(var(--pb-glass-blur));
  -webkit-backdrop-filter: blur(var(--pb-glass-blur));
  border: var(--pb-glass-border);
  color: var(--pb-text);
}

.pb-pill--tint {
  background: rgba(255, 255, 255, 0.25);
  color: inherit;
}

.pb-pill--interactive {
  cursor: pointer;
}

.pb-pill--interactive:hover:not(:disabled) {
  filter: brightness(1.12);
}

.pb-pill--interactive:active:not(:disabled) {
  transform: scale(0.97);
}

.pb-pill--interactive:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

.pb-pill:disabled {
  cursor: default;
  opacity: 0.5;
}

.pb-pill__label {
  font-weight: 700;
  white-space: nowrap;
}

.pb-pill__dot {
  flex: none;
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: var(--pb-dot);
  box-shadow: 0 0 12px var(--pb-dot);
}

.pb-pill__dot--blink {
  width: 16px;
  height: 16px;
  box-shadow: 0 0 14px var(--pb-dot);
  animation: pbBlink 1s steps(1) infinite;
}

@media (prefers-reduced-motion: reduce) {
  .pb-pill__dot--blink {
    animation: none;
  }
}
</style>
