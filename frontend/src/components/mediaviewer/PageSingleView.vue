<template>
  <div class="pb-single-view column no-wrap flex-center full-height">
    <MediaItemPreviewViewer :item="item" />
  </div>
</template>

<script setup lang="ts">
import { default as MediaItemPreviewViewer } from '../MediaItemPreviewViewer.vue'
import type { components } from '@/dto/api'

defineProps<{
  item: components['schemas']['MediaitemPublic']
}>()
</script>

<style scoped>
.pb-single-view {
  padding: 20px;
  border-radius: 32px;
  background: var(--pb-surface-1);
}
</style>
