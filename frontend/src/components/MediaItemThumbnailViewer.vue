<!--
  MediaItemThumbnailViewer — square gallery thumbnail with media-type badge (dc.html L155-157).
  Fills its parent (the gallery tile sets size, radius 22 and overflow).
  Badge by media_type: collage t2 "Collage", animation t3 "GIF", video t4 "Video", multicamera white "Wigglegram"; image: none.
-->
<template>
  <div class="pb-thumb">
    <!-- Display Elements -->
    <q-img
      v-if="isImage(item.processed)"
      class="pb-thumb__media"
      :src="`/media/thumbnail/${item.id}?${item.revision}`"
      loading="eager"
      loading-show-delay="800"
      :ratio="1"
      fit="cover"
    />

    <!-- mimic the q-img for video-elements to make it look same as images but display mp4 gif-like-->
    <video
      v-else-if="isVideo(item.processed)"
      class="pb-thumb__media"
      autoplay
      loop
      muted
      playsinline
      :src="`/media/thumbnail/${item.id}?${item.revision}`"
    ></video>
    <!--eslint-disable-next-line @intlify/vue-i18n/no-raw-text-->
    <div v-else class="pb-thumb__unsupported">Element not supported to display.</div>

    <!-- media-type badge for collages, animations, videos, multicam; none for a basic image -->
    <span v-if="badge" class="pb-thumb__badge" :style="{ background: badge.bg, color: badge.fg }">{{ badge.label }}</span>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import type { components } from '@/dto/api'
import { isVideo, isImage } from '@/util/media_is_type'

const props = defineProps<{
  item: components['schemas']['MediaitemPublic']
}>()

const { t } = useI18n()

const badge = computed(() => {
  switch (props.item.media_type) {
    case 'collage':
      return { label: t('Collage'), bg: 'var(--t2)', fg: 'var(--t2i)' }
    case 'animation':
      return { label: t('GIF'), bg: 'var(--t3)', fg: 'var(--t3i)' }
    case 'video':
      return { label: t('Video'), bg: 'var(--t4)', fg: 'var(--t4i)' }
    case 'multicamera':
      return { label: t('Wigglegram'), bg: '#ffffff', fg: '#0a0b10' }
    default:
      return null
  }
})
</script>

<style scoped>
.pb-thumb {
  position: relative;
  width: 100%;
  height: 100%;
}

.pb-thumb__media {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 50%;
}

.pb-thumb__unsupported {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 12px;
  text-align: center;
  font-size: 13px;
  color: var(--pb-muted);
}

.pb-thumb__badge {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 800;
  line-height: 1.2;
  pointer-events: none;
}
</style>
