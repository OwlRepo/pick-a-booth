<template>
  <!-- collage shot approval, dc.html L97-103 (landscape) / L240-245 (portrait) -->
  <div id="itemapproval-dialog" class="approval">
    <div class="approval__photo">
      <q-img
        v-if="showImage"
        class="approval__image"
        :draggable="false"
        loading="eager"
        :src="`/api/processing/approval/${approval_id}`"
        fit="cover"
        position="50% 40%"
        @error="showImage = false"
        loading-show-delay="800"
      />

      <!-- video approval not yet supported -->

      <ItemNotAvailableError v-else />

      <div class="approval__abort">
        <PbPill id="layout-button-back" variant="glass" :size="52" icon="x" @click="userAbort()">{{ $t('Stop collage') }}</PbPill>
      </div>
    </div>

    <div class="approval__panel">
      <div class="approval__head">
        <div class="approval__progress">
          <div class="approval__shot">{{ $t('Shot {no} of {total}', { no: number_captures_taken, total: total_captures_to_take }) }}</div>
          <PbStepDots :total="total_captures_to_take" :value="number_captures_taken" color="var(--t2)" />
        </div>
        <div class="approval__title">{{ $t('Keep this one?') }}</div>
      </div>

      <div class="approval__spacer"></div>

      <div class="approval__actions">
        <PbBigButton
          id="item-approval-button-reject"
          :height="isPortrait ? 120 : 96"
          bordered
          icon="rotate-ccw"
          :icon-size="28"
          :font-size="24"
          block
          @click="userReject()"
        >
          {{ $t('Try again') }}
        </PbBigButton>
        <PbBigButton
          id="item-approval-button-approve"
          :height="isPortrait ? 120 : 124"
          bg="var(--t5)"
          fg="var(--t5i)"
          icon="check"
          :icon-size="isPortrait ? 32 : 35"
          :font-size="isPortrait ? 28 : 30"
          block
          @click="userConfirm()"
        >
          {{ $t('MSG_APPROVE_COLLAGE_ITEM_APPROVE') }}
        </PbBigButton>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue'
import { remoteProcedureCall } from '@/util/fetch_api.js'
import ItemNotAvailableError from '@/components/ItemNotAvailableError.vue'
import PbBigButton from '@/components/pb/PbBigButton.vue'
import PbPill from '@/components/pb/PbPill.vue'
import PbStepDots from '@/components/pb/PbStepDots.vue'
import { useIsPortrait } from '@/components/pb/orientation'

defineProps<{
  approval_id: string
  number_captures_taken: number
  total_captures_to_take: number
}>()

const isPortrait = useIsPortrait(() => 'auto')
const showImage = ref(true)

onBeforeMount(() => {
  showImage.value = true
})

const userConfirm = () => {
  remoteProcedureCall('/api/processing/confirm')
}
const userReject = () => {
  remoteProcedureCall('/api/processing/reject')
}
const userAbort = () => {
  remoteProcedureCall('/api/processing/abort')
}
</script>

<style scoped>
.approval {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: var(--pb-bg);
  display: grid;
  grid-template-columns: minmax(0, 1fr) 400px;
  gap: 20px;
  padding: 24px;
}

.approval__photo {
  position: relative;
  border-radius: 32px;
  overflow: hidden;
  background: var(--pb-surface-1);
}

.approval__image {
  width: 100%;
  height: 100%;
}

.approval__abort {
  position: absolute;
  top: 18px;
  left: 18px;
}

.approval__panel {
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding: 28px;
  border-radius: 32px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
}

.approval__head,
.approval__progress {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.approval__shot {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--pb-muted);
}

.approval__title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 42px;
  line-height: 1.05;
}

.approval__spacer {
  flex: 1;
}

.approval__actions {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

@media (orientation: portrait) {
  .approval {
    grid-template-columns: minmax(0, 1fr);
    grid-template-rows: minmax(0, 1fr) auto;
    gap: 18px;
  }

  .approval__panel {
    gap: 16px;
  }

  .approval__head {
    flex-direction: row-reverse;
    align-items: center;
    justify-content: space-between;
  }

  .approval__progress {
    align-items: flex-end;
    gap: 8px;
  }

  .approval__shot {
    font-size: 13px;
  }

  .approval__title {
    font-size: 38px;
    line-height: normal;
  }

  .approval__spacer {
    display: none;
  }

  .approval__actions {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1.4fr);
    gap: 14px;
  }
}
</style>
