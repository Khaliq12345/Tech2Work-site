<template>
  <section id="industries" class="pt-20 px-10 md:px-15 text-center">
    <div class="text-left gap-y-4 mb-10">
      <h3 class="text-3xl font-bold mb-4 uppercase">
        OUR CUSTOM HEALTHCARE SOFTWARE DEVELOPMENT PROCESS
      </h3>
      <p class="text-xl font-semibold">
        Here’s what the software development lifecycle will look like for your
        tailored healthcare software development solutions.
      </p>
    </div>
    <!--  -->
    <div class="flex flex-col lg:flex-row gap-4">
      <!-- Sidebar -->
      <div class="flex flex-col gap-4 w-full lg:w-1/3">
        <UButton
          v-for="service in processes"
          :key="service.name"
          :label="service.name"
          variant="outline"
          class="justify-start text-xl font-semibold rounded-xl px-6 py-4"
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
        <h2 class="text-2xl font-bold underline underline-offset-4">
          {{ selected.name }}
        </h2>
        <USeparator class="p-8 border-white" color="neutral" />
        <div class="grid grid-cols-1 gap-6">
          <p class="text-md leading-relaxed">
            {{ selected.description }}
          </p>
        </div>
      </UCard>
    </div>
  </section>
</template>

<script setup lang="ts">
const props = defineProps<{ processes: any[] }>();

const selected = ref(props.processes[0]);

function selectService(service: any) {
  selected.value = service;
}
</script>
