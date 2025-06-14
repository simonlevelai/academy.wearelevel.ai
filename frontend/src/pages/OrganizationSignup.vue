<template>
  <div class="min-h-screen bg-level-light">
    <div class="container mx-auto px-4 py-8">
      <!-- Header -->
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-level-dark mb-2">Register Your Organization</h1>
        <p class="text-level-gray">Join Level AI Academy and empower your team with AI skills for social impact</p>
      </div>

      <!-- Registration Form -->
      <div class="max-w-4xl mx-auto">
        <div class="level-card p-8">
          <form @submit.prevent="submitRegistration">
            <!-- Step Indicator -->
            <div class="flex justify-center mb-8">
              <div class="flex items-center space-x-4">
                <div v-for="(step, index) in steps" :key="index" 
                     class="flex items-center">
                  <div class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-semibold"
                       :class="currentStep > index ? 'bg-level-teal text-white' : 
                               currentStep === index ? 'bg-level-primary text-white' : 
                               'bg-gray-200 text-gray-500'">
                    {{ index + 1 }}
                  </div>
                  <span class="ml-2 text-sm" 
                        :class="currentStep >= index ? 'text-level-dark' : 'text-gray-400'">
                    {{ step }}
                  </span>
                  <div v-if="index < steps.length - 1" 
                       class="w-8 h-px bg-gray-200 ml-4"></div>
                </div>
              </div>
            </div>

            <!-- Step 1: Organization Details -->
            <div v-if="currentStep === 0" class="space-y-6">
              <h3 class="text-xl font-semibold text-level-dark mb-4">Organization Information</h3>
              
              <div class="grid md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Organization Name *</label>
                  <input v-model="formData.organizationName" type="text" required
                         class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                </div>
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Organization Type *</label>
                  <select v-model="formData.organizationType" required
                          class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                    <option value="">Select type...</option>
                    <option value="Charity">Charity</option>
                    <option value="Social Enterprise">Social Enterprise</option>
                    <option value="B-Corp">B-Corp</option>
                    <option value="Non-Profit">Non-Profit</option>
                    <option value="Community Group">Community Group</option>
                    <option value="Think Tank">Think Tank</option>
                    <option value="Educational Institution">Educational Institution</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
              </div>

              <div class="grid md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Primary Sector</label>
                  <select v-model="formData.sector"
                          class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                    <option value="">Select sector...</option>
                    <option value="Healthcare">Healthcare</option>
                    <option value="Education">Education</option>
                    <option value="Environment">Environment</option>
                    <option value="Social Justice">Social Justice</option>
                    <option value="Poverty & Homelessness">Poverty & Homelessness</option>
                    <option value="Mental Health">Mental Health</option>
                    <option value="Children & Youth">Children & Youth</option>
                    <option value="Elderly Care">Elderly Care</option>
                    <option value="Disability Support">Disability Support</option>
                    <option value="Arts & Culture">Arts & Culture</option>
                    <option value="Community Development">Community Development</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Team Size</label>
                  <select v-model="formData.teamSize"
                          class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                    <option value="">Select size...</option>
                    <option value="1-5">1-5 people</option>
                    <option value="6-20">6-20 people</option>
                    <option value="21-50">21-50 people</option>
                    <option value="51-100">51-100 people</option>
                    <option value="100+">100+ people</option>
                  </select>
                </div>
              </div>

              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">Organization Description</label>
                <textarea v-model="formData.description" rows="3"
                          class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none"
                          placeholder="Briefly describe your organization's mission and work..."></textarea>
              </div>

              <div class="grid md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Website URL</label>
                  <input v-model="formData.website" type="url"
                         class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none"
                         placeholder="https://your-organization.org">
                </div>
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Charity/Registration Number</label>
                  <input v-model="formData.registrationNumber" type="text"
                         class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                </div>
              </div>
            </div>

            <!-- Step 2: Contact Information -->
            <div v-if="currentStep === 1" class="space-y-6">
              <h3 class="text-xl font-semibold text-level-dark mb-4">Contact Information</h3>
              
              <div class="grid md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Primary Contact Name *</label>
                  <input v-model="formData.contactName" type="text" required
                         class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                </div>
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Email Address *</label>
                  <input v-model="formData.contactEmail" type="email" required
                         class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                </div>
              </div>

              <div class="grid md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Phone Number</label>
                  <input v-model="formData.phoneNumber" type="tel"
                         class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                </div>
                <div>
                  <label class="block text-sm font-medium text-level-dark mb-2">Country</label>
                  <select v-model="formData.country"
                          class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                    <option value="">Select country...</option>
                    <option value="United Kingdom">United Kingdom</option>
                    <option value="United States">United States</option>
                    <option value="Canada">Canada</option>
                    <option value="Australia">Australia</option>
                    <option value="Germany">Germany</option>
                    <option value="France">France</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
              </div>

              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">Address</label>
                <textarea v-model="formData.address" rows="3"
                          class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none"></textarea>
              </div>
            </div>

            <!-- Step 3: Learning Goals -->
            <div v-if="currentStep === 2" class="space-y-6">
              <h3 class="text-xl font-semibold text-level-dark mb-4">Learning Goals & AI Focus</h3>
              
              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">Maximum Team Members for Training</label>
                <input v-model.number="formData.maxLearners" type="number" min="1" max="200"
                       class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none"
                       placeholder="e.g., 10">
                <p class="text-sm text-level-gray mt-1">How many people from your organization will be using Level AI Academy?</p>
              </div>

              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">AI Focus Areas</label>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
                  <label v-for="area in aiFocusAreas" :key="area" class="flex items-center">
                    <input type="checkbox" :value="area" v-model="formData.selectedFocusAreas"
                           class="mr-2 text-level-primary">
                    <span class="text-sm">{{ area }}</span>
                  </label>
                </div>
              </div>

              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">Learning Goals</label>
                <textarea v-model="formData.learningGoals" rows="4"
                          class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none"
                          placeholder="What do you hope to achieve through AI training? How will it help your organization's mission?"></textarea>
              </div>

              <div class="space-y-3">
                <label class="flex items-start">
                  <input type="checkbox" v-model="formData.enableReporting"
                         class="mr-3 mt-1 text-level-primary">
                  <div>
                    <span class="font-medium">Enable Team Progress Reporting</span>
                    <p class="text-sm text-level-gray">Allow organization administrators to view team learning progress and completion rates.</p>
                  </div>
                </label>

                <label class="flex items-start">
                  <input type="checkbox" v-model="formData.customBranding"
                         class="mr-3 mt-1 text-level-primary">
                  <div>
                    <span class="font-medium">Custom Organization Branding</span>
                    <p class="text-sm text-level-gray">Add your organization's logo and colors to the learning platform.</p>
                  </div>
                </label>
              </div>
            </div>

            <!-- Navigation Buttons -->
            <div class="flex justify-between mt-8 pt-6 border-t border-level-border">
              <Button v-if="currentStep > 0" @click="previousStep" variant="outline">
                Previous
              </Button>
              <div v-else></div>

              <Button v-if="currentStep < steps.length - 1" @click="nextStep" variant="solid">
                Next
              </Button>
              <Button v-else type="submit" variant="solid" :loading="submitting">
                Register Organization
              </Button>
            </div>
          </form>
        </div>
      </div>

      <!-- Benefits Section -->
      <div class="max-w-4xl mx-auto mt-12">
        <h2 class="text-2xl font-semibold text-center text-level-dark mb-8">
          Why Choose Level AI Academy for Your Organization?
        </h2>
        <div class="grid md:grid-cols-3 gap-6">
          <div class="text-center p-6">
            <div class="w-12 h-12 bg-level-gradient rounded-full mx-auto mb-4 flex items-center justify-center">
              <Heart class="w-6 h-6 text-white" />
            </div>
            <h3 class="font-semibold mb-2">Purpose-Driven Focus</h3>
            <p class="text-sm text-level-gray">AI training specifically designed for charities, social enterprises, and purpose-driven organizations.</p>
          </div>
          <div class="text-center p-6">
            <div class="w-12 h-12 bg-level-gradient rounded-full mx-auto mb-4 flex items-center justify-center">
              <Users class="w-6 h-6 text-white" />
            </div>
            <h3 class="font-semibold mb-2">Team Management</h3>
            <p class="text-sm text-level-gray">Enroll your entire team, track progress, and measure collective learning outcomes.</p>
          </div>
          <div class="text-center p-6">
            <div class="w-12 h-12 bg-level-gradient rounded-full mx-auto mb-4 flex items-center justify-center">
              <BarChart3 class="w-6 h-6 text-white" />
            </div>
            <h3 class="font-semibold mb-2">Impact Measurement</h3>
            <p class="text-sm text-level-gray">Learn how to use AI to measure and amplify your organization's social impact.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { Button } from 'frappe-ui'
