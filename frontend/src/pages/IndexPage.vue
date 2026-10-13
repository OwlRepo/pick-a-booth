<template>
  <q-page id="index-page" class="pb-index">
    <!--
      one frame for all states so the camera card (and its PreviewStream) is never remounted:
      idle = top bar / camera card / mode tiles (dc.html L37-67, L191-220);
      countdown + recording = camera card inset 24 (dc.html L72, L108, L225)
    -->
    <div class="pb-index__frame" :class="{ 'pb-index__frame--idle': stateStore.isStateIdle }">
      <div v-if="stateStore.isStateIdle" class="pb-index__topbar">
        <div class="pb-index__title">
          <div id="frontpage_text" class="pb-index__event">{{ frontpageText }}</div>
          <div class="pb-index__subline">{{ $t("Pick a mode and tap — that's it.") }}</div>
        </div>
        <div class="pb-index__topbar-actions">
          <PbPill
            v-if="configurationStore.configuration.uisettings.show_gallery_on_frontpage"
            id="frontpage-button-to-gallery"
            :size="60"
            icon="images"
            @click="router.push('/gallery')"
          >
            {{ $t('BTN_LABEL_MAINPAGE_TO_GALLERY') }}
          </PbPill>
          <PbRoundButton
            v-if="configurationStore.configuration.uisettings.show_admin_on_frontpage"
            id="frontpage-button-to-admin"
            :label="$t('BTN_LABEL_MAINPAGE_TO_ADMIN')"
            icon="lock"
            :size="60"
            variant="muted"
            class="action-button-admin"
            :class="{ 'action-button-admin-invisible': adminButtonInvisible }"
            :invisible="adminButtonInvisible"
            @click="onBtnAdminClick"
          />
        </div>
      </div>

      <div class="pb-index__camera">
        <preview-stream
          v-if="showPreviewThrottled"
          :index_device="configurationStore.configuration.cameras.index_backend_video"
          :frame-overlay="frameOverlay"
          :fixed-size="fixedSize"
          :enable-blurred-background-stream="configurationStore.configuration.uisettings.livestream_blurredbackground"
          :enable-mirror-effect-stream="configurationStore.configuration.uisettings.livestream_mirror_effect"
          :blurredbackground-high-framerate="configurationStore.configuration.uisettings.livestream_blurredbackground_high_framerate"
        ></preview-stream>

        <div v-if="stateStore.isStateIdle && showPreviewThrottled" class="pb-index__live">
          <PbPill tag="div" variant="glass" :size="40" dot="var(--pb-live)">{{ $t('Live') }}</PbPill>
        </div>

        <!-- layer display the countdown timer -->
        <div v-if="stateStore.isStateCountdown" id="frontpage-countdown" class="pb-index__countdown">
          <div class="pb-index__lookup">
            <PbPill tag="div" variant="glass" :size="60" icon="arrow-up">{{ $t('Look up at the camera') }}</PbPill>
          </div>
          <countdown-timer
            ref="countdowntimer"
            :duration="stateStore.jobmodel.duration"
            :message-duration="configurationStore.configuration.uisettings.TAKEPIC_MSG_TIME"
            :message-text="configurationStore.configuration.uisettings.TAKEPIC_MSG_TEXT"
            :steps-total="stateStore.jobmodel.total_captures_to_take"
            :steps-done="stateStore.jobmodel.number_captures_taken"
          ></countdown-timer>
        </div>

        <!-- video state controls, dc.html L109-110 -->
        <div v-if="stateStore.isStateRecording" id="frontpage-indicator-recording" class="pb-index__rec">
          <PbPill tag="div" variant="glass" :size="56" dot="var(--t1)" dot-blink>
            <span class="pb-index__rec-label">{{ $t('REC') }} {{ recordingElapsedLabel }}</span>
          </PbPill>
        </div>
        <div v-if="stateStore.isStateRecording" id="frontpage-indicator-stop-recording" class="pb-index__stop">
          <PbBigButton :height="104" pill padding="0 48px" bg="var(--t1)" fg="var(--t1i)" :font-size="30" @click="stopRecordingVideo()">
            <template #icon><PbStopSquare :size="35" /></template>
            {{ $t('Stop recording') }}
          </PbBigButton>
        </div>
      </div>

      <FrontpageTriggerButtons v-if="stateStore.isStateIdle" :triggers="triggerButtons" @trigger-action="invokeAction"></FrontpageTriggerButtons>
    </div>

    <!-- layer display processing spinner grid to show user computer working hard, dc.html L92 / L235 -->
    <div v-if="stateStore.isStateProcessing" class="pb-index__processing" role="status">
      <PbSpinner />
      <div class="pb-index__processing-text">
        <div class="pb-index__processing-title">{{ $t('Almost there…') }}</div>
        <div class="pb-index__processing-sub">{{ $t('Your photo is being made. It will pop up right here.') }}</div>
      </div>
    </div>

    <!-- dialog for approval -->
    <div v-if="stateStore.isStateApproval && stateStore.jobmodel.approval_id">
      <MediaItemApprovalViewer
        :approval_id="stateStore.jobmodel.approval_id"
        :number_captures_taken="stateStore.jobmodel.number_captures_taken"
        :total_captures_to_take="stateStore.jobmodel.total_captures_to_take"
      >
      </MediaItemApprovalViewer>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { watchDebounced, refThrottled } from '@vueuse/core'
