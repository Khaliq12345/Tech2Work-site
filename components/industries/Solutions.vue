<template>
  <section id="services" class="py-20 px-10 bg-white text-center">
    <p class="text-4xl mb-20 font-bold text-gray-900 uppercase">
      SOLUTIONS WE DEVELOP FOR THIS INDUSTRY
    </p>
    <div
      class="container mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
    >
      <HomeServiceCard
        v-for="item in items"
        :class="item.class"
        :title="item.title"
        :desc="item.desc"
        icon=""
        :features="item.features"
      />
    </div>
  </section>
</template>

<script lang="ts" setup>
defineProps<{ items: any[] }>();
</script>
