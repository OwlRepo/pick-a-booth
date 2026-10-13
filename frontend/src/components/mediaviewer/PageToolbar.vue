<!--
  PageToolbar — the result / detail side panel (dc.html L116-125 result L, L252-258 result P, L165-173 detail L).
  Slots:
    head     left part of the header row (title, or the Back pill host); the "N of M" counter renders on the right
             when image_number and images_total are given
    default  panel content between header and actions (auto-return bar, QR card)
  Actions: configured share buttons, ghost row (Save / Filter / Delete), "Take one more!" (last action again).
  Landscape: share buttons in a 2-col row, ghost buttons in their own row. Portrait: one 4-col grid for both.
-->
<template>
  <section v-if="item" id="gallery-toolbar" class="pb-toolbar">
    <div class="pb-toolbar__head">
      <slot name="head" />
      <span v-if="props.image_number && props.images_total" class="pb-toolbar__counter">
        {{
          $t('LABEL_ELEMENT_X_OF_Y', {
            no: props.image_number,
            total: props.images_total,
          })
        }}
      </span>
    </div>

    <slot />

    <div class="pb-toolbar__spacer" />

    <div class="pb-toolbar__actions">
      <div v-if="showShare && visibleShareCount > 0" class="pb-toolbar__shares" :style="{ '--pb-share-cols': Math.min(visibleShareCount, 2) }">
        <ShareTriggerButtons :triggers="shareButtons" :current-item-is-image="isPrintableImage(item.processed)" @trigger-action="invokeShareAction" />
      </div>

      <div v-if="ghostCount > 0" class="pb-toolbar__ghosts" :style="{ '--pb-ghost-cols': ghostCount }">
        <PbGhostButton v-if="showDownload" class="action-button-download" icon="download" @click="openURL(`/sharepage/#?url=/media/full/${item.id}`)">
          {{ $t('BTN_LABEL_GALLERY_DOWNLOAD') }}
        </PbGhostButton>
        <PbGhostButton v-if="showFilter && enableFilter" class="action-button-filter" icon="sparkles" @click="invokeToggleDisplayFilter">
          {{ $t('BTN_LABEL_GALLERY_FILTER') }}
        </PbGhostButton>
        <PbGhostButton v-if="showDelete" class="action-button-delete" icon="trash" @click="confirmDeleteDialog = true">
          {{ $t('BTN_LABEL_GALLERY_DELETE') }}
        </PbGhostButton>
      </div>
    </div>

    <PbBigButton
      v-if="lastActionTriggerButton"
      block
      class="action-button pb-toolbar__again"
      :height="isPortrait ? 112 : 108"
      :icon-size="isPortrait ? 37 : 35"
      :font-size="isPortrait ? 32 : 30"
      :icon="lastActionTriggerButton.icon || 'camera'"
      :bg="againColor.bg"
      :fg="againColor.fg"
      @click="invokeAction(lastActionTriggerButton)"
    >
      {{ lastActionTriggerButton.title }}
    </PbBigButton>
  </section>

  <q-dialog v-model="confirmDeleteDialog" class="pb-dialog" backdrop-filter="blur(6px)">
    <div id="gallery-confirm-delete-dialog" class="pb-confirm">
      <div class="pb-confirm__head">
        <span class="pb-confirm__icon"><PbIcon name="trash" :size="24" /></span>
        <span class="pb-confirm__title">{{ $t('MSG_CONFIRM_DELETE_IMAGE') }}</span>
      </div>
      <div class="pb-confirm__actions">
        <PbGhostButton v-close-popup>{{ $t('BTN_LABEL_CANCEL') }}</PbGhostButton>
        <PbBigButton
          v-close-popup
          block
          :height="72"
          :font-size="22"
          :icon-size="24"
          icon="trash"
          bg="var(--t1)"
          fg="var(--t1i)"
          @click="[invokeDeleteMediaitem(item.id), $emit('closeEvent')]"
        >
          {{ $t('BTN_LABEL_DELETE_IMAGE') }}
        </PbBigButton>
      </div>
    </div>
  </q-dialog>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { openURL } from 'quasar'
