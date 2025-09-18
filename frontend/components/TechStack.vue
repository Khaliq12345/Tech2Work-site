<template>
  <section
    id="techstack"
    class="py-20 px-5 md:px-15 lg:px-30 bg-white text-center"
  >
    <!--  -->
    <UTabs :items="items" variant="link" class="" size="md">
      <template #leading="{ item }"> </template>
      <template #default="{ item }">
        <span
          class="text-xl md:text-3xl lg:text-4xl font-bold hover:text-gray-500"
          >{{ item.label }}</span
        >
      </template>
      <template #services="{ item }">
        <div class="mt-8 flex flex-wrap xl:flex-nowrap gap-5 justify-center">
          <div class="text-left flex-1/2">
            <h3 class="text-xl lg:text-3xl font-bold mb-2">
              {{ $t("teckstack_services_title") }}
            </h3>
            <p class="text-sm md:text-md lg:text-lg font-semibold">
              {{ $t("teckstack_services_desc") }}
            </p>
          </div>
          <!--  -->
          <HomeServiceCard
            v-for="item in servicesItems.slice(0, 1)"
            :class="item.classname"
            :title="
              $t(
                `teckstack_services_title_${item.title.replaceAll(' ', '_').toLowerCase()}`,
              ) ?? item.title
            "
            :desc="
              $t(
                `teckstack_services_desc_${item.title.replaceAll(' ', '_').toLowerCase()}`,
              ) ?? item.desc
            "
            :icon="item.icon"
            :features="[]"
          />
        </div>
        <!--  -->
        <div class="mt-8 flex flex-wrap lg:flex-nowrap gap-5 justify-center">
          <HomeServiceCard
            v-for="item in servicesItems.slice(1)"
            :class="item.classname"
            :title="
              $t(
                `teckstack_services_title_${item.title.replaceAll(' ', '_').toLowerCase()}`,
              ) ?? item.title
            "
            :desc="
              $t(
                `teckstack_services_desc_${item.title.replaceAll(' ', '_').toLowerCase()}`,
              ) ?? item.desc
            "
            :icon="item.icon"
            :features="[]"
          />
        </div>
      </template>
      <template #tech-stack="{ item }">
        <div class="mt-8 flex flex-wrap xl:flex-nowrap gap-5 justify-center">
          <div class="text-left flex-4/4">
            <h3 class="text-xl lg:text-3xl font-bold mb-2">
              {{ $t("teckstack_techs_title") }}
            </h3>
            <p class="text-sm md:text-md lg:text-lg font-semibold">
              {{ $t("teckstack_techs_desc") }}
            </p>
          </div>
          <!--  -->
          <HomeServiceCard
            v-for="item in techItems.slice(0, 2)"
            :class="item.classname"
            :title="
              $t(
                `teckstack_techs_title_${item.title.replaceAll(' ', '_').toLowerCase()}`,
              ) ?? item.title
            "
            :desc="
              $t(
                `teckstack_techs_desc_${item.title.replaceAll(' ', '_').toLowerCase()}`,
              ) ?? item.desc
            "
            :icon="item.icon"
            :features="[]"
          />
        </div>
        <!--  -->
        <div class="mt-8 flex flex-wrap lg:flex-nowrap gap-5 justify-center">
          <HomeServiceCard
            v-for="item in techItems.slice(2)"
            :class="item.classname"
            :title="
              $t(
                `teckstack_techs_title_${item.title.replaceAll(' ', '_').toLowerCase()}`,
              ) ?? item.title
            "
            :desc="
              $t(
                `teckstack_techs_desc_${item.title.replaceAll(' ', '_').toLowerCase()}`,
              ) ?? item.desc
            "
            :icon="item.icon"
            :features="[]"
          />
        </div>
      </template>
    </UTabs>
  </section>
</template>

<script setup lang="ts">
import type { TabsItem } from "@nuxt/ui";
const items = [
  {
    label: "Services",
    slot: "services" as const,
  },
  {
    label: "Tech stack",
    slot: "tech-stack" as const,
  },
] satisfies TabsItem[];
const servicesItems: Ref<any[]> = ref([]);
const techItems: Ref<any[]> = ref([]);
const { data } = await useFetch("/api/global/get-service-tech-stack");
const tmp = data.value as any;
servicesItems.value = tmp.filter((it: any) => it.type === "service");
techItems.value = tmp.filter((it: any) => it.type === "techstack");
</script>
