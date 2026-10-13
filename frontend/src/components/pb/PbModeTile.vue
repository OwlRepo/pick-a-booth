<!--
  PbModeTile — front-page mode tile (dc.html L44-47 landscape, L197-199 portrait).
  Props:
    bg: string                   tile colour, any CSS value; use tileColor() from src/theme/palette.ts
    fg: string                   ink colour, any CSS value (tileColor().fg)
    icon?: string                PbIcon name (stroke 2.2), or use the #icon slot
    orientation?: 'auto' | 'landscape' | 'portrait' = 'auto'
                                 landscape: radius 28, padding 22, icon circle 64 / glyph 30, label 27px
                                 portrait:  radius 32, padding 26, icon circle 76 / glyph 36, label 34px
                                 'auto' follows the orientation media query
    disabled?: boolean
  Slots: default = label (Sora 600), icon = custom icon.
  Fills its grid cell (width/height 100%); the parent grid sets the row height.
  Native listeners (@click) fall through to the <button>.
-->
<template>
  <button
    type="button"
    class="pb-mode-tile"
    :class="{ 'pb-mode-tile--portrait': isPortrait }"
    :disabled="disabled"
    :style="{ '--pb-tile-bg': bg, '--pb-tile-fg': fg }"
  >
    <span class="pb-mode-tile__icon">
      <slot name="icon">
        <PbIcon v-if="icon" :name="icon" :size="isPortrait ? 36 : 30" :stroke-width="2.2" />
      </slot>
    </span>
    <span class="pb-mode-tile__label"><slot /></span>
  </button>
</template>

<script setup lang="ts">
import PbIcon from './PbIcon.vue'
import { useIsPortrait, type PbOrientation } from './orientation'

const {
  bg,
  fg,
  icon,
  orientation = 'auto',
  disabled = false,
} = defineProps<{
  bg: string
  fg: string
  icon?: string
  orientation?: PbOrientation
  disabled?: boolean
}>()

const isPortrait = useIsPortrait(() => orientation)
</script>

<style scoped>
.pb-mode-tile {
  appearance: none;
  margin: 0;
  border: 0;
  font: inherit;
  text-align: left;
  width: 100%;
  height: 100%;
  min-width: 0;
  background: var(--pb-tile-bg);
  color: var(--pb-tile-fg);
  border-radius: 28px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  cursor: pointer;
  box-shadow: 0 12px 32px -12px var(--pb-tile-bg);
  -webkit-tap-highlight-color: transparent;
}

.pb-mode-tile:hover:not(:disabled) {
  transform: translateY(-3px);
  filter: brightness(1.06);
}

.pb-mode-tile:active:not(:disabled) {
  transform: scale(0.97);
}

.pb-mode-tile:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

.pb-mode-tile:disabled {
  cursor: default;
  opacity: 0.5;
}

.pb-mode-tile__icon {
  width: 64px;
  height: 64px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.28);
  display: flex;
  align-items: center;
  justify-content: center;
}

.pb-mode-tile__label {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 27px;
  line-height: 1;
}

.pb-mode-tile--portrait {
  border-radius: 32px;
  padding: 26px;
}

.pb-mode-tile--portrait .pb-mode-tile__icon {
  width: 76px;
  height: 76px;
}

.pb-mode-tile--portrait .pb-mode-tile__label {
  font-size: 34px;
}
</style>
