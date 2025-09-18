<template>
  <div id="services" class="py-20 px-5 md:px-10 lg:px-20 text-center">
    <p
      class="text-xl md:text-2xl lg:text-3xl mb-15 font-bold text-gray-900 uppercase"
    >
      {{ $t("about_value_title") }}
    </p>
    <UCollapsible v-for="item in items" class="md:hidden my-4">
      <UButton
        :icon="item.icon"
        :label="
          $t(
            `about_values_title_${item.title.replaceAll(' ', '_').toLowerCase()}`,
          ) ?? item.title
        "
        variant="outline"
        class="justify-start w-full text-md md:text-xl font-semibold rounded-xl px-6 py-4 text-gray-800 border-gray-300 hover:bg-gray-100"
      />
      <template #content>
        <div>
          <p class="font-semibold my-2">
            {{
              $t(
                `about_values_desc_${item.title.replaceAll(" ", "_").toLowerCase()}`,
              ) ?? item.desc
            }}
          </p>
        </div>
      </template>
    </UCollapsible>

    <div
      class="mt-8 hidden md:flex md:flex-wrap gap-5 justify-center place-items-center"
    >
      <AboutServiceCard
        v-for="item in items"
        class=""
        :title="
          $t(
            `about_values_title_${item.title.replaceAll(' ', '_').toLowerCase()}`,
          ) ?? item.title
        "
        :desc="
          $t(
            `about_values_desc_${item.title.replaceAll(' ', '_').toLowerCase()}`,
          ) ?? item.desc
        "
        :icon="item.icon"
        :features="[]"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
const items: Ref<any> = ref([]);
const { data } = await useFetch("/api/about/get-about-value");
items.value = data.value;
</script>
