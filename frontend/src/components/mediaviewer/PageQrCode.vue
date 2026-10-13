<!--
  PageQrCode — QR download card(s) in the result / detail panel (PbQrCard, dc.html L119-121 / L254-256).
  One card per share URL. Title / subtitle come from uisettings.qrcode_text_above / qrcode_text_below;
  the design copy is the fallback when those are empty.
-->
<template>
  <transition v-if="urls?.length > 0" appear enter-active-class="animated fadeIn">
    <div class="pb-qrcode">
      <template v-for="(url, index) in props.urls" :key="index">
        <a v-if="linkQrCodes" :href="url" target="_blank" class="pb-qrcode__link">
          <PbQrCard :value="url" :title="title" :subtitle="subtitle" />
        </a>
        <PbQrCard v-else :value="url" :title="title" :subtitle="subtitle" />
      </template>
    </div>
  </transition>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import PbQrCard from '@/components/pb/PbQrCard.vue'

interface Props {
  urls: string[]
  textAbove?: string
  textBelow?: string
  linkQrCodes?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  linkQrCodes: () => false,
})

const { t } = useI18n()
const title = computed(() => props.textAbove || t('Scan to get your photo'))
const subtitle = computed(() => props.textBelow || t('Point your phone camera here. No app needed.'))
</script>

<style scoped>
.pb-qrcode {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.pb-qrcode__link {
  color: inherit;
  text-decoration: none;
}
</style>
