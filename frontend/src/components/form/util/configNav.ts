import { ref, type InjectionKey, type Ref } from 'vue'

/**
 * Shared state between AdminConfigPage (renders the section nav card and the form card title)
 * and TopLevelNavigationRenderer (owns the schema categories and renders the active one).
 */
export interface ConfigNavState {
  /** visible category labels of the current schema, in order */
  labels: Ref<string[]>
  /** index into labels of the category that is rendered */
  active: Ref<number>
}

export const CONFIG_NAV_KEY: InjectionKey<ConfigNavState> = Symbol('configNav')

export const createConfigNavState = (): ConfigNavState => ({
  labels: ref<string[]>([]),
  active: ref(0),
})

/** "ui_settings" -> "ui settings"; the nav/title capitalize via CSS, as the previous tabs did */
export const categoryTitle = (label: string | undefined): string => (label ?? '').replace(/_/g, ' ')
