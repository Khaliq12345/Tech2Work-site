<template>
  <section
    id="services"
    class="py-20 bg-gradient-to-br from-gray-300 to-gray-50 text-center"
  >
    <p class="text-2xl md:text-3xl lg:text-4xl mb-20 font-bold text-gray-900 uppercase">
      Our clients and what they say
    </p>
    <div class=" mx-auto flex px-3 flex-wrap justify-center gap-5">
      <TestimonialCard
        v-for="item in items"
        :quote="item.quote"
        :name="item.name"
        :role="item.role"
        :avatar="item.avatar"
        :class="item.classname"
      />
    </div>
  </section>
</template>

<script lang="ts" setup>

const items: Ref<any[]> = ref([]);
const { data } = await useFetch("/api/home/get-home-testimonials");
items.value = data.value as any;
</script>
