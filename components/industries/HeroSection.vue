<template>
  <div
    class="opacity-85"
    :style="`background-image: url(${bgimg}); `"
    style="background-repeat: no-repeat; background-size: cover"
  >
    <div
      class="px-10 py-40 inset-0 bg-black/50 flex items-center justify-center z-50"
    >
      <section class="text-left">
        <p class="text-6xl mb-8 font-bold text-white">{{ title }}</p>
        <p class="mb-15 text-2xl text-white">{{ desc }}</p>
        <CustomModal class="bg-amber-400">
          <template #trigger>
            <UButton
              class="font-bold bg-white hover:bg-amber-50 rounded-full text-black py-5 px-10 text-2xl"
              >Start With Us !</UButton
            >
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
defineProps<{ bgimg: string; title: string; desc: string; features: any[] }>();
</script>
