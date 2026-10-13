<!--
  ReturnButton — the layout-owned Back pill (MainLayout / StandaloneLayout decide whether it exists and handle `triggerReturn`).
  Props:
    icon?: string = 'sym_o_arrow_back_ios_new'   PbIcon name (maps to Lucide arrow-left)
  Emits: triggerReturn
  Placement: by default a 60px solid pill pinned top-left (inset 24). A page can host it inside its own layout instead
  (gallery header, result panel) or hide it, via useReturnButtonSlot() exported below; behaviour and emit stay the same.
-->
<template>
  <Teleport v-if="hostSlot && hostSlot.target" :to="hostSlot.target">
    <PbPill id="layout-button-back" :size="slotOptions.size ?? 60" :icon="slotOptions.icon ?? icon" @click="emit('triggerReturn')">
      {{ slotOptions.label ?? t('BTN_LABEL_BACK') }}
    </PbPill>
  </Teleport>
  <q-page-sticky v-else-if="!slotOptions.hidden" position="top-left" :offset="[24, 24]">
    <PbPill id="layout-button-back" :size="60" :icon="icon" @click="emit('triggerReturn')">{{ t('BTN_LABEL_BACK') }}</PbPill>
  </q-page-sticky>
</template>

<script lang="ts">
import { useI18n } from 'vue-i18n'
import { computed, onBeforeUnmount, shallowRef, watch, type Ref } from 'vue'

export interface ReturnButtonSlotOptions {
  /** hide the layout's Back pill entirely (e.g. the slideshow, which has its own exit button) */
  hidden?: boolean
  /** label override, e.g. "Done" on the result screen; default BTN_LABEL_BACK */
  label?: string
  /** PbIcon name override, e.g. 'check' */
  icon?: string
  /** pill height inside the host element (PbPill sizes); default 60 */
  size?: 60 | 56 | 52 | 40
}

interface ReturnButtonSlot {
  owner: symbol
  target: HTMLElement | null
  options: () => ReturnButtonSlotOptions
}

// One page is mounted at a time below a layout, so a single module-level slot is enough.
const activeSlot = shallowRef<ReturnButtonSlot | null>(null)

/**
 * Let the current page host the layout's Back pill (teleported into the element bound to the returned ref) or hide it.
 * The layout still decides whether a Back pill exists at all and what it does; the page only decides where it sits.
 */
export function useReturnButtonSlot(options: () => ReturnButtonSlotOptions = () => ({})): Ref<HTMLElement | null> {
  const owner = Symbol('return-button-slot')
  const target = shallowRef<HTMLElement | null>(null)

  watch(
    target,
    el => {
      activeSlot.value = { owner, target: el, options }
    },
    { immediate: true }
  )
  onBeforeUnmount(() => {
    if (activeSlot.value?.owner === owner) activeSlot.value = null
  })

  return target
}
</script>

<script setup lang="ts">
import PbPill from '@/components/pb/PbPill.vue'

const { t } = useI18n()

const { icon = 'sym_o_arrow_back_ios_new' } = defineProps<{
  icon?: string
}>()

const emit = defineEmits<{
  triggerReturn: []
}>()

const hostSlot = computed(() => activeSlot.value)
const slotOptions = computed<ReturnButtonSlotOptions>(() => hostSlot.value?.options() ?? {})
</script>
