<template>
  <section id="services" class="py-20 bg-white text-center">
    <p
      class="text-xl md:text-2xl lg:text-3xl mb-20 font-bold text-gray-900 uppercase"
    >
      {{ $t("home_services_title") }}
    </p>
    <div
      class="container mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 px-3"
    >
      <HomeServiceCard
        v-for="item in items"
        :class="item.classname"
        :title="item.title"
        :desc="item.description"
        :icon="item.icon"
        :features="item.features"
      />
    </div>
  </section>
</template>

<script lang="ts" setup>
const { locale } = useI18n();
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/home/get-home-services", {
  params: { locale: locale.value },
});
items.value = data.value;
</script>
