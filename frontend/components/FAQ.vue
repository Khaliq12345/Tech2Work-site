<template>
  <section id="industries" class="py-20 px-5 md:px-10 lg:px-15 bg-gray-200 text-center">
    <div class="text-left flex flex-wrap lg:flex-nowrap gap-y-5 mb-10">
      <h3 class="lg:flex-1/4 text-xl md:text-3xl lg:text-4xl font-bold mb-5 uppercase">
        Frequently Asked Questions
      </h3>
      <div class="w-full lg:flex-1/2 justify-center place-items-center">
        <UAccordion :items="items">
          <template #default="{ item }">
            <span class="text-xl md:text-2xl font-bold">{{ item.label }}</span>
          </template>
          <template #content="{ item }">
            <p class="text-left my-2">
              {{ item.content }}
            </p>
          </template>
        </UAccordion>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const items: Ref<any[]> = ref([]);
const { data } = await useFetch("/api/global/get-faq");
items.value = data.value as any;
</script>
