<template>
  <q-page id="logs-page" padding>
    <section class="pb-admin-card">
      <div class="logs-head">
        <h2 class="pb-admin-card__title">{{ $t('log messages') }}</h2>
        <q-btn no-caps unelevated class="pb-admin-btn" href="/api/debug/log/latest" target="_blank">{{ $t('download logs') }}</q-btn>
      </div>

      <q-markup-table flat class="logs-table">
        <thead>
          <tr class="text-left">
            <th>{{ $t('log level') }}</th>
            <th>{{ $t('time') }}</th>
            <th style="width: 100%">{{ $t('log message') }}</th>
            <th>{{ $t('module name') }}</th>
            <th>{{ $t('function name') }}</th>
            <th>{{ $t('line') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(record, idx) in store.logrecords as any[]" :key="idx">
            <td>
              <span class="logs-level" :style="{ background: debugLevelColor(record.level) }">{{ record.level }}</span>
            </td>
            <td>{{ record.time }}</td>
            <td>{{ record.message }}</td>
            <td>{{ record.name }}</td>
            <td>{{ record.funcName }}</td>
            <td>{{ record.lineno }}</td>
          </tr>
        </tbody>
      </q-markup-table>
    </section>
  </q-page>
</template>

<script setup lang="ts">
import { useMainStore } from '@/stores/main-store'
import { QBtn } from 'quasar'

const store = useMainStore()

// level badge background (palette tokens; ink stays dark on all of them)
const debugLevelColor = (level: string) => {
  if (level == 'DEBUG') return 'var(--t4)'
  if (level == 'INFO') return 'var(--t4)'
  if (level == 'WARNING') return 'var(--t3)'
  if (level == 'ERROR') return 'var(--pb-danger-text)'
  if (level == 'CRITICAL') return 'var(--pb-danger-text)'

  return 'var(--pb-muted)'
}
</script>

<style scoped>
.logs-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.logs-head .pb-admin-card__title {
  margin: 0;
}

.logs-table {
  background: transparent;
  color: var(--pb-text);
}

.logs-table :deep(th),
.logs-table :deep(td) {
  border-color: rgba(255, 255, 255, 0.1);
}

.logs-table :deep(th) {
  color: var(--pb-muted);
  font-weight: 700;
}

.logs-level {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 999px;
  color: var(--pb-bg);
  font-size: 12px;
  font-weight: 700;
}
</style>
