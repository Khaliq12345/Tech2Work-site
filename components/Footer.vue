<template>
  <div class="mt-8"></div>
  <!-- <footer class="bg-gray-100 py-10 mt-8">
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
  </footer> -->
  <!-- 
    -->
  <footer
    class="bg-black text-white font-bold text-sm pt-4 border-t border-white/10"
  >
    <div
      class="max-w-7xl mx-auto px-4 pb-6 flex flex-col items-center gap-3 text-center md:flex-row md:justify-between"
    >
      <!-- Legal Links -->
      <div class="flex flex-wrap justify-center gap-6">
        <NuxtLink to="/terms" class="hover:underline">TERMS OF USE</NuxtLink>
        <NuxtLink to="/privacy" class="hover:underline"
          >PRIVACY POLICY</NuxtLink
        >
        <NuxtLink to="/sitemap" class="hover:underline">SITEMAP</NuxtLink>
      </div>

      <!-- Social Icons -->
      <div class="flex gap-2 mt-2">
        <a
          v-for="icon in socialIcons"
          :key="icon.name"
          :href="icon.url"
          target="_blank"
          rel="noopener noreferrer"
          class="bg-white/10 hover:bg-white/20 p-2 rounded text-white"
        >
          <Icon :name="icon.name" class="w-4 h-4" />
        </a>
      </div>
    </div>

    <div class="text-center text-xs text-white/80 pb-4">
      © 2025 Tech2Work Agency, ALL RIGHTS RESERVED
    </div>
  </footer>
</template>

<script setup lang="ts">
const socialIcons = [
  { name: "mdi:facebook", url: "https://facebook.com" },
  { name: "mdi:twitter", url: "https://twitter.com" },
  { name: "mdi:youtube", url: "https://youtube.com" },
  { name: "mdi:instagram", url: "https://instagram.com" },
  { name: "mdi:linkedin", url: "https://linkedin.com" },
  { name: "mdi:briefcase-outline", url: "https://clutch.co" }, // clutch
  { name: "mdi:github", url: "https://github.com" },
  { name: "mdi:behance", url: "https://behance.net" },
];
</script>
