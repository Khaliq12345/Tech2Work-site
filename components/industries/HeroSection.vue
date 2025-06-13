<template>
  <div
    class="px-10 py-45 opacity-85"
    :style="`background-image: url(${bgimg}); `"
    style="background-repeat: no-repeat; background-size: cover"
  >
    <section class="text-left">
      <p class="text-6xl mb-8 font-bold text-white">{{ title }}</p>
      <p class="mb-15 text-2xl text-white">{{ desc }}</p>
      <UModal>
        <!-- <UModal :fullscreen="true"  :overlay="true"> class="" :overlay="true" :ui="{ overlay: ' opacity-50 bg-black' }" -->
        <UButton
          class="font-bold bg-white hover:bg-amber-50 rounded-full text-black py-5 px-10 my-5 text-2xl"
          >Start With Us !</UButton
        >
        <template #content>
          <Placeholder class="h-48 m-4" />
          <!-- <HomeContact class="" /> -->
        </template>
      </UModal>
    </section>
  </div>
</template>

<script lang="ts" setup>
defineProps<{ bgimg: string; title: string; desc: string; features: any[] }>();
</script>
