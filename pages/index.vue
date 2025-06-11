<template>
  <NuxtLayout name="default">
    <HeroSection />
    <ServicesSection />
    <TestimonialsSection />
    <!-- <TechStack />
    <Industries /> -->
    <AboutSection />
    <ContactSection />
    The rest of the page
  </NuxtLayout>

</template>

<script lang="ts" setup>
import HeroSection from '~/components/home/HeroSection.vue'
import ServicesSection from '~/components/home/ServicesSection.vue'
import AboutSection from '~/components/home/AboutSection.vue'
import TestimonialsSection from '~/components/home/TestimonialsSection.vue'
import TechStack from '~/components/home/TechStack.vue'
import Industries from '~/components/home/Industries.vue'
import ContactSection from '~/components/home/ContactSection.vue'
</script>
