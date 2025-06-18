<template>
  <section id="services" class="py-20 px-5 md:px-10 bg-white text-center">
    <p class="text-xl md:text-3xl lg:text-4xl mb-20 font-bold text-gray-900 uppercase">
      SOLUTIONS WE DEVELOP FOR THIS INDUSTRY
    </p>
    <div
      class="container mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
    >
      <HomeServiceCard
        v-for="item in items"
        :class="item.classname"
        :title="item.title"
        :desc="item.desc"
        icon=""
        :features="item.features"
      />
    </div>
  </section>
</template>

<script lang="ts" setup>
const props = defineProps<{industry:string}>();
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/industries/get-industry-solutions", {
  method: 'GET',
      params: {
        'industry': props.industry
      }
});
items.value = data.value
</script>
