<template>
  <section class="py-16 bg-gray-100">
    <h2 class="text-3xl text-center font-bold text-gray-800 mb-8">Ils nous font confiance</h2>
    <nuxtui-carousel :items="testimonials">
      <template #item="{item}">
        <blockquote class="p-6 bg-white rounded-lg shadow">
          "{{ item.quote }}"
          <footer class="mt-4 text-sm text-gray-500">— {{ item.author }}</footer>
        </blockquote>
      </template>
    </nuxtui-carousel>
  </section>
</template>

<script lang="ts" setup>
const testimonials = [
  { quote: "Super réactif et professionnel !", author: "Client A" },
  { quote: "Ils ont boosté notre projet digital.", author: "Client B" },
]
</script>
