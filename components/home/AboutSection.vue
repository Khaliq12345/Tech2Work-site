<template>
  <section id="about" class="py-20 bg-gray-50">
    <div class="container mx-auto text-center">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">Qui sommes-nous ?</h2>
      <p class="text-gray-700 max-w-3xl mx-auto mb-10">
        Chez <strong>Tech2Work Agency</strong>, nous transformons vos idées en solutions digitales sur mesure.
        De la conception au déploiement, notre équipe vous accompagne pour atteindre vos objectifs technologiques.
      </p>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-10">
        <StatCard title="+8 ans" subtitle="d'expérience" icon="calendar" />
        <StatCard title="30+" subtitle="projets réalisés" icon="layout-grid" />
        <StatCard title="100%" subtitle="clients satisfaits" icon="smile" />
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
import StatCard from '~/components/home/StatCard.vue'
</script>
