<template>
  <div id="services" class="py-20 px-5 md:px-10 lg:px-20 text-center">
    <p
      class="text-xl md:text-3xl lg:text-4xl mb-15 font-bold text-gray-900 uppercase"
    >
      OUR VALUES
    </p>
    <div class="mt-8 flex flex-wrap gap-5 justify-center place-items-center">
      <AboutServiceCard
        v-for="item in items"
        class=""
        :title="item.title"
        :desc="item.desc"
        :icon="item.icon"
        :features="[]"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/about/get-about-value");
items.value = data.value
</script>
