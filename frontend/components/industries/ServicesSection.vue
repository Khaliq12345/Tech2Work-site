<template>
  <div id="services" class="pt-20 px-5 md:px-10 lg:px-20 text-center">
    <p class="text-xl md:text-3xl lg:text-4xl mb-8 font-bold text-gray-900 uppercase">
      SERVICES WE PROVIDE IN THIS INDUSTRY
    </p>
    <div
      class="mt-8 grid md:grid-cols-2 lg:grid-cols-3 gap-5 justify-center place-items-center"
    >
      <UCard
        v-for="item in items"
        variant="soft"
        class="bg-white text-left shadow-2xl"
        :class="item.class"
      >
        <UIcon :name="item.icon" size="50" class="py-2" />
        <div class="flex items-center justify-start">
          <div class="text-left">
            <h3 class="text-xl md:text-2xl font-bold mb-2">{{ item.title }}</h3>
            <p class="font-semibold">{{ item.desc }}</p>
          </div>
        </div>
      </UCard>
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
