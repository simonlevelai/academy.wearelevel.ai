<template>
  <div class="container mx-auto px-4 py-8">
    <!-- Hero Section -->
    <div class="hero-gradient text-white rounded-card p-8 mb-8">
      <div class="max-w-4xl mx-auto text-center">
        <h1 class="text-4xl font-bold mb-4">Impact Stories</h1>
        <p class="text-xl opacity-90">
          See how purpose-driven organizations are using AI to amplify their social impact
        </p>
      </div>
    </div>

    <!-- Stories Grid -->
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
      <div v-for="story in impactStories" :key="story.id" class="level-card p-6 cursor-pointer" 
           @click="selectedStory = story">
        <div class="flex items-center mb-4">
          <div class="w-12 h-12 bg-level-gradient rounded-full flex items-center justify-center text-white font-bold">
            {{ story.organization.charAt(0) }}
          </div>
          <div class="ml-3">
            <h3 class="font-semibold text-level-dark">{{ story.organization }}</h3>
            <p class="text-sm text-level-gray">{{ story.sector }}</p>
          </div>
        </div>
        <h4 class="font-semibold mb-2 text-level-dark">{{ story.title }}</h4>
        <p class="text-level-gray text-sm mb-4">{{ story.summary }}</p>
        <div class="flex items-center justify-between">
          <span class="badge-ai text-xs">{{ story.aiTool }}</span>
          <span class="text-level-teal font-semibold">{{ story.impact }}</span>
        </div>
      </div>
    </div>

    <!-- Call to Action -->
    <div class="bg-level-light rounded-card p-6 text-center">
      <h2 class="text-2xl font-semibold mb-4 text-level-dark">Ready to Create Your Impact Story?</h2>
      <p class="text-level-gray mb-6">
        Join Level AI Academy and learn how to implement AI in your organization
      </p>
      <router-link to="/courses" class="inline-block bg-level-primary text-white px-6 py-3 rounded-button font-semibold hover:bg-level-secondary transition-colors">
        Explore Courses
      </router-link>
    </div>

    <!-- Story Detail Modal -->
    <Dialog v-model="showStoryModal" :options="{ size: '4xl' }" v-if="selectedStory">
      <template #body>
        <div class="p-6">
          <div class="flex items-center mb-6">
            <div class="w-16 h-16 bg-level-gradient rounded-full flex items-center justify-center text-white font-bold text-xl">
              {{ selectedStory.organization.charAt(0) }}
            </div>
            <div class="ml-4">
              <h2 class="text-2xl font-bold text-level-dark">{{ selectedStory.organization }}</h2>
              <p class="text-level-gray">{{ selectedStory.sector }} • {{ selectedStory.location }}</p>
            </div>
          </div>

          <h3 class="text-xl font-semibold mb-4 text-level-dark">{{ selectedStory.title }}</h3>
          
          <div class="grid md:grid-cols-2 gap-6 mb-6">
            <div>
              <h4 class="font-semibold mb-2 text-level-dark">The Challenge</h4>
              <p class="text-level-gray">{{ selectedStory.challenge }}</p>
            </div>
            <div>
              <h4 class="font-semibold mb-2 text-level-dark">The Solution</h4>
              <p class="text-level-gray">{{ selectedStory.solution }}</p>
            </div>
          </div>

          <div class="bg-level-light rounded-button p-4 mb-6">
            <h4 class="font-semibold mb-2 text-level-dark">Impact Achieved</h4>
            <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
              <div v-for="metric in selectedStory.metrics" :key="metric.label" class="text-center">
                <div class="text-2xl font-bold text-level-teal">{{ metric.value }}</div>
                <div class="text-sm text-level-gray">{{ metric.label }}</div>
              </div>
            </div>
          </div>

          <div class="flex justify-between items-center">
            <div>
              <span class="badge-ai mr-2">{{ selectedStory.aiTool }}</span>
              <span class="text-sm text-level-gray">Level AI Academy Graduate</span>
            </div>
            <Button @click="showStoryModal = false">Close</Button>
          </div>
        </div>
      </template>
    </Dialog>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Dialog, Button } from 'frappe-ui'

const selectedStory = ref(null)
const showStoryModal = computed({
  get: () => !!selectedStory.value,
  set: (value) => {
    if (!value) selectedStory.value = null
  }
})

