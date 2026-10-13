<!--
  HeaderCountdownTimer — auto-return countdown, rendered as the v2 auto-return bar (PbAutoReturnBar, dc.html L118 / L253).
  Props:
    duration: number    seconds until `triggerTimeout`
    left?: string       left caption, e.g. "Photo 12 of 48"
  Emits: triggerTimeout (once, when the countdown reaches 0). Ticks every 100ms; fill = remaining / duration.
-->
<template>
  <PbAutoReturnBar
    v-if="remainingSeconds >= 0"
    id="gallery-linear-progress-bar"
    :progress="props.duration > 0 ? remainingSeconds / props.duration : 0"
    :left="props.left"
    :right="$t('Back to start in {s}s', { s: Math.max(0, Math.ceil(remainingSeconds)) })"
  />
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import PbAutoReturnBar from '@/components/pb/PbAutoReturnBar.vue'

const props = defineProps<{
  duration: number
  left?: string
}>()

const remainingSeconds = ref(0)
let intervalTimerId: number

const emit = defineEmits<{
  triggerTimeout: []
}>()

// functions
function abortTimer() {
  clearInterval(intervalTimerId)
  remainingSeconds.value = 0
}
function startTimer() {
  remainingSeconds.value = props.duration

  intervalTimerId = window.setInterval(() => {
    remainingSeconds.value -= 0.1

    if (remainingSeconds.value <= 0) {
      clearInterval(intervalTimerId)
      emit('triggerTimeout') //TODO: this.$router.push({ path: '/' })
    }
  }, 100)
}

onMounted(() => {
  startTimer()
})

onBeforeUnmount(() => {
  abortTimer()
})
</script>
