<!--
  PageShareParameters — share action input dialog body (dc.html L143-148 landscape 620px, L274-279 portrait 680px).
  Rendered inside the parent's q-dialog (backdrop rgba(5,6,10,.72) + blur 6 is set there).
  Validation rules and the ui_type=int +/- controls are unchanged; q-form only emits on valid input.
-->
<template>
  <div class="pb-share-dialog">
    <q-form autofocus @submit="onSubmit" class="pb-share-dialog__form" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false">
      <div class="pb-share-dialog__head">
        <div class="pb-share-dialog__title-group">
          <span v-if="!isEmpty(parameters_dialog_action_icon)" class="pb-share-dialog__icon">
            <PbIcon :name="parameters_dialog_action_icon" :size="24" />
          </span>
          <span class="pb-share-dialog__title">{{ parameters_dialog_caption }}</span>
        </div>
        <PbRoundButton v-close-popup :size="56" icon="x" :label="$t('BTN_LABEL_CANCEL')" />
      </div>

      <div v-for="parameter in props.parameters" :key="parameter.key" class="pb-share-dialog__field">
        <label class="pb-share-dialog__label" :for="`pb-share-param-${parameter.key}`">{{ parameter.label }}</label>
        <!-- ui_type=int        -->
        <q-input
          v-if="parameter.ui_type == 'int'"
          borderless
          no-error-icon
          class="pb-share-dialog__input"
          v-model="formData[parameter.key]"
          :for="`pb-share-param-${parameter.key}`"
          :key="parameter.key"
          :name="parameter.key"
          :rules="[
            val => (val !== null && val !== '') || 'Please type a number', // required.
            val =>
              (parameter.valid_max && parseInt(val) <= parseInt(parameter.valid_max)) || `Please type a number lower than ${parameter.valid_max}`,
            val => (parameter.valid_min && parseInt(val) >= parseInt(parameter.valid_min)) || `Please type a number more than ${parameter.valid_min}`,
          ]"
        >
          <template v-slot:before>
            <PbRoundButton
              :size="80"
              :label="`${parameter.label} -1`"
              @click="formData[parameter.key] = String(parseInt(formData[parameter.key]) - 1)"
              :disabled="!isEmpty(parameter.valid_min) && parseInt(formData[parameter.key]) <= parseInt(parameter.valid_min)"
            >
              <Minus :size="30" :stroke-width="2" aria-hidden="true" />
            </PbRoundButton>
          </template>
          <template v-slot:after>
            <PbRoundButton
              :size="80"
              :label="`${parameter.label} +1`"
              @click="formData[parameter.key] = String(parseInt(formData[parameter.key]) + 1)"
              :disabled="!isEmpty(parameter.valid_max) && parseInt(formData[parameter.key]) >= parseInt(parameter.valid_max)"
            >
              <Plus :size="30" :stroke-width="2" aria-hidden="true" />
            </PbRoundButton>
          </template>
        </q-input>
        <!-- ui_type=input (and else) -->
        <q-input
          v-else
          borderless
          no-error-icon
          class="pb-share-dialog__input"
          v-model="formData[parameter.key]"
          :for="`pb-share-param-${parameter.key}`"
          :key="parameter.key"
          :name="parameter.key"
          :hint="$t('We only use it to send this photo.')"
          :rules="[
            val => (val && val.length > 0) || 'Please type something',
            val => (parameter.valid_max && val.length <= parseInt(parameter.valid_max)) || `Please type text longest ${parameter.valid_max} chars.`,
            val => (parameter.valid_min && val.length >= parseInt(parameter.valid_min)) || `Please type text shortest ${parameter.valid_min} chars.`,
          ]"
        />
      </div>

      <PbBigButton
        type="submit"
        block
        :height="88"
        :icon-size="30"
        :font-size="26"
        :icon="isEmpty(parameters_dialog_action_icon) ? undefined : parameters_dialog_action_icon"
        bg="var(--t4)"
        fg="var(--t4i)"
      >
        {{ parameters_dialog_action_label }}
      </PbBigButton>
    </q-form>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { onBeforeMount } from 'vue'
