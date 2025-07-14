<template>
  <section
    id="services"
    class="py-20 bg-gradient-to-br from-gray-300 to-gray-50 text-center"
  >
    <p class="text-xl md:text-2xl px-4 lg:text-3xl mb-20 font-bold text-gray-900 uppercase">
      Our clients and what they say
    </p>
    <UCarousel
      class="md:px-10"
      v-slot="{ item }"
      loop
      dots
      :autoplay="{ delay: 2000 }"
      :items="items"
      :ui="{ item: 'lg:basis-1/2' }"
    >
      <TestimonialCard
        :quote="item.quote"
        :name="item.name"
        :role="item.role"
        :avatar="item.avatar"
        class="mx-3"
      />
    </UCarousel>
  </section>
</template>

<script lang="ts" setup>

const items: Ref<any[]> = ref([]);
const { data } = await useFetch("/api/home/get-home-testimonials");
items.value = data.value as any;
</script>
