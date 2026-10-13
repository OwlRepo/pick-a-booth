<!--
  PbGhostButton — secondary surface button, e.g. Filter / Delete (dc.html L124).
  Props:
    icon?: string                PbIcon name (22px, stroke 2), or use the #icon slot
    orientation?: 'auto' | 'landscape' | 'portrait' = 'auto'
                                 height 72 (landscape) / 88 (portrait); 'auto' follows the orientation media query
    disabled?: boolean
  Slots: default = label (Manrope 700 19px), icon = custom icon.
  Native listeners (@click) fall through to the <button>.
-->
<template>
  <button type="button" class="pb-ghost-button" :class="{ 'pb-ghost-button--portrait': isPortrait }" :disabled="disabled">
    <slot name="icon">
      <PbIcon v-if="icon" :name="icon" :size="22" />
    </slot>
    <span v-if="$slots.default" class="pb-ghost-button__label"><slot /></span>
  </button>
</template>

<script setup lang="ts">
import PbIcon from './PbIcon.vue'
import { useIsPortrait, type PbOrientation } from './orientation'

const {
  icon,
  orientation = 'auto',
  disabled = false,
} = defineProps<{
  icon?: string
  orientation?: PbOrientation
  disabled?: boolean
}>()

const isPortrait = useIsPortrait(() => orientation)
</script>

<style scoped>
.pb-ghost-button {
  appearance: none;
  margin: 0;
  padding: 0;
  font: inherit;
  height: 72px;
  border-radius: 20px;
  background: var(--pb-surface-2);
  border: var(--pb-line);
  color: var(--pb-text);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.pb-ghost-button--portrait {
  height: 88px;
}

.pb-ghost-button:hover:not(:disabled) {
  background: var(--pb-surface-2-hover);
}

.pb-ghost-button:active:not(:disabled) {
  transform: scale(0.98);
}

.pb-ghost-button:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

.pb-ghost-button:disabled {
  cursor: default;
  opacity: 0.5;
}

.pb-ghost-button__label {
  font-weight: 700;
  font-size: 19px;
  white-space: nowrap;
}
</style>
