<template>
  <div id="services" class="mb-20 px-10 lg:px-20 text-center">
    <p class="text-4xl mb-8 font-bold text-gray-900 uppercase">
      WHY TECH2WORK FOR THIS DEVELOPMENT ?
    </p>
    <div class="mt-10 gap-5 justify-center place-items-center">
      <UAccordion :items="items">
          <template #default="{ item }">
            <span class="text-2xl font-bold">{{ item.title }}</span>
          </template>
          <template #content="{ item }">
            <p class="text-left">
              {{ item.content }}
            </p>
          </template>
        </UAccordion>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps<{ items: any[] }>();
</script>
