<template>
  <div class="container mx-auto px-4 py-8">
    <!-- Header -->
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold text-level-dark">Team Management</h1>
        <p class="text-level-gray">Manage your organization's learning team and track progress</p>
      </div>
      <Button @click="showInviteModal = true" variant="solid">
        <UserPlus class="w-4 h-4 mr-2" />
        Invite Team Member
      </Button>
    </div>

    <!-- Organization Overview -->
    <div class="grid md:grid-cols-4 gap-6 mb-8">
      <div class="level-card p-6 text-center">
        <div class="text-3xl font-bold text-level-primary mb-2">{{ teamStats.totalMembers }}</div>
        <div class="text-sm text-level-gray">Team Members</div>
      </div>
      <div class="level-card p-6 text-center">
        <div class="text-3xl font-bold text-level-teal mb-2">{{ teamStats.activeLearners }}</div>
        <div class="text-sm text-level-gray">Active Learners</div>
      </div>
      <div class="level-card p-6 text-center">
        <div class="text-3xl font-bold text-level-secondary mb-2">{{ teamStats.coursesCompleted }}</div>
        <div class="text-sm text-level-gray">Courses Completed</div>
      </div>
      <div class="level-card p-6 text-center">
        <div class="text-3xl font-bold text-level-orange mb-2">{{ teamStats.avgProgress }}%</div>
        <div class="text-sm text-level-gray">Avg Progress</div>
      </div>
    </div>

    <!-- Team Members Table -->
    <div class="level-card">
      <div class="p-6 border-b border-level-border">
        <h2 class="text-xl font-semibold text-level-dark">Team Members</h2>
      </div>
      
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-level-light">
            <tr>
              <th class="text-left p-4 font-medium text-level-dark">Member</th>
              <th class="text-left p-4 font-medium text-level-dark">Role</th>
              <th class="text-left p-4 font-medium text-level-dark">Courses Enrolled</th>
              <th class="text-left p-4 font-medium text-level-dark">Progress</th>
              <th class="text-left p-4 font-medium text-level-dark">Last Active</th>
              <th class="text-left p-4 font-medium text-level-dark">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="member in teamMembers" :key="member.id" class="border-b border-level-border hover:bg-level-light">
              <td class="p-4">
                <div class="flex items-center">
                  <div class="w-10 h-10 bg-level-gradient rounded-full flex items-center justify-center text-white font-semibold mr-3">
                    {{ member.name.charAt(0) }}
                  </div>
                  <div>
                    <div class="font-medium text-level-dark">{{ member.name }}</div>
                    <div class="text-sm text-level-gray">{{ member.email }}</div>
                  </div>
                </div>
              </td>
              <td class="p-4">
                <span class="px-2 py-1 text-xs rounded-full"
                      :class="member.role === 'Admin' ? 'bg-level-primary text-white' : 'bg-level-light text-level-dark'">
                  {{ member.role }}
                </span>
              </td>
              <td class="p-4 text-level-dark">{{ member.coursesEnrolled }}</td>
              <td class="p-4">
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-level-light rounded-full mr-2">
                    <div class="h-2 bg-level-teal rounded-full" :style="`width: ${member.progress}%`"></div>
                  </div>
                  <span class="text-sm text-level-gray">{{ member.progress }}%</span>
                </div>
              </td>
              <td class="p-4 text-level-gray">{{ formatDate(member.lastActive) }}</td>
              <td class="p-4">
                <div class="flex space-x-2">
                  <Button size="sm" @click="viewMemberDetails(member)">View</Button>
                  <Button size="sm" variant="outline" @click="removeMember(member)" v-if="member.role !== 'Admin'">
                    Remove
                  </Button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Invite Team Member Modal -->
    <Dialog v-model="showInviteModal" :options="{ size: '2xl' }">
      <template #body>
        <div class="p-6">
          <h3 class="text-lg font-semibold mb-4">Invite Team Member</h3>
          
          <form @submit.prevent="inviteMember">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">Full Name</label>
                <input v-model="inviteForm.name" type="text" required
                       class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
              </div>
              
              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">Email Address</label>
                <input v-model="inviteForm.email" type="email" required
                       class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
              </div>
              
              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">Role</label>
                <select v-model="inviteForm.role"
                        class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none">
                  <option value="Member">Team Member</option>
                  <option value="Admin">Administrator</option>
                </select>
              </div>
              
              <div>
                <label class="block text-sm font-medium text-level-dark mb-2">Welcome Message (Optional)</label>
                <textarea v-model="inviteForm.message" rows="3"
                          class="w-full p-3 border border-level-input rounded-button focus:border-level-primary focus:outline-none"
                          placeholder="Add a personal welcome message..."></textarea>
              </div>
            </div>
            
            <div class="flex justify-end space-x-3 mt-6">
              <Button @click="showInviteModal = false" variant="outline">Cancel</Button>
              <Button type="submit" :loading="inviting">Send Invitation</Button>
            </div>
          </form>
        </div>
      </template>
    </Dialog>

    <!-- Member Details Modal -->
    <Dialog v-model="showMemberModal" :options="{ size: '3xl' }" v-if="selectedMember">
      <template #body>
        <div class="p-6">
          <div class="flex items-center mb-6">
            <div class="w-16 h-16 bg-level-gradient rounded-full flex items-center justify-center text-white font-bold text-xl mr-4">
              {{ selectedMember.name.charAt(0) }}
            </div>
            <div>
              <h3 class="text-xl font-semibold text-level-dark">{{ selectedMember.name }}</h3>
              <p class="text-level-gray">{{ selectedMember.email }}</p>
            </div>
          </div>

          <div class="grid md:grid-cols-2 gap-6">
            <div class="level-card p-4">
              <h4 class="font-semibold mb-3">Learning Progress</h4>
              <div class="space-y-3">
                <div v-for="course in selectedMember.courses" :key="course.name" 
                     class="flex justify-between items-center">
                  <span class="text-sm">{{ course.name }}</span>
                  <div class="flex items-center">
                    <div class="w-16 h-2 bg-level-light rounded-full mr-2">
                      <div class="h-2 bg-level-teal rounded-full" :style="`width: ${course.progress}%`"></div>
                    </div>
                    <span class="text-xs text-level-gray">{{ course.progress }}%</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="level-card p-4">
              <h4 class="font-semibold mb-3">Recent Activity</h4>
              <div class="space-y-2">
                <div v-for="activity in selectedMember.recentActivity" :key="activity.id" 
                     class="text-sm">
                  <div class="font-medium">{{ activity.action }}</div>
                  <div class="text-level-gray">{{ formatDate(activity.date) }}</div>
                </div>
              </div>
            </div>
          </div>

          <div class="flex justify-end mt-6">
            <Button @click="showMemberModal = false">Close</Button>
          </div>
        </div>
      </template>
    </Dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { Button, Dialog } from 'frappe-ui'
