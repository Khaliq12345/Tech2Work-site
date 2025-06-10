<template>
  <nuxtui-card outlined class="p-6 text-center">
    <nuxtui-icon :name="icon" size="4xl" />
    <h3 class="mt-4 font-semibold">{{ title }}</h3>
    <p class="mt-2 text-gray-600">Description concise.</p>
  </nuxtui-card>
</template>

<script lang="ts" setup>
defineProps<{ title: string; icon: string }>()
</script>
