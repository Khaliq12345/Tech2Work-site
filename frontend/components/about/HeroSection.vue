<template>
  <div
    class="opacity-85"
    :style="`background-image: url('bg2.jpg'); `"
    style="background-repeat: no-repeat; background-size: cover"
  >
    <div
      class="px-5 md:px-10 py-25 md:py-30 lg:py-40 inset-0 bg-black/50 flex items-center justify-center z-50"
    >
      <section class="text-left">
        <p class="text-xl md:text-3xl lg:text-5xl mb-8 font-bold text-white">
          {{ $t("about_hero_section_title1") }}
        </p>
        <p class="mb-15 text-xl md:text-2xl text-white">
          {{ $t("about_hero_section_title2") }}
        </p>
        <CustomModal>
          <template #trigger>
            <UButton
              class="font-bold bg-white hover:bg-amber-50 rounded-full text-black py-5 px-10 text-md md:text-xl lg:text-2xl"
            >
              {{ $t("cta_become_part") }}
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

<script lang="ts" setup></script>