import { Heart, Users, BarChart3 } from 'lucide-vue-next'
import { useRouter } from 'vue-router'

const router = useRouter()

const currentStep = ref(0)
const submitting = ref(false)

const steps = [
  'Organization Details',
  'Contact Information', 
  'Learning Goals'
]

const aiFocusAreas = [
  'Process Automation',
  'Data Analysis',
  'Content Generation',
  'Grant Writing',
  'Impact Measurement',
  'Social Media Management',
  'Fundraising Optimization',
  'Volunteer Management',
  'Resource Allocation',
  'Outcome Prediction'
]

const formData = reactive({
  organizationName: '',
  organizationType: '',
  sector: '',
  teamSize: '',
  description: '',
  website: '',
  registrationNumber: '',
  contactName: '',
  contactEmail: '',
  phoneNumber: '',
  country: '',
  address: '',
  maxLearners: 10,
  selectedFocusAreas: [],
  learningGoals: '',
  enableReporting: true,
  customBranding: false
})

const nextStep = () => {
  if (validateCurrentStep()) {
    currentStep.value++
  }
}

const previousStep = () => {
  if (currentStep.value > 0) {
    currentStep.value--
  }
}

const validateCurrentStep = () => {
  switch (currentStep.value) {
    case 0:
      return formData.organizationName && formData.organizationType
    case 1:
      return formData.contactName && formData.contactEmail
    case 2:
      return formData.maxLearners > 0
    default:
      return true
  }
}

const submitRegistration = async () => {
  if (!validateCurrentStep()) return
  
  submitting.value = true
  
  try {
    // Prepare data for submission
    const registrationData = {
      ...formData,
      aiFocusAreas: formData.selectedFocusAreas.join(', ')
    }
    
    // Call the API to create the organization
    const response = await fetch('/api/method/lms.lms.doctype.lms_organization.lms_organization.register_organization', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Frappe-CSRF-Token': frappe.csrf_token || ''
      },
      body: JSON.stringify({ data: JSON.stringify(registrationData) })
    })
    
    const result = await response.json()
    
    if (result.message?.success) {
      alert('Organization registered successfully! You will receive a welcome email shortly.')
      router.push('/courses')
    } else {
      throw new Error(result.message?.message || 'Registration failed')
    }
    
  } catch (error) {
    console.error('Registration error:', error)
    alert(`Registration failed: ${error.message}. Please try again.`)
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.hero-gradient {
  background: var(--gradient-primary);
}

.level-card {
  background: white;
  border: 1px solid var(--color-border);
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
}

input:focus,
textarea:focus,
select:focus {
  border-color: var(--color-primary) !important;
  outline: none;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}
</style>