// Sample impact stories data
const impactStories = ref([
  {
    id: 1,
    organization: "Hope Housing Foundation",
    sector: "Homelessness Support",
    location: "Manchester, UK",
    title: "AI-Powered Case Management Saves 15 Hours Weekly",
    summary: "Automated intake processes and intelligent case matching help housing officers focus on direct client support.",
    challenge: "Manual paperwork and case management consumed 60% of staff time, reducing direct client interaction.",
    solution: "Implemented AI-powered intake forms and automated case prioritization using Level AI Academy training.",
    impact: "15hrs saved/week",
    aiTool: "Process Automation",
    metrics: [
      { label: "Time Saved", value: "15hrs/week" },
      { label: "Cases Processed", value: "+40%" },
      { label: "Client Satisfaction", value: "94%" }
    ]
  },
  {
    id: 2,
    organization: "Green Future Initiative",
    sector: "Environmental Conservation",
    location: "Brighton, UK",
    title: "Grant Success Rate Doubles with AI Writing Assistant",
    summary: "Environmental charity uses AI to craft compelling grant applications, securing £250k in additional funding.",
    challenge: "Limited grant writing expertise led to low success rates and missed funding opportunities.",
    solution: "Trained team in AI-assisted grant writing techniques through Level AI Academy courses.",
    impact: "£250k secured",
    aiTool: "Content Generation",
    metrics: [
      { label: "Grant Success Rate", value: "85%" },
      { label: "Additional Funding", value: "£250k" },
      { label: "Application Time", value: "-50%" }
    ]
  },
  {
    id: 3,
    organization: "Mind Wellness Centre",
    sector: "Mental Health Support",
    location: "Birmingham, UK",
    title: "Predictive Analytics Improves Crisis Intervention",
    summary: "AI helps identify at-risk clients earlier, enabling proactive support and reducing emergency interventions by 30%.",
    challenge: "Reactive approach to mental health crises led to poor outcomes and stretched resources.",
    solution: "Developed predictive models using anonymized data to identify early warning signs.",
    impact: "30% fewer crises",
    aiTool: "Predictive Analytics",
    metrics: [
      { label: "Crisis Reduction", value: "30%" },
      { label: "Early Interventions", value: "+65%" },
      { label: "Client Outcomes", value: "Improved" }
    ]
  },
  {
    id: 4,
    organization: "Learning Together Trust",
    sector: "Education",
    location: "London, UK",
    title: "Personalized Learning Paths Boost Student Outcomes",
    summary: "AI-driven assessment and curriculum adaptation helps disadvantaged students achieve better educational outcomes.",
    challenge: "One-size-fits-all approach failed to address diverse learning needs of disadvantaged students.",
    solution: "Created adaptive learning system using AI to personalize educational content and pacing.",
    impact: "25% grade improvement",
    aiTool: "Adaptive Learning",
    metrics: [
      { label: "Grade Improvement", value: "25%" },
      { label: "Engagement Rate", value: "90%" },
      { label: "Completion Rate", value: "+40%" }
    ]
  },
  {
    id: 5,
    organization: "Community Food Network",
    sector: "Food Security",
    location: "Glasgow, UK",
    title: "Smart Inventory Reduces Food Waste by 40%",
    summary: "AI-powered demand forecasting and inventory management helps food bank optimize distribution and reduce waste.",
    challenge: "Unpredictable demand led to frequent shortages and significant food waste.",
    solution: "Implemented AI forecasting system to predict demand patterns and optimize food distribution.",
    impact: "40% less waste",
    aiTool: "Demand Forecasting",
    metrics: [
      { label: "Food Waste Reduction", value: "40%" },
      { label: "People Fed", value: "+500/month" },
      { label: "Cost Savings", value: "£15k/year" }
    ]
  },
  {
    id: 6,
    organization: "Elder Care Connect",
    sector: "Senior Care",
    location: "Cardiff, UK",
    title: "Chatbot Provides 24/7 Support for Isolated Seniors",
    summary: "AI companion reduces loneliness and provides instant access to resources for elderly community members.",
    challenge: "Limited staff availability meant seniors often waited hours for support during evenings and weekends.",
    solution: "Developed empathetic AI chatbot trained on senior care protocols and local resources.",
    impact: "24/7 availability",
    aiTool: "Conversational AI",
    metrics: [
      { label: "Response Time", value: "Instant" },
      { label: "User Satisfaction", value: "92%" },
      { label: "Loneliness Score", value: "-35%" }
    ]
  }
])
</script>

<style scoped>
.hero-gradient {
  background: var(--gradient-primary);
}

.level-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.badge-ai {
  background: var(--gradient-primary);
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 500;
}
</style>