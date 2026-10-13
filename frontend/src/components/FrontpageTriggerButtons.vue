<template>
  <!-- mode tiles, dc.html L43-67 (landscape 6 cols x 196px) / L196-220 (portrait 3 x 2, 380px) -->
  <div class="action-buttons frontpage-trigger-buttons">
    <PbModeTile
      v-for="(trigger, index) in visibleTriggers"
      :key="index"
      class="action-button"
      :class="['action-button-' + index]"
      :bg="colors[index].bg"
      :fg="colors[index].fg"
      :icon="isEmpty(trigger.icon) ? undefined : trigger.icon"
      :aria-label="trigger.title || trigger.icon"
      @click="triggerButtonClick(trigger)"
    >
      {{ trigger.title }}
    </PbModeTile>
  </div>
</template>

<script setup lang="ts">
import { isEmpty } from 'lodash'
import { computed } from 'vue'
import type { TriggerSchema } from '@/types/trigger-schema'
import PbModeTile from '@/components/pb/PbModeTile.vue'
import { tileColor } from '@/theme/palette'

const props = defineProps<{
  triggers: TriggerSchema[]
}>()

const visibleTriggers = computed(() => props.triggers.filter(t => t.show_button && !(isEmpty(t.title) && isEmpty(t.icon))))

// trigger.action is "actions/<group>" (e.g. "actions/multicamera"); tileColor matches on the bare group name
const colors = computed(() =>
  visibleTriggers.value.map((trigger, index) => tileColor({ ...trigger, action: trigger.action.replace(/^actions\//, '') }, index))
)

const emit = defineEmits<{
  triggerAction: [trigger: TriggerSchema]
}>()

function triggerButtonClick(trigger: TriggerSchema) {
  emit('triggerAction', trigger)
}
</script>

<style scoped>
.frontpage-trigger-buttons {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  grid-auto-rows: minmax(0, 1fr);
  gap: 14px;
  height: 196px;
}

@media (orientation: portrait) {
  .frontpage-trigger-buttons {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    height: 380px;
  }
}
</style>
