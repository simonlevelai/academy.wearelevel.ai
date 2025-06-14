<template>
  <div class="min-h-screen bg-level-light flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <!-- Logo -->
      <div class="flex justify-center">
        <img class="h-12 w-auto" src="/logo.svg" alt="Level AI Academy">
      </div>
      <h2 class="mt-6 text-center text-3xl font-bold text-level-dark">
        Sign in to Level AI Academy
      </h2>
      <p class="mt-2 text-center text-sm text-level-gray">
        Learn AI skills for social impact
      </p>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="level-card py-8 px-4 shadow sm:rounded-lg sm:px-10">
        
        <!-- Social Login Buttons -->
        <SocialLogin />
        
        <!-- Traditional Login Form -->
        <form class="space-y-6" @submit.prevent="handleLogin">
          <div>
            <label for="email" class="block text-sm font-medium text-level-dark">
              Email address
            </label>
            <div class="mt-1">
              <input
                id="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                v-model="loginForm.email"
                class="appearance-none block w-full px-3 py-2 border border-level-input rounded-button placeholder-gray-400 focus:outline-none focus:ring-level-primary focus:border-level-primary sm:text-sm"
                placeholder="Enter your email"
              />
            </div>
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-level-dark">
              Password
            </label>
            <div class="mt-1">
              <input
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                v-model="loginForm.password"
                class="appearance-none block w-full px-3 py-2 border border-level-input rounded-button placeholder-gray-400 focus:outline-none focus:ring-level-primary focus:border-level-primary sm:text-sm"
                placeholder="Enter your password"
              />
            </div>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input
                id="remember_me"
                name="remember_me"
                type="checkbox"
                v-model="loginForm.remember"
                class="h-4 w-4 text-level-primary focus:ring-level-primary border-gray-300 rounded"
              />
              <label for="remember_me" class="ml-2 block text-sm text-level-gray">
                Remember me
              </label>
            </div>

            <div class="text-sm">
              <a href="/forgot-password" class="font-medium text-level-primary hover:text-level-secondary">
                Forgot your password?
              </a>
            </div>
          </div>

          <div>
            <Button
              type="submit"
              :loading="isLoggingIn"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-button shadow-sm text-sm font-medium text-white bg-level-primary hover:bg-level-secondary focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-level-primary"
            >
              Sign in
            </Button>
          </div>
        </form>

        <!-- Sign up link -->
        <div class="mt-6">
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-level-border" />
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="px-2 bg-white text-level-gray">New to Level AI Academy?</span>
            </div>
          </div>

          <div class="mt-6 grid grid-cols-1 gap-3">
            <router-link
              to="/organization-signup"
              class="w-full inline-flex justify-center py-2 px-4 border border-level-border rounded-button shadow-sm bg-white text-sm font-medium text-level-dark hover:bg-level-light focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-level-primary"
            >
              Register your organization
            </router-link>
          </div>
        </div>

        <!-- Organization login note -->
        <div class="mt-6 p-4 bg-level-light rounded-button">
          <div class="flex">
            <div class="flex-shrink-0">
              <Info class="h-5 w-5 text-level-primary" />
            </div>
            <div class="ml-3">
              <h3 class="text-sm font-medium text-level-dark">
                Organization Account?
              </h3>
              <div class="mt-2 text-sm text-level-gray">
                <p>
                  If your organization is already registered, sign in with your work email or contact your organization administrator for access.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { Button } from 'frappe-ui'
import { Info } from 'lucide-vue-next'
import SocialLogin from '@/components/SocialLogin.vue'

const router = useRouter()

const isLoggingIn = ref(false)
const loginForm = reactive({
  email: '',
  password: '',
  remember: false
})

const handleLogin = async () => {
  isLoggingIn.value = true
  
  try {
    // Call Frappe's login API
    const response = await fetch('/api/method/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        usr: loginForm.email,
        pwd: loginForm.password
      })
    })
    
    const result = await response.json()
    
    if (response.ok && !result.exc) {
      // Login successful
      window.location.href = '/lms'
    } else {
      // Login failed
      const errorMessage = result._server_messages 
        ? JSON.parse(result._server_messages)[0] 
        : 'Login failed. Please check your credentials.'
      alert(errorMessage)
    }
    
  } catch (error) {
    console.error('Login error:', error)
    alert('Login failed. Please try again.')
  } finally {
    isLoggingIn.value = false
  }
}
</script>

<style scoped>
.level-card {
  background: white;
  border: 1px solid var(--color-border);
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
}

input:focus {
  border-color: var(--color-primary) !important;
  outline: none;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}
</style>