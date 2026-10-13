<template>
  <div v-if="availableFilter.length > 0" class="pb-filter-cards">
    <button v-for="filter in availableFilter" :key="filter" type="button" class="pb-filter-card" @click="applyFilterClick(filter)">
      <q-img class="pb-filter-card__img" loading="lazy" :ratio="1" :src="`/api/filter/${id}?filter=${filter}`" />
      <span class="pb-filter-card__label">{{ filter }}</span>
    </button>
  </div>
  <div v-else class="pb-filter-cards__empty">
    <q-icon name="sym_o_mood_bad" size="xl"></q-icon>
    <!-- eslint-disable-next-line @intlify/vue-i18n/no-raw-text -->
    <p>No filter available.</p>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  id: string
  availableFilter: string[]
}>()

const emit = defineEmits<{
  triggerApplyFilter: [id: string, filter: string]
}>()

function applyFilterClick(filter: string) {
  // console.log(`trigger action ${action}, config_index ${config_index}`);
  emit('triggerApplyFilter', props.id, filter)
}
</script>

<style scoped>
.pb-filter-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 12px;
}

.pb-filter-card {
  appearance: none;
  margin: 0;
  padding: 0;
  font: inherit;
  position: relative;
  border: var(--pb-line);
  border-radius: 22px;
  overflow: hidden;
  background: var(--pb-surface-2);
  color: var(--pb-text);
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.pb-filter-card:hover {
  transform: scale(1.02);
}

.pb-filter-card:active {
  transform: scale(0.98);
}

.pb-filter-card:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

.pb-filter-card__img {
  display: block;
  width: 100%;
}

.pb-filter-card__label {
  position: absolute;
  right: 10px;
  bottom: 10px;
  padding: 6px 12px;
  border-radius: 999px;
  background: var(--pb-glass-bg);
  backdrop-filter: blur(var(--pb-glass-blur));
  -webkit-backdrop-filter: blur(var(--pb-glass-blur));
  font-size: 13px;
  font-weight: 800;
  pointer-events: none;
}

.pb-filter-cards__empty {
  text-align: center;
  color: var(--pb-muted);
}
</style>
