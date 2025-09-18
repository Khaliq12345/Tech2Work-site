<template>
  <div class="flex flex-wrap gap-8 container mx-auto">
    <UCard
      class="col-span-1 lg:col-span-2 shadow-xl p-0 md:p-3 lg:p-4 flex flex-col justify-center w-full bg-gradient-to-br from-black to-gray-400"
    >
      <div class="flex flex-wrap lg:flex-nowrap justify-center gap-5">
        <!--  -->
        <div
          class="bg-white text-black shadow-md rounded-xl p-8 w-full space-y-6 lg:flex-1/2"
        >
          <h2 class="text-xl md:text-2xl font-bold uppercase leading-tight">
            {{ $t("request_proposal_title1") }}
          </h2>
          <p class=" ">{{ $t("request_proposal_title2") }}</p>
          <ContactForm />
          <p class="mt-2 text-md">
            {{ $t("request_proposal_title3") }}
          </p>
        </div>
        <!--  -->
        <div class="hidden lg:block space-y-6 lg:flex-1/2 text-center px-10">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
            {{ $t("request_proposal_title4") }}
          </h2>
          <p class="text-gray-600 dark:text-gray-300 text-base mb-15">
            {{ $t("request_proposal_title5") }}
          </p>
          <div
            v-for="f in features"
            :key="f"
            class="flex text-left items-center my-4"
          >
            <UIcon name="i-lucide-circle-check-big" size="20" class="mr-5" />
            {{ f }}
          </div>
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
const features = [
  $t("request_proposal_feature1"),
  $t("request_proposal_feature2"),
  $t("request_proposal_feature3"),
  $t("request_proposal_feature4"),
  $t("request_proposal_feature5"),
];
</script>
