<template>
  <div id="services" class="pt-20 text-center">
    <p class="text-xl md:text-3xl lg:text-4xl mb-8 font-bold text-gray-900 uppercase">
      What clients say about
    </p>
    <UCarousel
      class="md:px-10 bg-white"
      v-slot="{ item }"
      loop
      dots
      :autoplay="{ delay: 2000 }"
      :items="items"
      :ui="{ item: 'lg:basis-1/2' }"
    >
      <HomeTestimonialCard
        :quote="item.quote"
        :name="item.name"
        :role="item.role"
        :avatar="item.avatar"
        class="flex-2/5 mx-3 mb-20"
      />
    </UCarousel>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps<{industry:string}>();
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/industries/get-industry-testimonials", {
  method: 'GET',
      params: {
        'industry': props.industry
      }
});
items.value = data.value
</script>
