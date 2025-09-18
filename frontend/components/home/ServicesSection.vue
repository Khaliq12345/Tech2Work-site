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
        :title="
          $t(
            `home_services_title_${item.title.replaceAll(' ', '_').toLowerCase()}`,
          )
        "
        :desc="
          $t(
            `home_services_desc_${item.title.replaceAll(' ', '_').toLowerCase()}`,
          )
        "
        :icon="item.icon"
        :features="
          item.features.map((f: any, i: any) =>
            $t(
              `home_services_feature_${item.title.replaceAll(' ', '_').toLowerCase()}_${i}`,
            ),
          )
        "
      />
    </div>
  </section>
</template>

<script lang="ts" setup>
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/home/get-home-services");
items.value = data.value;
</script>
