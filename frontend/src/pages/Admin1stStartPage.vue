<template>
  <q-page id="admin-1ststart-page" padding>
    <h1 class="first-start-title">{{ $t('1st Start') }}</h1>

    <div class="first-start-grid">
      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"
          ><span class="pb-admin-card__dot" style="background: var(--t2)"></span>{{ $t('Standalone pages, slideshows') }}</div
        >
        <p>
          {{
            $t(
              'The standalone page links can be used on another device to show the gallery and let users browse their photos, print it without blocking the photobooth.'
            )
          }}
        </p>
        <div class="pb-admin-actions">
          <a href="#/standalone/gallery" target="_blank" class="pb-admin-action"><PbIcon name="images" :size="18" />{{ $t('Standalone Gallery') }}</a>
          <a href="#/standalone/slideshow" target="_blank" class="pb-admin-action"
            ><PbIcon name="images" :size="18" />{{ $t('Standalone Slideshow Random') }}</a
          >
          <a href="#/standby/slideshow/random" target="_blank" class="pb-admin-action"
            ><PbIcon name="images" :size="18" />{{ $t('Slideshow Random (opens after timeout automatically)') }}</a
          >
        </div>
      </section>

      <section class="pb-admin-card">
        <div class="pb-admin-card__eyebrow"><span class="pb-admin-card__dot" style="background: var(--t4)"></span>{{ $t('REST-API') }}</div>
        <p>
          {{
            $t(
              "The photobooth comes with a REST-API. The frontend part of the app uses the same API. It's well documented and used to integrate further with your own systems. Check the openapi documentation, it's interactive so easy to test."
            )
          }}
        </p>
        <div class="pb-admin-actions">
          <a href="/api/doc" target="_blank" class="pb-admin-action"
            ><PbIcon name="list" :size="18" />{{ $t('API documentation of Pick-a-Booth') }}</a
          >
        </div>
      </section>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import PbIcon from '@/components/pb/PbIcon.vue'
</script>

<style scoped>
.first-start-title {
  margin: 0 0 20px;
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 40px;
  line-height: 1.1;
}

.first-start-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
  align-items: start;
}

.first-start-grid p {
  margin: 6px 0 0;
  font-size: 15px;
  line-height: 1.5;
  color: var(--pb-muted-2);
}

@media (max-width: 640px) {
  .first-start-grid {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
