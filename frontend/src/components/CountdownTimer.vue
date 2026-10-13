<template>
  <!-- countdown ring + step dots, dc.html L74-77 / L227-230; capture message ("Smile!") L84-87 -->
  <div v-show="showBox" id="countdown-timer-container">
    <div class="countdown-timer__ring">
      <PbCountdownRing
        id="countdown-circular-progress"
        v-show="showCountdown"
        :progress="ringProgress"
        :color="showMessage ? 'var(--t2)' : 'var(--t1)'"
        :font-size="showMessage ? 96 : undefined"
      >
        <!-- eslint-disable-next-line vue/no-v-html -->
        <span v-show="showMessage" id="countdown-timer-message" v-html="messageText"></span>
        <span v-show="!showMessage">{{ parseFloat(remainingSeconds.toFixed(0)) }}</span>
      </PbCountdownRing>
    </div>

    <div v-if="stepsTotal > 1" class="countdown-timer__steps">
      <PbStepDots
        :total="stepsTotal"
        :value="stepsActive"
        :color="showMessage ? 'var(--t2)' : 'var(--t1)'"
        :aria-label="$t('Shot {no} of {total}', { no: stepsActive, total: stepsTotal })"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import PbCountdownRing from '@/components/pb/PbCountdownRing.vue'
import PbStepDots from '@/components/pb/PbStepDots.vue'

let intervalTimerId: number
const remainingSeconds = ref(0)
const startDuration = ref(0)

interface Props {
  duration: number
  messageDuration?: number
  messageText?: string
  // multi-capture jobs (collage, ...): total captures and captures already taken; dots hidden when total <= 1
  stepsTotal?: number
  stepsDone?: number
}

const props = withDefaults(defineProps<Props>(), {
  messageDuration: 0.5,
  messageText: '😃',
  stepsTotal: 0,
  stepsDone: 0,
})

const showBox = computed(() => {
  return remainingSeconds.value > 0
})
const showCountdown = computed(() => {
  return remainingSeconds.value > 0
})
const showMessage = computed(() => {
  return remainingSeconds.value <= props.messageDuration
})

// elapsed fraction of the countdown; the ring is full (in t2) during the capture message
const ringProgress = computed(() => {
  if (showMessage.value || startDuration.value <= 0) return 1
  return 1 - remainingSeconds.value / startDuration.value
})

// the shot being taken now counts as active: dots 1..(taken + 1)
const stepsActive = computed(() => Math.min(props.stepsTotal, props.stepsDone + 1))

onMounted(() => {
  startTimer()
})

onBeforeUnmount(() => {
  abortTimer()
})

const abortTimer = () => {
  clearInterval(intervalTimerId)
  remainingSeconds.value = 0
}
const startTimer = () => {
  startDuration.value = props.duration
  remainingSeconds.value = startDuration.value

  console.log(`starting timer, duration=${startDuration.value}`)

  intervalTimerId = window.setInterval(() => {
    remainingSeconds.value -= 0.05

    if (remainingSeconds.value <= 0) {
      clearInterval(intervalTimerId)
    }
  }, 50)
}
</script>

<style lang="css">
#countdown-timer-container {
  position: absolute;
  inset: 0;
  pointer-events: none;
  user-select: none;
}
</style>

<style scoped>
.countdown-timer__ring {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.countdown-timer__steps {
  position: absolute;
  bottom: 28px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
}
</style>
