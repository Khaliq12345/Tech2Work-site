<template>
  <UCard variant="soft" class="p-y text-center shadow-2xl">
    <div class="flex flex-wrap lg:flex-nowrap items-center gap-x-5">
      <div class="lg:flex-1/2 text-left">
        <h3 class="text-xl md:text-2xl font-bold text-black mb-4">
          {{ item.title }}
        </h3>
        <p class="text-base text-gray-700 mb-4">
          {{ item.description }}
        </p>
        <!-- Location -->
        <div class="flex mt-4 items-center text-sm mb-3">
          <UIcon name="i-heroicons-map-pin" />
          <span class="font-semibold px-2"
            >{{ $t(`portfolio_project_card_location_label`) }} :
          </span>
          {{ item.location }}
        </div>
        <!-- Industries -->
        <div class="mb-3">
          <div class="flex flex-wrap gap-y-2 items-center text-sm mb-2">
            <UIcon name="i-lucide-box" />
            <span class="font-semibold px-2">Industries : </span>
            <div class="flex flex-wrap gap-2">
              <UBadge
                v-for="tech in item.industries"
                :key="tech"
                :label="tech"
                variant="outline"
                size="sm"
              />
            </div>
          </div>
        </div>
        <!-- Technologies -->
        <div class="mb-3">
          <div class="flex flex-wrap gap-y-2 items-center text-sm mb-2">
            <UIcon name="i-lucide-gpu" />
            <span class="font-semibold px-2">Technologies : </span>
            <div class="flex flex-wrap gap-2">
              <UBadge
                v-for="tech in item.technologies"
                :key="tech"
                :label="tech"
                variant="outline"
                size="sm"
              />
            </div>
          </div>
        </div>
      </div>
      <div
        class="lg:flex-1/2 lg:order-2 w-full items-center justify-center place-items-center rounded-b-lg lg:rounded-l-none lg:rounded-r-lg overflow-hidden"
      >
        <img
          :src="item.imgUrl"
          class="max-w-full h-50 object-contain rounded-lg shadow-md"
        />
      </div>
    </div>
  </UCard>
</template>

<script lang="ts" setup>
import type { CaseStudy } from "~/interface/caseStudy";
defineProps<{
  item: CaseStudy;
}>();
</script>
