<template>
  <div id="services" class="pt-20 text-center">
    <p class="text-4xl mb-8 font-bold text-gray-900 uppercase">
      What clients say about
    </p>
    <UCarousel
      class="px-10 bg-white"
      v-slot="{ item }"
      loop
      arrows
      dots
      :autoplay="{ delay: 2000 }"
      :items="items"
      :ui="{ item: 'basis-1/2' }"
    >
      <HomeTestimonialCard
        :quote="item.quote"
        :name="item.name"
        :role="item.role"
        :avatar="item.img"
        class="flex-2/5 mx-3 mb-20"
      />
    </UCarousel>
  </div>
</template>

<script lang="ts" setup>
defineProps<{ items: any[] }>();
</script>
