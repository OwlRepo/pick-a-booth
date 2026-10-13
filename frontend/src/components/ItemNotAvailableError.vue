<!-- eslint-disable @intlify/vue-i18n/no-raw-text -->
<template>
  <!-- usually not visible but if page is called with wrong id or the page was not closed after an item is deleted -->
  <div class="window-height window-width row justify-center items-center flex flex-center">
    <q-card class="pb-not-found q-pa-md no-shadow" bordered>
      <q-card-section>
        <div class="pb-not-found__title">🔎 oh no, item not found 🤷</div>
      </q-card-section>
      <q-card-section>
        <p>We have been looking everywhere but the item was not found. Maybe it was deleted?</p>
      </q-card-section>
      <q-card-section>
        <q-btn rounded unelevated no-caps label="go back to home" class="pb-not-found__btn full-width" to="/"></q-btn>
      </q-card-section>
      <q-card-section>
        <p class="pb-not-found__muted">If this happens again, please report a bug.</p>
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.pb-not-found {
  max-width: 560px;
  border-radius: var(--r-card);
  background: var(--pb-surface-1);
  border: var(--pb-line);
  color: var(--pb-text);
}

.pb-not-found__title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 30px;
  line-height: 1.15;
}

.pb-not-found__btn {
  min-height: 64px;
  background: var(--t1);
  color: var(--t1i);
  font-weight: 700;
  font-size: 18px;
}

.pb-not-found__muted {
  color: var(--pb-muted);
}
</style>
