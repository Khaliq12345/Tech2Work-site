<template>
  <div class="min-h-screen  flex flex-col bg-white text-gray-900">
    <Header />
    <main>
      <slot />
    </main>
    <Footer />
  </div>
</template>

<script lang="ts" setup>
import Header from '~/components/Header.vue'
import Footer from '~/components/Footer.vue'
</script>
