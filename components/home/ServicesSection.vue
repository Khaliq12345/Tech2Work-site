<template>
  <section id="services" class="py-20 bg-white text-center">
    <p class="text-4xl mb-20 font-bold text-gray-900 uppercase">
      What We Offer to Accelerate Your Growth
    </p>
    <div
      class="container mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
    >
      <HomeServiceCard
        v-for="item in items"
        :class="item.class"
        :title="item.title"
        :desc="item.desc"
        :icon="item.icon"
        :features="item.features"
      />
    </div>
  </section>
</template>

<script lang="ts" setup>
const items = [
  {
    class: " bg-gradient-to-br from-white to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
    features: [
      "End-to-end product development",
      "Business analysis and solution design",
      "Scalable MVP and beyond",
    ],
  },
  {
    class: " bg-gradient-to-br from-white to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
    features: [
      "End-to-end product development",
      "Business analysis and solution design",
      "Scalable MVP and beyond",
    ],
  },
  {
    class: "bg-gradient-to-br from-white to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
    features: [
      "End-to-end product development",
      "Business analysis and solution design",
      "Scalable MVP and beyond",
    ],
  },
  {
    class: "text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
    features: [
      "End-to-end product development",
      "Business analysis and solution design",
      "Scalable MVP and beyond",
    ],
  },
  {
    class: "text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
    features: [
      "End-to-end product development",
      "Business analysis and solution design",
      "Scalable MVP and beyond",
    ],
  },
  {
    class: "text-white bg-gradient-to-br from-black to-gray-400",
    title: "Product Development",
    desc: "Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
    icon: "i-lucide-mail",
    features: [
      "End-to-end product development",
      "Business analysis and solution design",
      "Scalable MVP and beyond",
    ],
  },
];
</script>
