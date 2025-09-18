<script setup lang="ts"></script>

<template>
  <section id="industries" class="py-20 px-10 md:px-15 bg-gray-200 text-center">
    <div class="flex flex-wrap md:flex-nowrap justify-center items-center">
      <div class="text-left mb-10 md:flex-1/2">
        <h3 class="text-xl md:text-2xl lg:text-3xl font-bold md:mb-2 uppercase">
          {{ $t("home_trusted_title1") }}
        </h3>
        <h3 class="text-xl md:text-2xl lg:text-3xl font-bold mb-5 uppercase">
          {{ $t("home_trusted_title2") }}
        </h3>
        <p class="text-md md:text-xl font-semibold">
          {{ $t("home_trusted_desc") }}
        </p>
        <CustomModal>
          <template #trigger>
            <UButton
              icon="i-heroicons-arrow-right"
              trailing
              color="primary"
              class="text-white text-md md:text-xl rounded-3xl py-3 px-6 mt-10"
              variant="solid"
              :label="$t('cta_get_quote')"
            />
          </template>
          <template #content>
            <RequestProposal />
          </template>
        </CustomModal>
      </div>
      <!--  -->
      <div class="md:flex-1/2 place-items-center">
        <img
          src="https://static.vecteezy.com/system/resources/previews/010/385/335/non_2x/technology-partners-icon-illustration-vector.jpg"
          class="rounded-full h-50 md:h-80"
          alt=""
        />
      </div>
    </div>
  </section>
</template>

<style scoped></style>
