<!--
  PageCarouselView — swipeable, infinite media carousel with 72px glass chevrons (dc.html L164-165).
  Chevrons sit at the carousel edges; the parent photo card's 20px padding places them 20px from the card edge.
-->
<template>
  <div class="pb-carousel">
    <q-carousel
      ref="carouselRef"
      v-model="currentMediaitemId"
      v-touch-swipe.mouse.down="handleSwipeDown"
      class="pb-carousel__track"
      swipeable
      animated
      draggable="false"
      :arrows="false"
      :infinite="true"
      transition-prev="slide-right"
      transition-next="slide-left"
      @transition="carouselTransition"
    >
      <q-carousel-slide
        v-for="slide in props.slicedImages"
        :key="slide.id"
        :name="slide.id"
        class="pb-carousel__slide column no-wrap flex-center full-height"
      >
        <MediaItemPreviewViewer :item="slide" />
      </q-carousel-slide>
    </q-carousel>

    <template v-if="props.slicedImages.length > 1">
      <PbRoundButton
        class="pb-carousel__chevron pb-carousel__chevron--prev"
        icon="chevron-left"
        :label="$t('Previous')"
        @click="carouselRef?.previous()"
      />
      <PbRoundButton class="pb-carousel__chevron pb-carousel__chevron--next" icon="chevron-right" :label="$t('Next')" @click="carouselRef?.next()" />
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref, toRef, watch } from 'vue'
import type { QCarousel } from 'quasar'
import type { components } from '@/dto/api'

import { default as MediaItemPreviewViewer } from '../MediaItemPreviewViewer.vue'
import PbRoundButton from '@/components/pb/PbRoundButton.vue'

const props = defineProps<{
  slicedImages: components['schemas']['MediaitemPublic'][]
  mediaitemId: string // warning: if invalid ID is given, there is just shown nothing...
}>()

const carouselRef = ref<QCarousel | null>(null)

const currentMediaitemId = toRef(props.mediaitemId)
// update currentSlide if changed externally, so slide can be updated
watch(
  () => props.mediaitemId,
  mediaitemId => {
    currentMediaitemId.value = mediaitemId
  }
)

const emit = defineEmits<{
  triggerChangedItem: [id: string | number]
}>()

function handleSwipeDown() {
  console.log('TODO: add method to close dialog programmatically')
}

function carouselTransition(newval: string | number) {
  emit('triggerChangedItem', newval)
}
</script>

<style scoped>
.pb-carousel {
  position: relative;
  width: 100%;
  height: 100%;
}

.pb-carousel__track {
  width: 100%;
  height: 100%;
  background: transparent;
}

.pb-carousel__slide {
  padding: 0;
  background: transparent;
}

.pb-carousel__chevron {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
}

.pb-carousel__chevron:active:not(:disabled) {
  transform: translateY(-50%) scale(0.95);
}

.pb-carousel__chevron--prev {
  left: 0;
}

.pb-carousel__chevron--next {
  right: 0;
}
</style>
