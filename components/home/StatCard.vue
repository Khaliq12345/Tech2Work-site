<template>
  <div class="bg-white p-6 rounded-2xl shadow-md text-center">
    <nuxtui-icon :name="icon" size="xl" class="text-gray-600 mb-4" />
    <h3 class="text-2xl font-semibold text-gray-900">{{ title }}</h3>
    <p class="text-gray-500">{{ subtitle }}</p>
  </div>
</template>

<script lang="ts" setup>
defineProps<{ title: string; subtitle: string; icon: string }>()
</script>
