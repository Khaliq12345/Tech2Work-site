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
      >
      </HomeTestimonialCard>
    </div>
    <!--  -->
    <div class="mt-5 container mx-auto flex flex-wrap lg:flex-nowrap gap-5">
      <HomeTestimonialCard
        v-for="item in items.slice(2, -1)"
        :quote="item.quote"
        :name="item.name"
        :role="item.role"
        :avatar="item.avatar"
        :class="item.class"
      >
      </HomeTestimonialCard>
    </div>
  </section>
</template>

<script lang="ts" setup>
import type { TestimonialType } from "~/interface/testimonialType";

const items: TestimonialType[] = [
  {
    quote: "Test Quote",
    name: "Test name",
    role: "Test role",
    avatar: "Test avatar",
    class: "Text class",
  },
  {
    quote: "Test Quote",
    name: "Test name",
    role: "Test role",
    avatar: "Test avatar",
    class: "Text class",
  },
  {
    quote: "Test Quote",
    name: "Test name",
    role: "Test role",
    avatar: "Test avatar",
    class: "Text class",
  },
  {
    quote: "Test Quote",
    name: "Test name",
    role: "Test role",
    avatar: "Test avatar",
    class: "Text class",
  },
  {
    quote: "Test Quote",
    name: "Test name",
    role: "Test role",
    avatar: "Test avatar",
    class: "Text class",
  },
  {
    quote: "Test Quote",
    name: "Test name",
    role: "Test role",
    avatar: "Test avatar",
    class: "Text class",
  },
];
</script>
