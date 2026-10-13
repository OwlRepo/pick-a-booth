import { computed, type ComputedRef } from 'vue'
import { useMediaQuery } from '@vueuse/core'

/** 'auto' follows the `(orientation: portrait)` media query (handoff §0: layout by orientation, not device sniffing). */
export type PbOrientation = 'auto' | 'landscape' | 'portrait'

export function useIsPortrait(orientation: () => PbOrientation): ComputedRef<boolean> {
  const portraitQuery = useMediaQuery('(orientation: portrait)')
  return computed(() => {
    const value = orientation()
    return value === 'portrait' || (value === 'auto' && portraitQuery.value)
  })
}
