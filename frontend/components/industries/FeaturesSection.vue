<template>
  <div id="services" class="mb-20 px-5 md:px-10 lg:px-20 text-center">
    <p class="text-xl md:text-3xl lg:text-4xl mb-8 font-bold text-gray-900 uppercase">
      SOFTWARE FEATURES WE BUILD
    </p>
    <div
      class="mt-10 grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5 justify-center place-items-center"
    >
      <UCard
        v-for="item in items"
        variant="soft"
        class="text-white bg-gradient-to-br from-black to-gray-300 text-left shadow-2xl"
        :class="item.class"
      >
        <UIcon :name="item.icon" size="50" class="py-2" />
        <div class="flex items-center justify-start">
          <div class="text-left">
            <h3 class="text-xl md:text-2xl font-semibold mt-3 mb-2">{{ item.title }}</h3>
          </div>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps<{ items: any[] }>();
</script>
