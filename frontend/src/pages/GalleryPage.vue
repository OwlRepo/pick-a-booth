<!--
  GalleryPage — header (Back pill + "Gallery" + count) and a square-thumbnail grid (dc.html L154-158 landscape, L285-289 portrait).
  Grid: 5 cols landscape / 3 cols portrait, gap 12, tiles radius 22. The Back pill is the layout's ReturnButton,
  hosted in the header via useReturnButtonSlot (it only appears where the layout shows one).
-->
<template>
  <q-page id="gallery-page" class="pb-gallery">
    <header class="pb-gallery__head">
      <div ref="returnSlot" class="pb-gallery__return" />
      <div class="pb-gallery__heading">
        <span class="pb-gallery__title">{{ $t('Gallery') }}</span>
        <span class="pb-gallery__count pb-gallery__count--landscape">{{
          $t('{count} photos · tap one to share', { count: mediacollectionStore.collection_number_of_items })
        }}</span>
        <span class="pb-gallery__count pb-gallery__count--portrait">{{
          $t('{count} photos', { count: mediacollectionStore.collection_number_of_items })
        }}</span>
      </div>
    </header>

    <div v-if="!isGalleryEmpty" class="pb-gallery__grid">
      <q-intersection v-for="item in mediacollectionStore.collection" :key="item.id" once class="pb-gallery__cell">
        <router-link :to="`${$route.path}/mediaviewer/${item.id}`" class="pb-gallery__tile">
          <MediaItemThumbnailViewer :item="item" />
        </router-link>
      </q-intersection>
    </div>
    <!-- eslint-disable-next-line vue/no-v-html -->
    <div v-else v-html="configurationStore.configuration.uisettings.GALLERY_EMPTY_MSG"></div>
  </q-page>
</template>
<script setup lang="ts">
import { computed } from 'vue'
import { useConfigurationStore } from '@/stores/configuration-store'
import { useMediacollectionStore } from '@/stores/mediacollection-store'
import { default as MediaItemThumbnailViewer } from '@/components/MediaItemThumbnailViewer.vue'
import { useReturnButtonSlot } from '@/components/ReturnButton.vue'

const configurationStore = useConfigurationStore()
const mediacollectionStore = useMediacollectionStore()

const returnSlot = useReturnButtonSlot(() => ({ size: 60 }))

const isGalleryEmpty = computed(() => {
  return mediacollectionStore.collection_number_of_items == 0
})
</script>

<style scoped>
.pb-gallery {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 24px;
  color: var(--pb-text);
}

.pb-gallery__head {
  display: flex;
  align-items: center;
  gap: 20px;
  min-height: 60px;
  padding: 0 4px;
}

.pb-gallery__return {
  display: flex;
  flex: none;
}

.pb-gallery__return:empty {
  display: none;
}

.pb-gallery__heading {
  display: flex;
  align-items: baseline;
  gap: 14px;
  min-width: 0;
}

.pb-gallery__title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 36px;
  line-height: 1.1;
}

.pb-gallery__count {
  font-size: 17px;
  font-weight: 600;
  color: var(--pb-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.pb-gallery__count--portrait {
  display: none;
}

.pb-gallery__grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 12px;
  align-content: start;
}

.pb-gallery__cell {
  aspect-ratio: 1 / 1;
}

.pb-gallery__tile {
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 22px;
  background: var(--pb-surface-2);
  color: inherit;
  -webkit-tap-highlight-color: transparent;
}

.pb-gallery__tile:hover {
  transform: scale(1.02);
}

.pb-gallery__tile:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

@media (orientation: portrait) {
  .pb-gallery__grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .pb-gallery__count--landscape {
    display: none;
  }

  .pb-gallery__count--portrait {
    display: inline;
  }
}
</style>