import { isEmpty } from 'lodash'
import { default as ShareTriggerButtons, type ShareSchema } from '../ShareTriggerButtons.vue'
import PbBigButton from '@/components/pb/PbBigButton.vue'
import PbGhostButton from '@/components/pb/PbGhostButton.vue'
import PbIcon from '@/components/pb/PbIcon.vue'
import { useIsPortrait } from '@/components/pb/orientation'
import { tileColor } from '@/theme/palette'
import type { TriggerSchema } from '@/types/trigger-schema'
import type { components } from '@/dto/api'
import { isPrintableImage } from '@/util/media_is_type'

const confirmDeleteDialog = ref(false)

const props = defineProps<{
  item: components['schemas']['MediaitemPublic']
  image_number?: number
  images_total?: number
  showDownload: boolean
  showDelete: boolean
  showFilter: boolean
  showShare: boolean
  shareButtons: ShareSchema[]
  enableFilter: boolean
  lastActionTriggerButton: TriggerSchema | null
}>()

const emit = defineEmits<{
  triggerShareAction: [config_index: number]
  triggerToggleDisplayFilter: []
  triggerDeleteMediaitem: [id: string]
  triggerAction: [trigger: TriggerSchema]
  closeEvent: [] // from quasar
}>()

const isPortrait = useIsPortrait(() => 'auto')

// same visibility filter as ShareTriggerButtons, to size the share row
const visibleShareCount = computed(() => props.shareButtons.filter(t => t.show_button && !(isEmpty(t.title) && isEmpty(t.icon))).length)
const ghostCount = computed(() => [props.showDownload, props.showFilter && props.enableFilter, props.showDelete].filter(Boolean).length)
// "Take one more!" is t1 by default (dc.html L125); the action's custom colour still wins, as on the start screen
const againColor = computed(() =>
  props.lastActionTriggerButton ? tileColor(props.lastActionTriggerButton, 0) : { bg: 'var(--t1)', fg: 'var(--t1i)' }
)

function invokeShareAction(config_index: number) {
  emit('triggerShareAction', config_index)
}

function invokeToggleDisplayFilter() {
  emit('triggerToggleDisplayFilter')
}

function invokeDeleteMediaitem(id: string) {
  emit('triggerDeleteMediaitem', id)
}

function invokeAction(trigger: TriggerSchema) {
  emit('triggerAction', trigger)
}
</script>

<style scoped>
.pb-toolbar {
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-width: 0;
  min-height: 0;
  padding: 24px;
  border-radius: 32px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  color: var(--pb-text);
  overflow-y: auto;
}

.pb-toolbar__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 52px;
}

.pb-toolbar__counter {
  font-size: 14px;
  font-weight: 600;
  color: var(--pb-muted);
  white-space: nowrap;
}

.pb-toolbar__spacer {
  flex: 1;
}

.pb-toolbar__actions {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.pb-toolbar__shares {
  display: grid;
  grid-template-columns: repeat(var(--pb-share-cols), minmax(0, 1fr));
  gap: 12px;
}

.pb-toolbar__ghosts {
  display: grid;
  grid-template-columns: repeat(var(--pb-ghost-cols), minmax(0, 1fr));
  gap: 12px;
}

.pb-confirm {
  width: 620px;
  max-width: 100%;
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding: 32px;
  border-radius: 36px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
  box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
  color: var(--pb-text);
}

.pb-confirm__head {
  display: flex;
  align-items: center;
  gap: 14px;
}

.pb-confirm__icon {
  flex: none;
  width: 52px;
  height: 52px;
  border-radius: 999px;
  background: var(--t1);
  color: var(--t1i);
  display: flex;
  align-items: center;
  justify-content: center;
}

.pb-confirm__title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 26px;
  line-height: 1.15;
}

.pb-confirm__actions {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

@media (orientation: portrait) {
  .pb-toolbar {
    overflow-y: visible;
  }

  .pb-toolbar__spacer {
    display: none;
  }

  /* dc.html L257: shares and ghost buttons share one 4-col row */
  .pb-toolbar__actions {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 12px;
  }

  .pb-toolbar__shares,
  .pb-toolbar__ghosts {
    display: contents;
  }

  .pb-confirm {
    width: 680px;
  }
}
</style>
