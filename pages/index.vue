<template>
  <NuxtLayout name="default">
    <HeroSection />
    <ServicesSection />
    <!-- <AboutSection />
    <TestimonialsSection />
    <ContactSection /> -->
    The rest of the page
  </NuxtLayout>

</template>

<script lang="ts" setup>
import HeroSection from '~/components/home/HeroSection.vue'
import ServicesSection from '~/components/home/ServicesSection.vue'
import AboutSection from '~/components/home/AboutSection.vue'
import TestimonialsSection from '~/components/home/TestimonialsSection.vue'
import ContactSection from '~/components/home/ContactSection.vue'
</script>
