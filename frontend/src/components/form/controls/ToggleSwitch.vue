<!--
  ToggleSwitch — settings pill toggle (dc.html L336): track 60x34, t1 when on / surface-2 when off,
  26px white knob inset 3px. The button is 52px tall so the hit target meets the 52px minimum.
  Props:
    modelValue: boolean
    disabled?: boolean
  Emits: update:modelValue. Native attrs (id, aria-label, autofocus, @focus, @blur) fall through to the <button>.
-->
<template>
  <button
    type="button"
    role="switch"
    class="toggle-switch"
    :class="{ 'toggle-switch--on': modelValue }"
    :aria-checked="modelValue"
    :disabled="disabled"
    @click="emit('update:modelValue', !modelValue)"
  >
    <span class="toggle-switch__track"><span class="toggle-switch__knob" /></span>
  </button>
</template>

<script setup lang="ts">
const { modelValue, disabled = false } = defineProps<{
  modelValue: boolean
  disabled?: boolean
}>()

const emit = defineEmits<{
  'update:modelValue': [value: boolean]
}>()
</script>

<style scoped>
.toggle-switch {
  appearance: none;
  display: inline-flex;
  align-items: center;
  height: 52px;
  margin: 0;
  padding: 0;
  border: 0;
  background: none;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.toggle-switch__track {
  position: relative;
  display: block;
  width: 60px;
  height: 34px;
  border-radius: 999px;
  background: var(--pb-surface-2);
  border: var(--pb-line);
  transition: background-color 0.15s ease;
}

.toggle-switch--on .toggle-switch__track {
  background: var(--t1);
}

.toggle-switch__knob {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 26px;
  height: 26px;
  border-radius: 999px;
  background: #fff;
  transition: transform 0.15s ease;
}

/* padding box 58px (60 - 1px border each side): 58 - 3 - 26 - 3 = 26px travel, i.e. right: 3px when on */
.toggle-switch--on .toggle-switch__knob {
  transform: translateX(26px);
}

.toggle-switch:focus-visible .toggle-switch__track {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

.toggle-switch:disabled {
  cursor: default;
  opacity: 0.5;
}

@media (prefers-reduced-motion: reduce) {
  .toggle-switch__track,
  .toggle-switch__knob {
    transition: none;
  }
}
</style>
