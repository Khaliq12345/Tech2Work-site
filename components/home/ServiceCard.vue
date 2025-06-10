<template>
  <UCard variant="subtle" class="p-6 text-center bg-gradient-to-br from-gray-50 to-gray-200">
    <div class="flex items-center justify-center">
    <UIcon :name="icon" size="50" class="mr-5" />
<div class="text-left">
  <h3 class="mt-4 font-semibold">{{ title }}</h3>
    <p class="mt-2 text-gray-600">Description concise.</p>
</div>
    </div>
    
  </UCard>
</template>

<script lang="ts" setup>
defineProps<{ title: string; icon: string }>()
</script>
