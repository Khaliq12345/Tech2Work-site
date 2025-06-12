<template>
  <div
    class="px-10 py-25 opacity-85"
    :style="`background-image: url(${bgimg}); `"
    style="background-repeat: no-repeat; background-size: cover"
  >
    <section class="text-left">
      <p class="text-6xl mb-3 font-bold text-white">{{ title }}</p>
      <p class="my-5 text-2xl text-white">{{ desc }}</p>
      <UModal>
        <!-- <UModal :fullscreen="true"  :overlay="true"> class="" :overlay="true" :ui="{ overlay: ' opacity-50 bg-black' }" -->
        <UButton
          class="font-bold bg-white hover:bg-amber-50 rounded-full text-black py-3 px-8 my-5 text-2xl"
          >Start With Us !</UButton
        >
        <template #content>
          <Placeholder class="h-48 m-4" />
          <!-- <HomeContact class="" /> -->
        </template>
      </UModal>
    </section>
    <div class="mt-8 flex flex-wrap md:flex-nowrap gap-5 justify-center">
      <UCard
        v-for="f in features"
        :key="f"
        variant="subtle"
        class="text-center bg-transparent text-white border-2 border-white flex-1/4 shadow-2xl"
      >
        <div class="flex items-center justify-start">
          <div class="text-left">
            <h3 class="text-3xl font-bold mb-2">{{ f.value }}</h3>
            <p class="font-semibold">{{ f.name }}</p>
          </div>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps<{ bgimg: string; title: string; desc: string; features: any[] }>();
</script>