import { computed, onBeforeUnmount, ref, watch } from 'vue'
import { remoteProcedureCall } from '@/util/fetch_api.js'
import { useMainStore } from '@/stores/main-store'
import { useStateStore } from '@/stores/state-store'
import { useConfigurationStore } from '@/stores/configuration-store'
import CountdownTimer from '@/components/CountdownTimer.vue'
import type { TriggerSchema } from '@/types/trigger-schema'
import { default as FrontpageTriggerButtons } from '@/components/FrontpageTriggerButtons.vue'
import { default as PreviewStream } from '@/components/PreviewStream.vue'
import MediaItemApprovalViewer from '@/components/MediaItemApprovalViewer.vue'
import PbBigButton from '@/components/pb/PbBigButton.vue'
import PbPill from '@/components/pb/PbPill.vue'
import PbRoundButton from '@/components/pb/PbRoundButton.vue'
import PbSpinner from '@/components/pb/PbSpinner.vue'
import PbStopSquare from '@/components/pb/PbStopSquare.vue'
import type { components } from '@/dto/api'
import type { Size2D } from '@/util/streamRenderer.ts'
import { plainText } from '@/theme/text'
const mainStore = useMainStore()
const stateStore = useStateStore()
const configurationStore = useConfigurationStore()
const router = useRouter()
const btnAdminClickCounter = ref(0)

watchDebounced(
  btnAdminClickCounter,
  () => {
    if (btnAdminClickCounter.value >= 5) {
      router.push('/admin')
    }
    btnAdminClickCounter.value = 0
  },
  { debounce: 500 }
)
const triggerButtons = computed(() => {
  const result: TriggerSchema[] = []

  Object.entries(configurationStore.configuration.actions).forEach(([key, actions]) => {
    actions.forEach((action, index: number) => {
      const trigger: TriggerSchema = {
        action: `actions/${key}`,
        config_index: index,
        show_button: action.trigger.ui_trigger.show_button,
        title: action.trigger.ui_trigger.title,
        icon: action.trigger.ui_trigger.icon,
        use_custom_color: action.trigger.ui_trigger.use_custom_color,
        custom_color: action.trigger.ui_trigger.custom_color,
      }

      result.push(trigger)
    })
  })

  return result
})

const frontpageText = computed(() => plainText(configurationStore.configuration.uisettings.FRONTPAGE_TEXT))

const adminButtonInvisible = computed(() => {
  return configurationStore.configuration.uisettings.admin_button_invisible
})

const showPreview = computed(() => {
  const enabledWhenIdle = configurationStore.configuration.uisettings.enable_livestream_when_idle
  const enabledWhenActive = configurationStore.configuration.uisettings.enable_livestream_when_active
  const machineIdle = stateStore.isStateIdle
  const machineRecord = stateStore.isStateRecording
  const machineCounting = stateStore.isStateCountdown
  const machineCapture = stateStore.isStateCapture

  // allow user to choose if shown during idle or process only. during record it cannot be disabled because video useful to show while recording
  return (machineIdle && enabledWhenIdle) || ((machineCounting || machineCapture) && enabledWhenActive) || machineRecord
})
// following is to avoid short time preview requested. there is a race condition when the state machine finishes and short time target is present.
// right after present it changes to finished and so the route is changed to presenter + the preview component is enabled which causes issues because
// just a moment later it's disabled again.
const showPreviewThrottled = refThrottled(showPreview, 500)

