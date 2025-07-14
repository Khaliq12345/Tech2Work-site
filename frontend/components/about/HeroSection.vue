<template>
  <div
    class="opacity-85"
    :style="`background-image: url('https://nexttech-tt.com/wp-content/uploads/2022/03/About-Us.jpg'); `"
    style="background-repeat: no-repeat; background-size: cover"
  >
    <div
      class="px-5 md:px-10 py-25 md:py-30 lg:py-40 inset-0 bg-black/50 flex items-center justify-center z-50"
    >
      <section class="text-left">
        <p class="text-xl md:text-3xl lg:text-5xl mb-8 font-bold text-white">
          ABOUT US
        </p>
        <p class="mb-15 text-xl md:text-2xl text-white">A trusted technology partner, driven by innovation and a passion for cutting-edge solutions.</p>
        <CustomModal>
          <template #trigger>
            <UButton
              class="font-bold bg-white hover:bg-amber-50 rounded-full text-black py-5 px-10 text-md md:text-xl lg:text-2xl"
            >
              Become Part or our team
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
</script>
