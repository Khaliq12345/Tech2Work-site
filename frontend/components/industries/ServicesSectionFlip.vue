<template>
  <div id="services" class="pb-20 px-5 md:px-10 lg:px-20 text-center">
    <p class="text-xl md:text-3xl lg:text-4xl mb-15 font-bold text-gray-900 uppercase">
      EMPOWER YOUR PROJECT WITH ADVANCED CAPABILITIES
    </p>
    <div class="mt-8 flex flex-wrap gap-5 justify-center place-items-center">
      <IndustriesServiceCard
        v-for="item in items"
        :class="item.classname"
        :title="item.title"
        :desc="item.desc"
        :icon="item.icon"
        :features="[]"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps<{industry:string}>();
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/industries/get-industry-services", {
  method: 'GET',
      params: {
        'industry': props.industry
      }
});
items.value = data.value
</script>
