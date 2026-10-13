<!--
  PbRoundButton — icon-only circle button (dc.html L165 carousel chevrons, top-bar lock circle).
  Props:
    label: string                accessible name (aria-label); required because the button has no text
    icon?: string                PbIcon name (stroke 2), or use the default slot
    size?: number = 72           px; design uses 56 / 60 / 72
    iconSize?: number            default 56: 24, 60: 22, 72: 30, otherwise round(size * 0.42)
    variant?: 'glass' | 'muted' = 'glass'
              glass = blurred glass, hover brightness(1.2), active scale(.95)
              muted = surface-2 with muted icon, hover text colour (top-bar admin lock)
    disabled?: boolean
  Native listeners (@click) fall through to the <button>.
-->
<template>
  <button
    type="button"
    class="pb-round-button"
    :class="`pb-round-button--${variant}`"
    :aria-label="label"
    :disabled="disabled"
    :style="{ width: `${size}px`, height: `${size}px` }"
  >
    <slot>
      <PbIcon v-if="icon" :name="icon" :size="resolvedIconSize" />
    </slot>
  </button>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import PbIcon from './PbIcon.vue'

const ICON_SIZES: Record<number, number> = { 56: 24, 60: 22, 72: 30 }

const {
  label,
  icon,
  size = 72,
  iconSize,
  variant = 'glass',
  disabled = false,
} = defineProps<{
  label: string
  icon?: string
  size?: number
  iconSize?: number
  variant?: 'glass' | 'muted'
  disabled?: boolean
}>()

const resolvedIconSize = computed(() => iconSize ?? ICON_SIZES[size] ?? Math.round(size * 0.42))
</script>

<style scoped>
.pb-round-button {
  appearance: none;
  margin: 0;
  padding: 0;
  border: 0;
  font: inherit;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: none;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.pb-round-button--glass {
  background: var(--pb-glass-bg);
  backdrop-filter: blur(var(--pb-glass-blur));
  -webkit-backdrop-filter: blur(var(--pb-glass-blur));
  border: var(--pb-glass-border);
  color: var(--pb-text);
}

.pb-round-button--glass:hover:not(:disabled) {
  filter: brightness(1.2);
}

.pb-round-button--glass:active:not(:disabled) {
  transform: scale(0.95);
}

.pb-round-button--muted {
  background: var(--pb-surface-2);
  color: var(--pb-muted);
}

.pb-round-button--muted:hover:not(:disabled) {
  color: var(--pb-text);
}

.pb-round-button:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

.pb-round-button:disabled {
  cursor: default;
  opacity: 0.5;
}
</style>
