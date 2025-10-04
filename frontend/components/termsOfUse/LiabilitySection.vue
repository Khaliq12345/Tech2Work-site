<template>
  <div class="bg-white px-5 md:px-15 pt-10 pb-10 lg:pb-20">
    <section class="text-left">
      <p
        class="pt-3 text-xl md:text-2xl lg:text-3xl mb-3 font-bold text-gray-900"
      >
        {{ $t("term_of_use_liability_title") }}
      </p>
      <p class="my-5 text-sm lg:text-lg text-gray-700">
        Tech2Work Agency {{ $t("term_of_use_liability_desc1") }} :
      </p>
      <div v-for="f in liabLst" class="flex items-center my-4">
        <UIcon name="i-lucide-circle-check-big" size="20" class="mr-5" />
        {{ f.value }}
      </div>
      <p class="font-bold my-10">
        {{ $t("term_of_use_liability_desc2") }}
      </p>
    </section>
  </div>
</template>

<script setup lang="ts">
const { locale } = useI18n();
const liabLst: Ref<any> = ref([]);
const { data } = await useFetch("/api/global/get-terms-of-use-liability", {
  params: { locale: locale.value },
});
liabLst.value = data.value;
</script>
