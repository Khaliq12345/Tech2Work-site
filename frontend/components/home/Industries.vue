<template>
  <section id="industries" class="py-20 px-6 md:px-15 bg-gray-200 text-center">
    <div class="text-left flex flex-wrap lg:flex-nowrap gap-y-4 mb-10">
      <h3 class="lg:flex-1/2 text-xl md:text-3xl lg:text-4xl font-bold mb-2 uppercase">
        We Provide IT Services to Various Industries
      </h3>
      <p class="text-sm md:text-md lg:text-xl font-semibold lg:flex-1/2">
        We create solutions to meet the demands of modern industries, where
        reliability, integration, and performance are non-negotiable. Our track
        record spans sectors like healthcare, logistics, finance, and
        manufacturing, giving us the context to solve for your edge cases, not
        just the obvious ones.
      </p>
    </div>
    <!--  -->

    <UCollapsible v-for="service in services"
          :key="service.name" class="lg:hidden my-4">
      <UButton
          
          :icon="service.icon"
          :label="service.name"
          variant="outline"
          class="justify-start w-full text-md md:text-xl font-semibold rounded-xl px-6 py-4"
          :class="{
            'bg-primary text-white border-primary':
              selected.name === service.name,
            'text-gray-800 border-gray-300 hover:bg-gray-100':
              selected.name !== service.name,
          }"
          @click="selectService(service)"
        />
      <template #content>
        <div
          class="grid grid-cols-1 gap-6 mt-3"
          :class="{ 'md:grid-cols-2': selected.samples.length != 0 }"
        >
          <p class="text-sm md:text-md leading-relaxed">
            {{ selected.description }}
          </p>
          <div v-if="selected.samples" class="flex flex-col gap-3">
            <span
              v-for="link in selected.samples"
              class="text-sm md:text-md font-medium text-white hover:text-gray-200"
            >
              {{ link }}
            </span>
          </div>
        </div>
      </template>
    </UCollapsible>

    <div class="lg:flex flex-col lg:flex-row gap-4 hidden">
      <!-- Sidebar -->
      <div class=" flex flex-col gap-4 w-full lg:w-1/3">
        <UButton
          v-for="service in services"
          :key="service.name"
          :icon="service.icon"
          :label="service.name"
          variant="outline"
          class="justify-start text-md md:text-xl font-semibold rounded-xl px-6 py-4"
          :class="{
            'bg-primary text-white border-primary':
              selected.name === service.name,
            'text-gray-800 border-gray-300 hover:bg-gray-100':
              selected.name !== service.name,
          }"
          @click="selectService(service)"
        />
      </div>
      <!-- Right content card -->
      <UCard
        class="w-full lg:w-2/3 lg:mt-0 mt-4 bg-gradient-to-bl from-black to-gray-400 text-white rounded-xl"
      >
        <h2 class="text-xl md:text-2xl font-bold underline underline-offset-4">
          {{ selected.name }}
        </h2>
        <USeparator class="p-4 md:p-8 border-white" color="neutral" />
        <div
          class="grid grid-cols-1 gap-6"
          :class="{ 'md:grid-cols-2': selected.samples.length != 0 }"
        >
          <p class="text-sm md:text-md leading-relaxed">
            {{ selected.description }}
          </p>
          <div v-if="selected.samples" class="flex flex-col gap-3">
            <span
              v-for="link in selected.samples"
              class="text-sm md:text-md font-medium text-white hover:text-gray-200"
            >
              {{ link }}
            </span>
          </div>
        </div>
      </UCard>
    </div>
  </section>
</template>

<script setup lang="ts">
import type { Service } from "~/interface/service";

const services: Ref<Service[]> = ref([]);
const { data } = await useFetch("/api/home/get-home-industries");
services.value = data.value as any;
const selected = ref<Service>(services.value[0]);
function selectService(service: Service) {
  selected.value = service;
}
</script>
