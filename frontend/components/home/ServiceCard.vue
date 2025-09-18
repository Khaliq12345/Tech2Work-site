<template>
  <UCard variant="soft" class="p-y text-center shadow-2xl w-full">
    <div class="flex items-center justify-start">
      <div class="text-left">
        <h3 class="text-lg md:text-xl font-bold mb-2">{{ title }}</h3>
        <p class="font-semibold">{{ desc }}</p>
      </div>
    </div>
    <!--  -->
    <div v-if="features.length != 0" class="text-left mt-6">
      <h3 v-if="icon" class="text-md md:text-lg font-semibold mb-5">
        {{ $t("home_services_features_title") }} :
      </h3>
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
