<template>
  <UCard variant="soft" class="p-y text-center shadow-2xl">
    <div class="flex items-center justify-start">
      <!-- <UIcon :name="icon" size="100" class="mr-5" /> -->
      <div class="text-left">
        <h3 class="text-3xl font-bold mb-2">{{ title }}</h3>
        <p class="font-semibold">{{ desc }}</p>
      </div>
    </div>
    <!--  -->
    <div v-if="features" class="text-left mt-6">
      <h3 class="text-2xl font-semibold mb-5">What you’ll get :</h3>
      <div v-for="f in features" :key="f" class="flex items-center my-4">
        <UIcon name="i-lucide-circle-check-big" size="20" class="mr-5" />
        {{ f }}
      </div>
    </div>
  </UCard>
</template>

<script lang="ts" setup>
defineProps<{
  title: string;
  desc: string;
  icon: string;
  features: string[];
}>();
</script>
