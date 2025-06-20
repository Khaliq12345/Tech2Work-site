<template>
  <NuxtLayout name="default">
    <IndustriesHeroSection :industry="industry" />
    <IndustriesTestimonialsSection :industry="industry" />
    <IndustriesTrustedSection
      :text="`Request a free one-hour consultation from our experts and
          get a detailed estimate`"
    />
    <IndustriesServicesSection :industry="industry" />
    <IndustriesSolutions :industry="industry" />
    <IndustriesServicesSectionFlip :industry="industry" />
    <IndustriesFeaturesSection :industry="industry" />
    <IndustriesReasonsSection :industry="industry" />
    <IndustriesTrustedSection
      :text="`Talk to our experts and find the best solution that suits your needs`"
    />
    <IndustriesProcess :industry="industry" />
    <TechStack />
    <FAQ />
    <Contact />
  </NuxtLayout>
</template>

<script lang="ts" setup>
const route = useRoute();

const industry = route.params.industry as string;
</script>
