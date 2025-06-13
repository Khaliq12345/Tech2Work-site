<template>
  <div id="services" class="mb-20 px-10 lg:px-20 text-center">
    <p class="text-4xl mb-8 font-bold text-gray-900 uppercase">
      WHY TECH2WORK FOR THIS DEVELOPMENT ?
    </p>
    <div class="mt-10 gap-5 justify-center place-items-center">
      <IndustriesReasonCard
        v-for="item in items"
        class="w-full mb-8"
        :title="item.title"
        :content="item.content"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps<{ items: any[] }>();
</script>
