<template>
  <!-- The section nav card and form card title live in AdminConfigPage (dc.html L331-334); this renders the active category only -->
  <div v-if="layout.visible" class="config-form">
    <template v-for="(element, index) in visibleCategories" :key="`${layout.path}-${index}`">
      <dispatch-renderer
        v-if="index == activeCategory"
        :schema="layout.schema"
        :uischema="element"
        :path="layout.path"
        :enabled="layout.enabled"
        :renderers="layout.renderers"
        :cells="layout.cells"
      />
    </template>
  </div>
</template>

<script lang="ts">
import { type Layout, type Categorization, type Category, isVisible, type Scoped } from '@jsonforms/core'
import { defineComponent, inject } from 'vue'
import { DispatchRenderer, rendererProps, useJsonFormsLayout, type RendererProps } from '@jsonforms/vue'
import { useQuasarLayout, useAjv, CONFIG_NAV_KEY, createConfigNavState } from '../util'

export default defineComponent({
  name: 'TopLevelNavigationRenderer',
  components: {
    DispatchRenderer,
  },
  props: {
    ...rendererProps<Layout>(),
  },
  setup(props: RendererProps<Layout>) {
    const ajv = useAjv()
    // provided by AdminConfigPage; a local state keeps the renderer usable standalone (first category only)
    const nav = inject(CONFIG_NAV_KEY, createConfigNavState, true)

    return {
      ...useQuasarLayout(useJsonFormsLayout(props)),

      nav,
      ajv,
    }
  },
  computed: {
    visibleCategories(): (Category | Categorization)[] {
      return (this.layout.uischema as Categorization).elements.filter((category: Category | Categorization) =>
        isVisible(category, this.layout.data, this.layout.path, this.ajv, this.config)
      )
    },
    visibleCategoryLabels(): string[] {
      return this.visibleCategories.map((element: any) => {
        return element.label ?? `${(element as Category & Scoped).scope.split('/').pop()}` //TODO: this is a workaround until categorization is well implemented.
      })
    },
    activeCategory(): number {
      return this.nav.active.value
    },
  },
  watch: {
    visibleCategoryLabels: {
      handler(labels: string[]) {
        this.nav.labels.value = labels
        if (this.nav.active.value >= labels.length) this.nav.active.value = 0
      },
      immediate: true,
    },
  },
})
</script>

<style scoped>
.config-form {
  min-width: 0;
}
</style>