const fixedSize = computed((): Size2D | null => {
  console.log('fixedSize determined:')
  console.info(stateStore.jobmodel)
  const captureDefinition = stateStore.jobmodel.captures_definition

  if (captureDefinition) {
    return {
      width: captureDefinition.width,
      height: captureDefinition.height,
    }
  } else {
    return null
  }
})
const frameOverlay = computed((): components['schemas']['UiFrameOverlay'] | null => {
  const idleFrameOverlay = configurationStore.configuration.uisettings.livestream_frameoverlay
  const actionFrameOverlay = stateStore.jobmodel.frame_overlay

  if (stateStore.isStateCountdown && actionFrameOverlay) {
    //during countdown the action frame is priorized if the action has this feature...
    return actionFrameOverlay
  } else if (stateStore.isStateIdle && idleFrameOverlay.enable && idleFrameOverlay.image) {
    // the live frame is shown in idle only
    return idleFrameOverlay as components['schemas']['UiFrameOverlay']
  } else {
    return null
  }
})

// REC timer: display-only client clock, starts when isStateRecording turns true
const recordingElapsedSeconds = ref(0)
let recordingTimerId: number | undefined
const stopRecordingClock = () => {
  window.clearInterval(recordingTimerId)
  recordingTimerId = undefined
}
watch(
  () => stateStore.isStateRecording,
  recording => {
    stopRecordingClock()
    recordingElapsedSeconds.value = 0
    if (recording) {
      const startedAt = Date.now()
      recordingTimerId = window.setInterval(() => {
        recordingElapsedSeconds.value = Math.floor((Date.now() - startedAt) / 1000)
      }, 250)
    }
  },
  { immediate: true }
)
onBeforeUnmount(stopRecordingClock)
const recordingElapsedLabel = computed(() => {
  const seconds = recordingElapsedSeconds.value
  return `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, '0')}`
})

const onBtnAdminClick = () => {
  if (adminButtonInvisible.value) {
    btnAdminClickCounter.value++
  } else {
    router.push('/admin')
  }
}
const invokeAction = (trigger: TriggerSchema) => {
  mainStore.lastAction = trigger // save last action so it can be started from itempresenter directly again.
  remoteProcedureCall(`/api/${trigger.action}/${trigger.config_index}`)
}
const stopRecordingVideo = () => {
  remoteProcedureCall('/api/processing/next')
}
</script>

<style scoped>
.pb-index {
  position: relative;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  background: var(--pb-bg);
  color: var(--pb-text);
}

.pb-index__frame {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-rows: minmax(0, 1fr);
  gap: 18px;
  padding: 24px;
}

.pb-index__frame--idle {
  grid-template-rows: 64px minmax(0, 1fr) 196px;
}

.pb-index__topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 0 4px;
}

.pb-index__title {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}

.pb-index__event {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 34px;
  line-height: 1.05;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pb-index__subline {
  font-size: 16px;
  font-weight: 600;
  color: var(--pb-muted);
}

.pb-index__topbar-actions {
  display: flex;
  gap: 12px;
}

.pb-index__camera {
  position: relative;
  border-radius: 32px;
  overflow: hidden;
  background: var(--pb-surface-1);
}

.pb-index__live {
  position: absolute;
  top: 18px;
  left: 18px;
}

.pb-index__countdown {
  position: absolute;
  inset: 0;
  background: rgba(10, 11, 16, 0.25);
}

.pb-index__lookup {
  position: absolute;
  top: 24px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  pointer-events: none;
}

.pb-index__rec {
  position: absolute;
  top: 24px;
  right: 24px;
}

.pb-index__rec-label {
  font-weight: 800;
  font-size: 20px;
  font-variant-numeric: tabular-nums;
}

.pb-index__stop {
  position: absolute;
  bottom: 28px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  pointer-events: none;
}

.pb-index__stop > * {
  pointer-events: auto;
}

.pb-index__processing {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: var(--pb-bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 44px;
  text-align: center;
  padding: 40px;
}

.pb-index__processing-text {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
}

.pb-index__processing-title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 84px;
  line-height: 1;
}

.pb-index__processing-sub {
  font-size: 22px;
  font-weight: 600;
  color: var(--pb-muted);
  max-width: 520px;
  text-wrap: pretty;
}

@media (orientation: portrait) {
  .pb-index__frame--idle {
    grid-template-rows: auto minmax(0, 1fr) 380px;
  }

  .pb-index__event {
    font-size: 36px;
  }

  .pb-index__processing-title {
    font-size: 76px;
  }
}
</style>