import { UserPlus } from 'lucide-vue-next'

const showInviteModal = ref(false)
const showMemberModal = ref(false)
const selectedMember = ref(null)
const inviting = ref(false)

const inviteForm = reactive({
  name: '',
  email: '',
  role: 'Member',
  message: ''
})

// Reactive data
const teamStats = ref({
  totalMembers: 0,
  activeLearners: 0,
  coursesCompleted: 0,
  avgProgress: 0
})

const teamMembers = ref([])
const currentOrganization = ref('Hope Foundation') // This would come from user session

// Load team data on component mount
const loadTeamData = async () => {
  try {
    // Load team stats
    const statsResponse = await fetch(`/api/method/lms.lms.doctype.lms_organization.lms_organization.get_organization_team_stats?organization=${encodeURIComponent(currentOrganization.value)}`)
    const statsResult = await statsResponse.json()
    
    if (statsResult.message && !statsResult.message.error) {
      teamStats.value = statsResult.message
    }
    
    // Load team members
    const membersResponse = await fetch(`/api/method/lms.lms.doctype.lms_organization.lms_organization.get_organization_team_members?organization=${encodeURIComponent(currentOrganization.value)}`)
    const membersResult = await membersResponse.json()
    
    if (membersResult.message && !membersResult.message.error) {
      teamMembers.value = membersResult.message
    }
    
  } catch (error) {
    console.error('Failed to load team data:', error)
  }
}

// Load data when component mounts
onMounted(() => {
  loadTeamData()
})

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-GB', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  })
}

const viewMemberDetails = (member) => {
  selectedMember.value = member
  showMemberModal.value = true
}

const removeMember = async (member) => {
  if (confirm(`Are you sure you want to remove ${member.name} from the team?`)) {
    try {
      const response = await fetch('/api/method/lms.lms.doctype.lms_organization.lms_organization.remove_team_member', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Frappe-CSRF-Token': frappe.csrf_token || ''
        },
        body: JSON.stringify({
          organization: currentOrganization.value,
          user_id: member.id
        })
      })
      
      const result = await response.json()
      
      if (result.message?.success) {
        // Remove from local list
        const index = teamMembers.value.findIndex(m => m.id === member.id)
        if (index > -1) {
          teamMembers.value.splice(index, 1)
          teamStats.value.totalMembers--
        }
        alert('Team member removed successfully!')
      } else {
        throw new Error(result.message?.message || 'Failed to remove member')
      }
    } catch (error) {
      console.error('Remove member error:', error)
      alert(`Failed to remove member: ${error.message}`)
    }
  }
}

const inviteMember = async () => {
  inviting.value = true
  
  try {
    const response = await fetch('/api/method/lms.lms.doctype.lms_organization.lms_organization.invite_team_member', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Frappe-CSRF-Token': frappe.csrf_token || ''
      },
      body: JSON.stringify({
        organization: currentOrganization.value,
        name: inviteForm.name,
        email: inviteForm.email,
        role: inviteForm.role,
        message: inviteForm.message
      })
    })
    
    const result = await response.json()
    
    if (result.message?.success) {
      // Reset form
      Object.assign(inviteForm, { name: '', email: '', role: 'Member', message: '' })
      showInviteModal.value = false
      
      // Reload team data to show new member
      await loadTeamData()
      
      alert('Invitation sent successfully!')
    } else {
      throw new Error(result.message?.message || 'Failed to send invitation')
    }
    
  } catch (error) {
    console.error('Invite error:', error)
    alert(`Failed to send invitation: ${error.message}`)
  } finally {
    inviting.value = false
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

.level-card:hover {
  box-shadow: var(--shadow-md);
}

input:focus,
textarea:focus,
select:focus {
  border-color: var(--color-primary) !important;
  outline: none;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}
</style>