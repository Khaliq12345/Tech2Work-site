<template>
  <div id="services" class="mb-20 px-5 md:px-10 lg:px-20 text-center">
    <p class="text-xl md:text-3xl lg:text-4xl mb-8 font-bold text-gray-900 uppercase">
      WHY TECH2WORK FOR THIS DEVELOPMENT ?
    </p>
    <div class="mt-10 gap-5 justify-center place-items-center">
      <UAccordion :items="items">
          <template #default="{ item }">
            <span class="text-xl md:text-2xl font-bold">{{ item.title }}</span>
          </template>
          <template #content="{ item }">
            <p class="text-left my-2">
              {{ item.content }}
            </p>
          </template>
        </UAccordion>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps<{industry:string}>();
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/industries/get-industry-reasons", {
  method: 'GET',
      params: {
        'industry': props.industry
      }
});
items.value = data.value
</script>
