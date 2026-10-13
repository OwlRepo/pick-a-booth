<template>
  <!-- plugin stats card: same card pattern as the dashboard artboard (dc.html L320-322) -->
  <section class="pb-admin-card">
    <div class="pb-admin-card__eyebrow"
      ><span class="pb-admin-card__dot" style="background: var(--t1)"></span>{{ stats.name }} {{ $t('(Plugin)') }}</div
    >

    <template v-for="(stat, index) in stats.stats" :key="index">
      <!-- SubStats -->
      <DashboardGenericItemSection v-if="isSubStats(stat)" :substats="stat"></DashboardGenericItemSection>

      <!-- SubList -->
      <template v-else>
        <div class="pb-admin-card__eyebrow stats-sublist">{{ stat.name }}</div>
        <DashboardGenericItemSection v-for="(sub, i) in stat.val" :key="i" :substats="sub"></DashboardGenericItemSection>
      </template>
    </template>

    <div v-if="stats.actions && stats.actions.length" class="pb-admin-actions stats-actions">
      <button v-for="(action, index) in stats.actions" :key="index" type="button" class="pb-admin-action" @click="actionButtonClick(action)">
        {{ action }}
      </button>
    </div>
  </section>
</template>

<script setup lang="ts">
import DashboardGenericItemSection from './DashboardGenericItemSection.vue'
import type { components } from '@/dto/api'

type SubStats = components['schemas']['SubStats']
type SubList = components['schemas']['SubList']
type StatEntry = SubStats | SubList

defineProps<{
  stats: components['schemas']['GenericStats']
}>()

const emit = defineEmits<{
  triggerAction: [action: string]
}>()

function actionButtonClick(action: string) {
  console.log(`trigger action  ${action}`)
  emit('triggerAction', action)
}
const isSubStats = (stat: StatEntry): stat is SubStats => {
  return !Array.isArray(stat.val)
}
</script>

<style scoped>
.stats-sublist {
  margin-top: 14px;
}

.stats-actions {
  margin-top: 10px;
}
</style>
