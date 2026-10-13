<!--
  SlideshowPage — full-bleed random slideshow with a bottom glass bar (dc.html L180-183 landscape, L294-297 portrait).
  Bar: event name (uisettings.FRONTPAGE_TEXT) + subline; "Tap to take your own" (t1) returns to the booth start screen.
  The button shows only on the booth's own standby route (meta.standbyMode); standalone slideshows on secondary
  devices must not navigate into the booth. The layout's Back pill is hidden here: the bar button replaces it.
-->
<template>
  <q-page id="slideshow-page" class="pb-slideshow absolute-full">
    <div v-if="mediacollectionStore.collection_number_of_items > 0" class="pb-slideshow__media">
      <MediaItemPreviewViewer :item="mediacollectionStore.collection[currentMediaitemIndex]" fit="cover" />
    </div>
    <div v-else class="full-height"><ItemNotAvailableError /></div>

    <div class="pb-slideshow__bar">
      <div class="pb-slideshow__text">
        <span class="pb-slideshow__name">{{ frontpageText }}</span>
        <span class="pb-slideshow__sub">{{ $t('The booth is open — come say cheese.') }}</span>
      </div>
      <PbBigButton
        v-if="route.meta.standbyMode === true"
        class="pb-slideshow__cta"
        :height="96"
        :icon-size="30"
        :font-size="26"
        padding="0 36px"
        icon="hand"
        bg="var(--t1)"
        fg="var(--t1i)"
        @click="router.push('/')"
      >
        {{ $t('Tap to take your own') }}
      </PbBigButton>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { computed, onMounted, onBeforeUnmount, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useConfigurationStore } from '@/stores/configuration-store'
import { useMediacollectionStore } from '@/stores/mediacollection-store'
import { default as MediaItemPreviewViewer } from '@/components/MediaItemPreviewViewer.vue'
import ItemNotAvailableError from '@/components/ItemNotAvailableError.vue'
import PbBigButton from '@/components/pb/PbBigButton.vue'
import { useReturnButtonSlot } from '@/components/ReturnButton.vue'
import { plainText } from '@/theme/text'

const route = useRoute()
const router = useRouter()
const configurationStore = useConfigurationStore()
const mediacollectionStore = useMediacollectionStore()
const nextMediaitemTimeout = 5_000
const currentMediaitemIndex = ref(0)
const frontpageText = computed(() => plainText(configurationStore.configuration.uisettings.FRONTPAGE_TEXT))

useReturnButtonSlot(() => ({ hidden: true }))

let intervalTimerId: number

// functions
function handleTimeout() {
  loadNextImage()
  clearTimeout(intervalTimerId)
  startTimer()
}

function startTimer() {
  intervalTimerId = window.setInterval(handleTimeout, nextMediaitemTimeout)
}
function loadNextImage() {
  currentMediaitemIndex.value = Math.floor(Math.random() * mediacollectionStore.collection_number_of_items)
}
onMounted(() => {
  startTimer()
})

onBeforeUnmount(() => {
  clearInterval(intervalTimerId)
})
</script>

<style scoped>
.pb-slideshow {
  overflow: hidden;
  background: var(--pb-bg);
  color: var(--pb-text);
}

.pb-slideshow__media {
  position: absolute;
  inset: 0;
}

.pb-slideshow__bar {
  position: absolute;
  left: 24px;
  right: 24px;
  bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 22px 22px 22px 32px;
  border-radius: 32px;
  background: var(--pb-glass-bg);
  backdrop-filter: blur(var(--pb-glass-blur));
  -webkit-backdrop-filter: blur(var(--pb-glass-blur));
  border: var(--pb-glass-border);
}

.pb-slideshow__text {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
}

.pb-slideshow__name {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 36px;
  line-height: 1.05;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pb-slideshow__sub {
  font-size: 17px;
  font-weight: 600;
  color: var(--pb-muted-2);
}

@media (orientation: portrait) {
  .pb-slideshow__bar {
    flex-direction: column;
    align-items: stretch;
    gap: 18px;
  }

  .pb-slideshow__name {
    font-size: 40px;
  }

  .pb-slideshow__cta {
    width: 100%;
  }
}
</style>
