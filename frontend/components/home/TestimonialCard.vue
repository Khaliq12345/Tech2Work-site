<template>
  <UCard
    variant="soft"
    class="rounded-2xl border-none bg-white text-gray-800 shadow-2xl"
  >
    <div class="space-y-3">
      <!-- Citation -->
      <div class="text-md lg:text-lg flex">
        <UIcon name="i-lucide-quote" class="text-gray-400 size-10 md:size-20 lg:size-30 mb-2 mr-5" />
        <div class="text-left">
          <span class="text-gray-700 text-lg md:text-xl lg:text-2xl font-semibold"
            >“{{ quote }}”</span
          >
          <!-- Auteur -->
          <div class="flex items-center gap-4 mt-5 md:mt-10">
            <img
              v-if="avatar"
              :src="avatar"
              class="md:w-20 md:h-20 h-10 w-10  rounded-full object-cover border"
            />
            <div
              v-else
              class="rounded-full object-cover border p-3 bg-gray-100"
            >
              <UIcon name="i-lucide-user-round" class="text-gray-600 size-15" />
            </div>
            <div class="text-left">
              <span class="font-bold text-md md:text-xl text-gray-900">{{ name }}</span>
              <p class="text-sm md:text-md text-gray-500">{{ role }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </UCard>
</template>

<script lang="ts" setup>
defineProps<{
  quote: string;
  name: string;
  role: string;
  avatar: string;
}>();
</script>
