<!--
  PbQrCard — QR download card (dc.html L119-121 landscape, L254-256 portrait).
  Props:
    value: string                QR payload (download URL)
    title?: string               Sora 600 23px line, e.g. uisettings.qrcode_text_above (or #title slot)
    subtitle?: string            muted 15px line, e.g. uisettings.qrcode_text_below (or #subtitle slot)
    orientation?: 'auto' | 'landscape' | 'portrait' = 'auto'
                                 white QR plate 118px (landscape) / 120px (portrait); 'auto' follows the media query
  The QR plate is role="img" labelled by `title` (the slot content cannot label it; pass `title` for a11y).
  Card: surface-2, radius 24, padding 18, line border; plate radius 16, padding 8.
-->
<template>
  <div class="pb-qr-card">
    <div class="pb-qr-card__plate" role="img" :aria-label="title" :style="{ width: `${plate}px`, height: `${plate}px` }">
      <qrcode-vue class="pb-qr-card__code" :value="value" :size="plate - 16" :margin="2" level="L" render-as="svg" />
    </div>
    <div class="pb-qr-card__text">
      <div v-if="title || $slots.title" class="pb-qr-card__title">
        <slot name="title">{{ title }}</slot>
      </div>
      <div v-if="subtitle || $slots.subtitle" class="pb-qr-card__subtitle">
        <slot name="subtitle">{{ subtitle }}</slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import QrcodeVue from 'qrcode.vue'
import { useIsPortrait, type PbOrientation } from './orientation'

const {
  value,
  title,
  subtitle,
  orientation = 'auto',
} = defineProps<{
  value: string
  title?: string
  subtitle?: string
  orientation?: PbOrientation
}>()

const isPortrait = useIsPortrait(() => orientation)
const plate = computed(() => (isPortrait.value ? 120 : 118))
</script>

<style scoped>
.pb-qr-card {
  display: flex;
  gap: 20px;
  align-items: center;
  padding: 18px;
  border-radius: 24px;
  background: var(--pb-surface-2);
  border: var(--pb-line);
}

.pb-qr-card__plate {
  flex: none;
  background: #fff;
  border-radius: 16px;
  padding: 8px;
}

.pb-qr-card__code {
  display: block;
  width: 100%;
  height: 100%;
}

.pb-qr-card__text {
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 0;
}

.pb-qr-card__title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 23px;
  line-height: 1.1;
}

.pb-qr-card__subtitle {
  font-size: 15px;
  color: var(--pb-muted);
  line-height: 1.4;
}
</style>
