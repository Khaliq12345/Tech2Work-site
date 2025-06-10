<template>
  <section id="services" class="py-20 bg-white text-center">
     <p class="text-3xl mb-10 font-bold text-gray-900">What We Offer to Accelerate Your Growth</p>
    <div class="container mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
      <ServiceCard title="Dév Web" icon="i-lucide-mail" />
      <ServiceCard title="Dév Mobile" icon="smartphone" />
      <ServiceCard title="IA & Data" icon="brain" />
      <ServiceCard title="IA & Data" icon="brain" />
    </div>
  </section>
</template>

<script lang="ts" setup>
import ServiceCard from '~/components/home/ServiceCard.vue'
</script>
