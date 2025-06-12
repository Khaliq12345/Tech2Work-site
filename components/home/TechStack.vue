<template>
  <section
    id="techstack"
    class="py-20 px-10 md:px-15 lg:px-30 bg-white text-center"
  >
    <!--  -->
    <UTabs :items="items" variant="link" class="" size="md">
      <template #leading="{ item }"> </template>
      <template #default="{ item }">
        <span class="text-4xl font-bold hover:text-gray-500">{{
          item.label
        }}</span>
      </template>
      <template #services="{ item }">
        <div class="mt-8 flex flex-wrap xl:flex-nowrap gap-5 justify-center">
          <div class="text-left flex-1/2">
            <h3 class="text-3xl font-bold mb-2">
              WE STILL BUILD CUSTOM SOFTWARE. JUST 2.5х FASTER NOW
            </h3>
            <p class="text-lg font-semibold">
              We asked what was slowing our teams down. The issue was in
              friction: tool-switching, lost flow, and duplicated work. So, we
              made Cursor AI part of our core engineering infrastructure. We
              trained our developers to use it deeply. Fully embedded in our
              process, Cursor lets us ship with fewer delays, less overhead, and
              more confidence in every release.
            </p>
          </div>
          <!--  -->
          <HomeServiceCard
            v-for="item in servicesItems.slice(0, 1)"
            :class="item.class"
            :title="item.title"
            :desc="item.desc"
            :icon="item.icon"
            :features="[]"
          />
        </div>
        <!--  -->
        <div class="mt-8 flex flex-wrap lg:flex-nowrap gap-5 justify-center">
          <HomeServiceCard
            v-for="item in servicesItems.slice(1)"
            :class="item.class"
            :title="item.title"
            :desc="item.desc"
            :icon="item.icon"
            :features="[]"
          />
        </div>
      </template>
      <template #tech-stack="{ item }">
        <div class="mt-8 flex flex-wrap xl:flex-nowrap gap-5 justify-center">
          <div class="text-left flex-4/4">
            <h3 class="text-3xl font-bold mb-2">
              The Technology Platforms We Use
            </h3>
            <p class="text-lg font-semibold">
              We build robust solutions aligned with your client's business
              goals, using any tech stack you need. Our tech-agnostic experts
              speak every language (Python, React, and more!) and embrace
              cutting-edge tech to keep you ahead. From ideation to launch, we
              handle it all, saving you time and hassle.
            </p>
          </div>
          <!--  -->
          <HomeServiceCard
            v-for="item in techItems.slice(0, 2)"
            :class="item.class"
            :title="item.title"
            :desc="item.desc"
            :icon="item.icon"
            :features="[]"
          />
        </div>
        <!--  -->
        <div class="mt-8 flex flex-wrap lg:flex-nowrap gap-5 justify-center">
          <HomeServiceCard
            v-for="item in techItems.slice(2)"
            :class="item.class"
            :title="item.title"
            :desc="item.desc"
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

const servicesItems = [
  {
    class: "text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
  {
    class: "flex-2/4 text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
  {
    class: "flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
  {
    class: "flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
];
const techItems = [
  {
    class: "flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
  {
    class: "flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
  {
    class: "flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
  {
    class: "flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
  {
    class: "flex-2/4 text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
  },
];
</script>
