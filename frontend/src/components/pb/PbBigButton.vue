<!--
  PbBigButton — large primary action (dc.html L102, L110, L123, L125).
  Props:
    height?: number = 96        px; design uses 52-124. Radius = min(32, floor(height / 3)) unless `pill`
    bg?: string = 'var(--pb-surface-2)'   any CSS value, e.g. 'var(--t5)'
    fg?: string = 'var(--pb-text)'        any CSS value, e.g. 'var(--t5i)'
    bordered?: boolean           adds the 1px line border (surface-2 "Try again" style)
    icon?: string                PbIcon name (stroke 2.2), or use the #icon slot (e.g. <PbStopSquare>)
    iconSize?: number = 28
    fontSize?: number = 24       label: Sora 600, letter-spacing -.02em
    pill?: boolean               radius 999px (Stop recording 104px, Save 52px)
    padding?: string             CSS padding, e.g. '0 48px' (pill buttons size to content)
    block?: boolean              width: 100%
    disabled?: boolean
  Slots: default = label, icon = custom icon.
  Native listeners (@click) fall through to the <button>.
-->
<template>
  <button type="button" class="pb-big-button" :class="{ 'pb-big-button--block': block }" :disabled="disabled" :style="rootStyle">
    <slot name="icon">
      <PbIcon v-if="icon" :name="icon" :size="iconSize" :stroke-width="2.2" />
    </slot>
    <span v-if="$slots.default" class="pb-big-button__label" :style="{ fontSize: `${fontSize}px` }"><slot /></span>
  </button>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import PbIcon from './PbIcon.vue'

const {
  height = 96,
  bg = 'var(--pb-surface-2)',
  fg = 'var(--pb-text)',
  bordered = false,
  icon,
  iconSize = 28,
  fontSize = 24,
  pill = false,
  padding,
  block = false,
  disabled = false,
} = defineProps<{
  height?: number
  bg?: string
  fg?: string
  bordered?: boolean
  icon?: string
  iconSize?: number
  fontSize?: number
  pill?: boolean
  padding?: string
  block?: boolean
  disabled?: boolean
}>()

const rootStyle = computed(() => ({
  height: `${height}px`,
  borderRadius: pill ? '999px' : `${Math.min(32, Math.floor(height / 3))}px`,
  background: bg,
  color: fg,
  ...(bordered ? { border: 'var(--pb-line)' } : {}),
  ...(padding ? { padding } : {}),
}))
</script>

<style scoped>
.pb-big-button {
  appearance: none;
  margin: 0;
  border: 0;
  padding: 0;
  font: inherit;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  flex: none;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.pb-big-button--block {
  width: 100%;
}

.pb-big-button:hover:not(:disabled) {
  filter: brightness(1.08);
}

.pb-big-button:active:not(:disabled) {
  transform: scale(0.98);
}

.pb-big-button:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

.pb-big-button:disabled {
  cursor: default;
  opacity: 0.5;
}

.pb-big-button__label {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  white-space: nowrap;
}
</style>
