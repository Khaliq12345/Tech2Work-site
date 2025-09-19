<template>
  <div class="container mx-auto w-full shadow-xl">
    <UCollapsible>
      <UButton
        color="neutral"
        class="p-10 font-bold text-xl md:text-2xl uppercase w-full"
      >
        {{ $t("home_process_title") }}
      </UButton>
      <template #content>
        <div class="p-10 gap-5 flex flex-col">
          <div v-for="item in items">
            <h3 class="font-bold text-base md:text-xl mb-1">
              {{ item.title }}
            </h3>
            <p class="text-sm md:text-lg">
              {{ item.content }}
            </p>
          </div>
        </div>
      </template>
    </UCollapsible>
  </div>
</template>

<script setup lang="ts">
const { locale } = useI18n();
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/home/get-home-process", {
  params: { locale: locale.value },
});
items.value = data.value;
</script>
