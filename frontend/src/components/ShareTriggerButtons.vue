<!--
  ShareTriggerButtons — configured share actions as big buttons (dc.html L123 landscape, L257 portrait).
  Renders one PbBigButton per visible trigger (no wrapper element, so the parent grid places them).
  Colour by trigger index: t3, t4, t5, t2 (cycling). Landscape 96h / icon 28 / Sora 24, portrait 88h / icon 25 / Sora 22.
-->
<template>
  <template v-for="(trigger, index) in triggers" :key="index">
    <PbBigButton
      v-if="trigger.show_button && !(isEmpty(trigger.title) && isEmpty(trigger.icon))"
      block
      :height="isPortrait ? 88 : 96"
      :icon-size="isPortrait ? 25 : 28"
      :font-size="isPortrait ? 22 : 24"
      :icon="isEmpty(trigger.icon) ? undefined : trigger.icon"
      :bg="`var(--t${shareColorSlot(index)})`"
      :fg="`var(--t${shareColorSlot(index)}i)`"
      :disabled="getShareAvailable(trigger.handles_images_only)"
      class="action-button action-button-share"
      :class="['share-button-' + index]"
      @click="triggerButtonClick(trigger.config_index)"
    >
      {{ trigger.title }}
    </PbBigButton>
  </template>
</template>

<script setup lang="ts">
import { isEmpty } from 'lodash'
import PbBigButton from '@/components/pb/PbBigButton.vue'
import { useIsPortrait } from '@/components/pb/orientation'

const props = defineProps<{
  triggers: ShareSchema[]
  currentItemIsImage: boolean
}>()

export interface ShareSchema {
  show_button: boolean
  title: string
  icon?: string // icon is optional
  handles_images_only: boolean
  config_index: number
}

// handoff §3 (07/16): share buttons coloured by index t3, t4, then t5, t2
const SHARE_COLOR_SLOTS = [3, 4, 5, 2]
const shareColorSlot = (index: number) => SHARE_COLOR_SLOTS[index % SHARE_COLOR_SLOTS.length]

const isPortrait = useIsPortrait(() => 'auto')

function getShareAvailable(handles_images_only: boolean) {
  return !props.currentItemIsImage && handles_images_only
}

const emit = defineEmits<{
  triggerAction: [config_index: number]
}>()

function triggerButtonClick(config_index: number) {
  console.log(`trigger share config_index ${config_index}`)
  emit('triggerAction', config_index)
}
</script>
