<template>
  <footer class="bg-gray-100 py-12 mt-12">
    <div class="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-sm text-gray-600 px-6">
      <div>
        <h3 class="text-lg font-semibold text-black mb-3">Tech2Work Agency</h3>
        <p>
          Nous construisons des solutions web et mobiles performantes pour faire grandir votre entreprise.
        </p>
      </div>

      <div>
        <h4 class="text-black font-semibold mb-2">Navigation</h4>
        <ul class="space-y-1">
          <li><NuxtLink to="#services">Services</NuxtLink></li>
          <li><NuxtLink to="#about">À propos</NuxtLink></li>
          <li><NuxtLink to="#contact">Contact</NuxtLink></li>
        </ul>
      </div>

      <div>
        <h4 class="text-black font-semibold mb-2">Contact</h4>
        <ul class="space-y-1">
          <li>Email : contact@tech2work.com</li>
          <li>Tél : +229 00 00 00 00</li>
          <li>Cotonou, Bénin</li>
        </ul>
      </div>
    </div>

    <div class="mt-10 text-center text-xs text-gray-400">
      &copy; {{ new Date().getFullYear() }} Tech2Work Agency. Tous droits réservés.
    </div>
  </footer>
</template>

<script lang="ts" setup>
</script>
