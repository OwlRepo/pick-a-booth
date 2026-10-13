<template>
  <!-- progress bar to show waiting to load filter, ... -->
  <div class="pb-processing-bar" role="progressbar" aria-busy="true">
    <div class="pb-processing-bar__fill" />
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.pb-processing-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  z-index: 10;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.1);
}

.pb-processing-bar__fill {
  width: 40%;
  height: 100%;
  border-radius: 999px;
  background: var(--t3);
  animation: pbProcessingSlide 2.1s ease-in-out infinite;
}

@keyframes pbProcessingSlide {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(250%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-processing-bar__fill {
    animation: none;
    width: 100%;
    opacity: 0.6;
  }
}
</style>
