<template>
  <!-- settings row (dc.html L335-337): label + config key in monospace, control on the right -->
  <div v-if="visible" :id="id" :class="styles.control.root">
    <div class="control-wrapper">
      <div class="control-wrapper__head">
        <div class="control-label-wrapper">
          <label :for="id + '-input'" :class="[styles.control.label, required ? styles.control.required : '']">
            {{ label }}
          </label>
          <q-icon v-if="appliedOptions.computeIntense" name="sym_o_memory" class="control-wrapper__flag control-wrapper__flag--danger">
            <q-tooltip>{{ $t('This setting affects CPU/GPU usage.') }}</q-tooltip>
          </q-icon>
          <q-icon v-if="appliedOptions.deprecated" name="sym_o_block" class="control-wrapper__flag control-wrapper__flag--warning">
            <q-tooltip>{{ $t('This setting is deprecated and may be removed in future versions.') }}</q-tooltip>
          </q-icon>
        </div>
        <div v-if="configKey" class="control-wrapper__key">{{ configKey }}</div>
        <div class="control-description-wrapper">
          <!--div :class="styles.control.description">{{ showDescription ? description : "" }}</div-->
          <div :class="styles.control.description">{{ description }}</div>
        </div>
      </div>
      <div class="control-field">
        <div :class="styles.control.wrapper">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { isDescriptionHidden } from '@jsonforms/core'
import { defineComponent, type PropType } from 'vue'
import type { Styles } from '../styles'
import type { Options } from '../util'

export default defineComponent({
  name: 'ControlWrapper',
  props: {
    id: {
      required: true,
      type: String,
    },
    description: {
      required: false as const,
      type: String,
      default: undefined,
    },
    errors: {
      required: false as const,
      type: String,
      default: undefined,
    },
    label: {
      required: false as const,
      type: String,
      default: undefined,
    },
    appliedOptions: {
      required: false as const,
      type: Object as PropType<Options>,
      default: undefined,
    },
    visible: {
      required: false as const,
      type: Boolean,
      default: true,
    },
    required: {
      required: false as const,
      type: Boolean,
      default: false,
    },
    isFocused: {
      required: false as const,
      type: Boolean,
      default: false,
    },
    styles: {
      required: true,
      type: Object as PropType<Styles>,
    },
    path: {
      required: false as const,
      type: String,
      default: undefined,
    },
  },
  computed: {
    // last segment of the data path, e.g. "uisettings.FRONTPAGE_TEXT" -> "FRONTPAGE_TEXT"
    configKey(): string {
      return this.path?.split('.').pop() ?? ''
    },
    showDescription(): boolean {
      return !isDescriptionHidden(this.visible, this.description, this.isFocused, !!this.appliedOptions?.showUnfocusedDescription)
    },
  },
})
</script>

<style scoped>
.control-wrapper {
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  gap: 24px;
  align-items: center;
  padding: 16px 0;
  border-top: var(--pb-line);
}

.control-wrapper__head {
  min-width: 0;
}

.control-label-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 16px;
  font-weight: 700;
  color: var(--pb-text);
}

.control-wrapper__key {
  font-family: ui-monospace, monospace;
  font-size: 13px;
  color: var(--pb-muted);
  overflow-wrap: anywhere;
}

.control-description-wrapper {
  margin-top: 4px;
  font-size: 13px;
  line-height: 1.4;
  color: var(--pb-muted);
}

.control-wrapper__flag {
  font-size: 18px;
}

.control-wrapper__flag--danger {
  color: var(--pb-danger-text);
}

.control-wrapper__flag--warning {
  color: var(--t3);
}

.control-field {
  min-width: 0;
}

/* inputs 48h r14 (dc.html L337); applies to the q-input / q-select of every control renderer in the slot */
.control-field :deep(.q-field--filled .q-field__control) {
  min-height: 48px;
  height: auto;
  padding: 0 16px;
  border-radius: 14px;
  background: var(--pb-bg);
  border: var(--pb-line);
  color: var(--pb-text);
}

.control-field :deep(.q-field--filled .q-field__control::before),
.control-field :deep(.q-field--filled .q-field__control::after) {
  display: none;
}

.control-field :deep(.q-field--filled.q-field--focused .q-field__control) {
  border-color: var(--pb-text);
}

.control-field :deep(.q-field__native),
.control-field :deep(.q-field__input),
.control-field :deep(.q-field__marginal) {
  height: auto;
  min-height: 46px;
  font-size: 15px;
  color: var(--pb-text);
}

.control-field :deep(.q-slider) {
  color: var(--t1);
}

@media (orientation: portrait) {
  .control-wrapper {
    grid-template-columns: minmax(0, 1fr);
    gap: 12px;
  }
}
</style>
