<template>
  <section
    id="services"
    class="py-20 bg-gradient-to-br from-gray-300 to-gray-50 text-center"
  >
    <p class="text-4xl mb-20 font-bold text-gray-900 uppercase">
      Our clients and what they say
    </p>
    <div class="container mx-auto flex flex-wrap lg:flex-nowrap gap-5">
      <HomeTestimonialCard
        v-for="item in items.slice(0, 2)"
        :quote="item.quote"
        :name="item.name"
        :role="item.role"
        :avatar="item.avatar"
        :class="item.class"
      />
    </div>
    <!--  -->
    <div class="mt-5 container mx-auto flex flex-wrap lg:flex-nowrap gap-5">
      <HomeTestimonialCard
        v-for="item in items.slice(2)"
        :quote="item.quote"
        :name="item.name"
        :role="item.role"
        :avatar="item.avatar"
        :class="item.class"
      />
    </div>
  </section>
</template>

<script lang="ts" setup>
import type { TestimonialType } from "~/interface/testimonialType";

const items: TestimonialType[] = [
  {
    quote:
      "They were able to handle everything we threw at them fairly easily.",
    name: "Guy Jackson",
    role: "Lead Software Developer, D-BIT Systems Pty Ltd",
    avatar: "",
    class: "flex-3/5",
  },
  {
    quote:
      "They were able to handle everything we threw at them fairly easily.",
    name: "Guy Jackson",
    role: "Lead Software Developer, D-BIT Systems Pty Ltd",
    avatar: "",
    class: "flex-2/5",
  },
  {
    quote:
      "They were able to handle everything we threw at them fairly easily.",
    name: "Guy Jackson",
    role: "Lead Software Developer, D-BIT Systems Pty Ltd",
    avatar: "",
    class: "flex-2/5",
  },
  {
    quote:
      "They were able to handle everything we threw at them fairly easily.",
    name: "Guy Jackson",
    role: "Lead Software Developer, D-BIT Systems Pty Ltd",
    avatar: "",
    class: "flex-3/5",
  },
];
</script>
