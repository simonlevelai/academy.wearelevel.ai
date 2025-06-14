<template>
  <div class="social-login-container">
    <div v-if="socialButtons.length > 0" class="space-y-3">
      <div class="text-center text-sm text-level-gray mb-4">
        Or sign in with
      </div>
      
      <div class="space-y-2">
        <button
          v-for="button in socialButtons"
          :key="button.provider"
          @click="loginWith(button)"
          class="w-full flex items-center justify-center px-4 py-3 border border-level-border rounded-button text-sm font-medium hover:bg-level-light transition-colors duration-200"
          :class="getButtonClass(button.provider)"
        >
          <component :is="getIcon(button.provider)" class="w-5 h-5 mr-3" />
          Continue with {{ button.name }}
        </button>
      </div>
      
      <div class="relative my-6">
        <div class="absolute inset-0 flex items-center">
          <div class="w-full border-t border-level-border"></div>
        </div>
        <div class="relative flex justify-center text-sm">
          <span class="px-2 bg-white text-level-gray">or</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Icons for social providers
const GoogleIcon = {
  template: `
    <svg viewBox="0 0 24 24" class="w-5 h-5">
      <path fill="#4285f4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
      <path fill="#34a853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
      <path fill="#fbbc05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
      <path fill="#ea4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
    </svg>
  `
}

const MicrosoftIcon = {
  template: `
    <svg viewBox="0 0 24 24" class="w-5 h-5">
      <path fill="#f25022" d="M1 1h10v10H1z"/>
      <path fill="#00a4ef" d="M13 1h10v10H13z"/>
      <path fill="#7fba00" d="M1 13h10v10H1z"/>
      <path fill="#ffb900" d="M13 13h10v10H13z"/>
    </svg>
  `
}

const socialButtons = ref([])
const loading = ref(false)

const getIcon = (provider) => {
  const icons = {
    google: GoogleIcon,
    microsoft: MicrosoftIcon
  }
  return icons[provider] || null
}

const getButtonClass = (provider) => {
  const classes = {
    google: 'hover:border-blue-300 focus:ring-blue-500',
    microsoft: 'hover:border-blue-300 focus:ring-blue-500'
  }
  return classes[provider] || ''
}

const loadSocialButtons = async () => {
  try {
    const response = await fetch('/api/method/lms.lms.social_auth.get_social_login_buttons')
    const result = await response.json()
    if (result.message) {
      socialButtons.value = result.message
    }
  } catch (error) {
    console.error('Failed to load social login buttons:', error)
  }
}

const loginWith = (button) => {
  if (loading.value) return
  
  loading.value = true
  // Redirect to OAuth provider
  window.location.href = button.url
}

onMounted(() => {
  loadSocialButtons()
})
</script>

<style scoped>
.social-login-container {
  max-width: 400px;
}

button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

button:active {
  transform: translateY(0);
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>