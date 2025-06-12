<template>
  <div id="services" class="pt-20 px-10 lg:px-20 text-center">
    <p class="text-4xl mb-8 font-bold text-gray-900 uppercase">
      SERVICES WE PROVIDE IN THIS INDUSTRY
    </p>
    <div class="mt-8 flex flex-wrap lg:flex-nowrap gap-5 justify-center">
      <IndustriesServiceCard
        v-for="item in items"
        :class="item.class"
        :title="item.title"
        :desc="item.desc"
        :icon="item.icon"
        :features="[]"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps<{ items: any[] }>();
</script>
