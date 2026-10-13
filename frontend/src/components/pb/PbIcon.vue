<!--
  PbIcon — Lucide icon with Material Symbols fallback.
  Props:
    name: string            config / sym_o_ name ("photo_camera", "sym_o_print") or Lucide kebab key ("chevron-left")
    size?: number = 24      px
    strokeWidth?: number = 2  Lucide stroke (design uses 2.2 on tiles and big buttons)
  Names without a Lucide mapping (src/theme/icons.ts) render <q-icon name="sym_o_<name>">.
  Decorative: always aria-hidden; label the parent control instead.
-->
<template>
  <component :is="lucide" v-if="lucide" class="pb-icon" :size="size" :stroke-width="strokeWidth" aria-hidden="true" />
  <q-icon v-else class="pb-icon" :name="symbol" :size="`${size}px`" aria-hidden="true" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { lucideFor } from '@/theme/icons'

const {
  name,
  size = 24,
  strokeWidth = 2,
} = defineProps<{
  name: string
  size?: number
  strokeWidth?: number
}>()

const lucide = computed(() => lucideFor(name))
const symbol = computed(() => (name.startsWith('sym_o_') ? name : `sym_o_${name}`))
</script>

<style scoped>
.pb-icon {
  flex: none;
}
</style>
