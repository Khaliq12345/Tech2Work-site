<script setup lang="ts">
import { ref } from 'vue'
import { UCard, UButton, ULink } from '#components'

interface SalesContact {
  id: string
  name: string
  role: string
  photoUrl: string
  linkedinUrl: string
}

const contacts: SalesContact[] = [
  {
    id: 'oleksii',
    name: 'Oleksii Kamynin',
    role: 'Sales Manager',
    photoUrl: 'https://thumbs.dreamstime.com/b/male-silhouette-black-white-vector-illustration-avatar-icon-pictogram-365114907.jpg',
    linkedinUrl: 'https://www.linkedin.com/in/oleksii-kamynin-profile',
  },
  {
    id: 'natalia',
    name: 'Natalia Zamai',
    role: 'Sales Manager',
    photoUrl: 'https://media.istockphoto.com/id/2014684899/vector/placeholder-avatar-female-person-default-woman-avatar-image-gray-profile-anonymous-face.jpg?s=612x612&w=0&k=20&c=D-dk9ek0_jb19TiMVNVmlpvYVrQiFiJmgGmiLB5yE4w=',
    linkedinUrl: 'https://www.linkedin.com/in/natalia-zamai-profile',
  },
  
]
</script>

<template>
  <div class="flex flex-wrap gap-8 py-12 md:py-20 container mx-auto px-4">
    <!-- Bloc principal de contact -->
    <UCard
      class="col-span-1 lg:col-span-2 shadow-xl p-6 flex flex-col justify-center w-full bg-gradient-to-br from-black to-gray-400"
    >
      <div class="space-y-6">
        <h2 class="text-3xl font-bold text-gray-900 dark:text-white">Let’s Build Together</h2>
        <p class="text-gray-600 dark:text-gray-300 text-base">
          Reach out to our sales managers for tailored software development solutions and professional guidance.
        </p>

        <UButton icon="i-heroicons-phone"  color="primary" class="text-white text-xl rounded-3xl py-3 px-6 mt-10" variant="solid"
                            label="Contact Us" to="#" />
      </div>
    </UCard>

    <!-- Contacts commerciaux -->
    <div class="grid grid-cols-1 sm:grid-cols-2 w-full gap-6">
      <UCard
        v-for="person in contacts"
        :key="person.id"
        class="p-4 rounded-lg hover:shadow-lg transition-shadow bg-gradient-to-br from-black to-gray-800" variant=""
      >

      <div class="flex justify-center items-center gap-x-5">
 <div class="">
<img
          :src="person.photoUrl"
          :alt="person.name"
          class="w-30 h-30 rounded-full object-cover mb-4 border-2 "
        />
      </div>

      <div class="">
<h3 class="text-lg font-semibold text-gray-900 dark:text-white">{{ person.name }}</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">{{ person.role }}</p>
        <ULink
          :to="person.linkedinUrl"
          target="_blank"
          class="inline-flex items-center text-white hover:text-gray-600 text-sm font-medium"
        >
          <UIcon name="i-mdi-linkedin" class="w-5 h-5 mr-1" />
          LinkedIn
        </ULink>
      </div>

      </div>

     
        
        
      </UCard>
    </div>
  </div>
</template>

<style scoped>
/* Aucun style personnalisé nécessaire grâce à Tailwind/Nuxt UI */
</style>
