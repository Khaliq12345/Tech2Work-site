<template>
  <section id="services" class="py-20 bg-white text-center">
    <div class="container mx-auto grid grid-cols-1 gap-8 px-3">
      <PortfolioProjectCard
        class="bg-white text-black"
        v-for="item in items"
        :item="item"
      />
    </div>
  </section>
</template>

<script lang="ts" setup>
const { locale } = useI18n();
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/portfolio/get-portfolio-projects", {
  params: { locale: locale.value },
});
items.value = data.value;
</script>
