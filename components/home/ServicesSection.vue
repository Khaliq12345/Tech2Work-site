<template>
  <section id="services" class="py-16 bg-white">
    <div class="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
      <ServiceCard title="Dév Web" icon="web" />
      <ServiceCard title="Dév Mobile" icon="smartphone" />
      <ServiceCard title="IA & Data" icon="brain" />
    </div>
  </section>
</template>

<script lang="ts" setup>
import ServiceCard from '~/components/home/ServiceCard.vue'
</script>
