<template>
  <div
    class="opacity-85"
    :style="`background-image: url('${bgimg}'); `"
    style="background-repeat: no-repeat; background-size: cover"
  >
    <div
      class="px-5 md:px-10 py-20 md:py-30 lg:py-40 inset-0 bg-black/50 flex items-center justify-center z-50"
    >
      <section class="text-left">
        <p class="text-2xl md:text-4xl lg:text-6xl mb-8 font-bold text-white">
          {{ title }}
        </p>
        <p class="mb-15 text-xl md:text-2xl text-white">{{ desc }}</p>
        <CustomModal>
          <template #trigger>
            <UButton
              class="font-bold bg-white hover:bg-amber-50 rounded-full text-black py-5 px-10 text-md md:text-xl lg:text-2xl"
            >
              Start With Us !
            </UButton>
          </template>
          <template #content>
            <RequestProposal />
          </template>
        </CustomModal>
      </section>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps<{ industry: string }>();
const bgimg = ref();
const title = ref();
const desc = ref();
const { data } = await useFetch("/api/industries/get-industry-details", {
  method: "GET",
  params: {
    industry: props.industry,
  },
});
bgimg.value = data.value[0].bgimg;
title.value = data.value[0].title;
desc.value = data.value[0].desc;
</script>
