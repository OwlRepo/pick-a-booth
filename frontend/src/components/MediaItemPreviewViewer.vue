<!--
  MediaItemPreviewViewer — full preview of one media item (image via q-img, video via <video>).
  Props:
    item: MediaitemPublic
    fit?: 'contain' | 'cover' = 'contain'   'cover' for the full-bleed slideshow (dc.html L180)
-->
<template>
  <div v-if="isImage(item.processed)" class="full-height full-width">
    <q-img
      :draggable="false"
      class="full-height"
      :fit="fit"
      loading="eager"
      loading-show-delay="800"
      no-transition
      :src="`/media/preview/${item.id}?${item.revision}`"
    />
  </div>
  <div v-else-if="isVideo(item.processed)" class="full-height full-width">
    <video
      :draggable="false"
      :src="`/media/preview/${item.id}?${item.revision}`"
      class="full-height full-width"
      muted
      autoplay
      :style="{ objectFit: fit, maxWidth: '100%', maxHeight: '100%', display: 'block' }"
      loop
      playsinline
      controlslist="nofullscreen nodownload noremoteplayback noplaybackrate"
      disablepictureinpicture
    ></video>
  </div>

  <!--eslint-disable-next-line @intlify/vue-i18n/no-raw-text-->
  <div v-else>Element not supported to display.</div>
</template>

<script setup lang="ts">
import type { components } from '@/dto/api'
import { isVideo, isImage } from '@/util/media_is_type'

const { fit = 'contain' } = defineProps<{
  item: components['schemas']['MediaitemPublic']
  fit?: 'contain' | 'cover'
}>()
</script>
