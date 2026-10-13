<!--
  PbGhostButton — secondary surface button, e.g. Filter / Delete (dc.html L124).
  Props:
    icon?: string                PbIcon name (22px, stroke 2), or use the #icon slot
    orientation?: 'auto' | 'landscape' | 'portrait' = 'auto'
                                 height 72 (landscape) / 88 (portrait); 'auto' follows the orientation media query
    disabled?: boolean
  Tap area: an invisible ::after grows the hit target to >= 88px around the 72px visual height.
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

/*
 * Invisible tap area of at least 88px around a smaller visual button (guest touch target).
 * :where() keeps `position: relative` at zero specificity so a consumer can still place the
 * button with position: absolute (still a containing block for the pseudo-element).
 * At 88px or taller the insets resolve to 0 and the tap area equals the visual box.
 */
:where(.pb-ghost-button) {
  position: relative;
}

.pb-ghost-button::after {
  content: '';
  position: absolute;
  top: min(0px, calc((100% - 88px) / 2));
  bottom: min(0px, calc((100% - 88px) / 2));
  left: min(0px, calc((100% - 88px) / 2));
  right: min(0px, calc((100% - 88px) / 2));
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