import { isEmpty } from 'lodash'
import { Minus, Plus } from 'lucide-vue-next'
import PbBigButton from '@/components/pb/PbBigButton.vue'
import PbIcon from '@/components/pb/PbIcon.vue'
import PbRoundButton from '@/components/pb/PbRoundButton.vue'
const formData = reactive<Record<string, any>>({})

import type { components } from '@/dto/api'

const props = defineProps<{
  config_index: number
  parameters_dialog_caption: string
  parameters_dialog_action_icon: string
  parameters_dialog_action_label: string
  parameters: components['schemas']['ShareProcessingParameters'][]
}>()

const emit = defineEmits<{
  triggerShareActionWithParameters: [config_index: number, input_data: object]
}>()

onBeforeMount(() => {
  // set form data to default values
  props.parameters.forEach(parameter => (formData[parameter.key] = parameter.default))
})

const onSubmit = () => {
  // alternative to get form data from event:
  // const form = new FormData(evt.target as HTMLFormElement)
  // const formData = Object.fromEntries(form)
  // console.error(formData)

  emit('triggerShareActionWithParameters', props.config_index, formData)
}
</script>

<style scoped>
.pb-share-dialog {
  width: 620px;
  max-width: 100%;
  padding: 32px;
  border-radius: 36px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
  color: var(--pb-text);
  font-family: 'Manrope', sans-serif;
}

.pb-share-dialog__form {
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.pb-share-dialog__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
}

.pb-share-dialog__title-group {
  display: flex;
  align-items: center;
  gap: 14px;
  min-width: 0;
}

.pb-share-dialog__icon {
  flex: none;
  width: 52px;
  height: 52px;
  border-radius: 999px;
  background: var(--t4);
  color: var(--t4i);
  display: flex;
  align-items: center;
  justify-content: center;
}

.pb-share-dialog__title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 30px;
  line-height: 1.1;
}

.pb-share-dialog__field {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.pb-share-dialog__label {
  font-size: 15px;
  font-weight: 700;
  color: var(--pb-muted);
}

/* q-input restyled to the 80px r22 field with a 2px t4 border (dc.html L146) */
.pb-share-dialog__input.q-field--with-bottom {
  padding-bottom: 0;
}

.pb-share-dialog__input :deep(.q-field__control) {
  height: 80px;
  padding: 0 24px;
  border-radius: 22px;
  background: var(--pb-bg);
  border: 2px solid var(--t4);
}

.pb-share-dialog__input :deep(.q-field__native) {
  height: 100%;
  padding: 0;
  font-family: 'Manrope', sans-serif;
  font-size: 28px;
  font-weight: 600;
  color: var(--pb-text);
  caret-color: var(--t4);
}

.pb-share-dialog__input :deep(.q-field__before),
.pb-share-dialog__input :deep(.q-field__after) {
  height: 80px;
  padding: 0;
}

.pb-share-dialog__input :deep(.q-field__before) {
  padding-right: 12px;
}

.pb-share-dialog__input :deep(.q-field__after) {
  padding-left: 12px;
}

.pb-share-dialog__input :deep(.q-field__bottom) {
  position: static;
  transform: none;
  padding: 10px 0 0;
  min-height: 0;
  font-size: 14px;
  line-height: 1.4;
  color: var(--pb-muted);
}

.pb-share-dialog__input.q-field--error :deep(.q-field__control) {
  border-color: var(--pb-danger-text);
}

.pb-share-dialog__input.q-field--error :deep(.q-field__bottom) {
  color: var(--pb-danger-text);
}

@media (orientation: portrait) {
  .pb-share-dialog {
    width: 680px;
  }
}
</style>
