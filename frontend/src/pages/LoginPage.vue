<template>
  <!-- 20 LoginPage (dc.html L303-312) -->
  <q-page id="login-page" class="login-page">
    <section class="login-page__poster">
      <PbPill variant="tint" icon="arrow-left" :icon-size="19" :font-size="16" @click="router.go(-1)">{{ $t('Back to booth') }}</PbPill>
      <h1 class="login-page__headline">{{ $t('Host only.') }}</h1>
    </section>

    <q-form class="login-page__form" @submit="submit">
      <div>
        <div class="login-page__title">{{ $t('Sign in') }}</div>
        <div class="login-page__subtitle">{{ $t('Enter the admin password to manage this booth.') }}</div>
      </div>

      <div class="login-page__field">
        <label for="login-password" class="login-page__label">{{ $t('Password') }}</label>
        <input id="login-password" v-model="user.password" class="login-page__input" type="password" autocomplete="current-password" />
      </div>

      <PbBigButton type="submit" block :height="68" bg="var(--t1)" fg="var(--t1i)" icon="chevron-right" :icon-size="23" :font-size="20">
        {{ $t('Sign in') }}
      </PbBigButton>

      <div class="login-page__hint">{{ $t('Forgot it? The password is set by whoever installed this booth.') }}</div>
    </q-form>
  </q-page>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { login } from '@/util/auth'
import { useRouter } from 'vue-router'
import PbPill from '@/components/pb/PbPill.vue'
import PbBigButton from '@/components/pb/PbBigButton.vue'

const router = useRouter()

const user = reactive({
  username: 'admin', // there are no usernames in our app, it's always admin...
  password: '',
})

const submit = async () => {
  try {
    // login() shows the error notification itself on failure
    await login(user)
    router.push('/admin')
  } catch (err) {
    console.error(err)
  }
}
</script>

<style scoped>
.login-page {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 540px;
  gap: 20px;
  height: 100vh;
  padding: 24px;
  background: var(--pb-bg);
  color: var(--pb-text);
}

.login-page__poster {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  min-height: 0;
  padding: 44px;
  border-radius: 32px;
  background: var(--t1);
  color: var(--t1i);
}

.login-page__headline {
  /* min-content puts each word on its own line, as "Host<br>only." in the reference */
  width: min-content;
  margin: 0;
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  font-size: 120px;
  line-height: 0.92;
  letter-spacing: -0.04em;
}

.login-page__form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 26px;
  min-height: 0;
  padding: 44px;
  border-radius: 32px;
  background: var(--pb-surface-1);
  border: var(--pb-line);
}

.login-page__title {
  font-family: 'Sora', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-size: 40px;
}

.login-page__subtitle {
  font-size: 17px;
  color: var(--pb-muted);
}

.login-page__field {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.login-page__label {
  font-size: 14px;
  font-weight: 700;
  color: var(--pb-muted);
}

.login-page__input {
  width: 100%;
  height: 64px;
  padding: 0 20px;
  border-radius: 18px;
  background: var(--pb-bg);
  border: var(--pb-line);
  color: var(--pb-text);
  font: inherit;
  font-size: 26px;
  letter-spacing: 0.3em;
  outline: none;
}

.login-page__input:focus-visible {
  outline: 3px solid var(--pb-text);
  outline-offset: 3px;
}

.login-page__hint {
  font-size: 14px;
  color: var(--pb-muted);
  line-height: 1.45;
}

/* no portrait artboard: poster stacks above the form */
@media (orientation: portrait) {
  .login-page {
    grid-template-columns: minmax(0, 1fr);
    grid-template-rows: minmax(0, 1fr) auto;
    height: auto;
    min-height: 100vh;
  }

  .login-page__poster {
    gap: 44px;
  }
}
</style>
