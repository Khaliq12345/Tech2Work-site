<template>
  <section id="industries" class="py-20 px-10 md:px-15 bg-gray-200 text-center">
    <div class="text-left flex flex-wrap lg:flex-nowrap gap-y-4 mb-10">
      <h3 class="lg:flex-1/2 text-4xl font-bold mb-2 uppercase">
        We Provide IT Services to Various Industries
      </h3>
      <p class="text-xl font-semibold lg:flex-1/2">
        We create solutions to meet the demands of modern industries, where
        reliability, integration, and performance are non-negotiable. Our track
        record spans sectors like healthcare, logistics, finance, and
        manufacturing, giving us the context to solve for your edge cases, not
        just the obvious ones.
      </p>
    </div>
    <!--  -->
    <div class="flex flex-col lg:flex-row gap-4">
      <!-- Sidebar -->
      <div class="flex flex-col gap-4 w-full lg:w-1/3">
        <UButton
          v-for="service in services"
          :key="service.name"
          :icon="service.icon"
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
        <div
          class="grid grid-cols-1 gap-6"
          :class="{ 'md:grid-cols-2': selected.links.length != 0 }"
        >
          <p class="text-md leading-relaxed">
            {{ selected.description }}
          </p>
          <div v-if="selected.links" class="flex flex-col gap-3">
            <ULink
              v-for="(link, index) in selected.links"
              :key="index"
              :to="link.url"
              class="underline font-medium text-white hover:text-gray-200"
            >
              {{ link.text }}
            </ULink>
          </div>
        </div>
      </UCard>
    </div>
  </section>
</template>

<script setup lang="ts">
import type { Service } from "~/interface/service";

const services: Service[] = [
  {
    name: "Development",
    icon: "i-lucide-code-xml",
    description:
      "We offer custom software development tailored to your needs, from web platforms and mobile apps to backend systems — scalable, secure, and optimized for performance.",
    links: [],
  },
  {
    name: "Data Analysis",
    icon: "i-lucide-database-zap",
    description:
      "Transform raw data into actionable insights using advanced analytics, dashboards, and reporting tools. Make smarter decisions powered by your own data.",
    links: [],
  },
  {
    name: "AI Automation",
    icon: "i-lucide-bot",
    description:
      "Boost efficiency with AI-powered automation: chatbots, intelligent workflows, predictive systems, and learning platforms using NLP and machine learning.",
    links: [
      { text: "E-learning Software Development", url: "#" },
      { text: "LMS Development", url: "#" },
      { text: "School Management Software Development", url: "#" },
    ],
  },
  {
    name: "Optimisation",
    icon: "i-lucide-sun",
    description:
      "Improve system performance, reduce costs, and enhance user experience with our optimization services — from infrastructure tuning to UX improvements.",
    links: [],
  },
];

const selected = ref<Service>(services[2]); // Default to "Education"

function selectService(service: Service) {
  selected.value = service;
}
</script>

<style scoped>
/* Optionnel : améliore le style du focus clavier */
button:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}
</style>
