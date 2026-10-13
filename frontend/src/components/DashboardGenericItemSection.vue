<template>
  <!-- one key / value row of a plugin stats card (.pb-admin-row, defined in AdminLayout) -->
  <div class="pb-admin-row">
    <span class="pb-admin-row__label">{{ substats.name }}</span>
    <span class="pb-admin-row__value">
      <template v-if="substats.display == 'label'">{{ formatValue(substats.val, substats.decimals, substats.unit) }}</template>
      <q-checkbox v-else-if="substats.display == 'checkbox'" :model-value="substats.val" dense></q-checkbox>
      <q-toggle v-else-if="substats.display == 'toggle'" :model-value="substats.val" dense></q-toggle>
      <template v-else-if="substats.display == 'spinner'">
        <q-spinner v-if="substats.val" class="item-section__spinner" />
      </template>
      <template v-else>{{ substats.val }}</template>
    </span>
  </div>
</template>

<script setup lang="ts">
import type { components } from '@/dto/api'

defineProps<{
  substats: components['schemas']['SubStats']
}>()

const formatValue = (val: string | number | boolean | null, decimals: number, suffix: string) => {
  if (val === null || val === undefined) return 'N/A'
  if (typeof val === 'string') return val
  if (typeof val === 'boolean') return val

  return `${val.toFixed(decimals)}${suffix}`
}
</script>

<style scoped>
.item-section__spinner {
  color: var(--t1);
}
</style>
