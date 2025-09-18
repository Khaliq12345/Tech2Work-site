<template>
  <div class="mt-8"></div>
  <footer class="bg-gray-200 py-10 mt-8">
    <div
      class="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-sm text-gray-600 px-6"
    >
      <div>
        <div class="flex gap-3 flex-wrap xl:flex-nowrap">
          <img src="~/assets/imgs/logo2.png" class="rounded-full h-50" alt="" />
          <div class="">
            <h3 class="text-2xl font-bold text-black mb-3">Tech2Work Agency</h3>
            <p>
              {{ $t("footer_desc1") }}
            </p>
          </div>
        </div>
      </div>
      <div>
        <h4 class="text-black text-lg font-semibold mb-2">Navigation</h4>
        <UNavigationMenu
          orientation="vertical"
          :items="items"
          class="w-full justify-center"
          variant="link"
          color="error"
        >
        </UNavigationMenu>
      </div>
      <div>
        <h4 class="text-black text-lg font-semibold mb-2">Contacts</h4>
        <ul class="space-y-1 text-md">
          <li>
            <a
              href="mailto:contact@tech2work.tech"
              class="flex items-center gap-2 transition-colors"
            >
              <UIcon name="i-lucide-mail" class="size-4" /><span class="text-sm"
                >Email: contact@tech2work.tech</span
              >
            </a>
          </li>
          <li>
            <a
              href="tel:+2290162369889"
              class="flex items-center gap-2 transition-colors"
            >
              <UIcon name="i-lucide-phone" class="size-4" />
              <span class="font-semibold"> {{ $t("footer_phone") }} </span> :
              +229 0162369889
            </a>
          </li>
          <li class="flex font-semibold items-center gap-2 transition-colors">
            <UIcon name="i-lucide-locate" class="size-4" /> Cotonou, Bénin
          </li>
        </ul>
      </div>
    </div>
  </footer>
  <!-- -->
  <footer
    class="bg-black text-white font-bold text-sm pt-4 border-t border-white/10"
  >
    <div
      class="max-w-7xl mx-auto px-4 pb-6 flex flex-col items-center gap-3 text-center md:flex-row md:justify-between"
    >
      <!-- Legal Links -->
      <div class="flex flex-wrap justify-center gap-6">
        <NuxtLink :to="getLocalizedPath('/termsOfUse')" class="hover:underline"
          >{{ $t("footer_terms") }}
        </NuxtLink>
        <NuxtLink
          :to="getLocalizedPath('/privacyPolicy')"
          class="hover:underline"
          >{{ $t("footer_privacy") }}
        </NuxtLink>
      </div>

      <div class="text-center text-xs text-white/80">
        © 2025 Tech2Work Agency, {{ $t("footer_desc2") }}
      </div>

      <!-- Social Icons -->
      <div class="flex gap-2">
        <a
          v-for="icon in socialIcons"
          :key="icon.name"
          :href="icon.url"
          target="_blank"
          rel="noopener noreferrer"
          class="bg-white/10 hover:bg-white/20 p-3 rounded text-white"
        >
          <Icon :name="icon.name" class="w-4 h-4" />
        </a>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const { items } = useMenuItems();
const route = useRoute();
const socialIcons = [
  {
    name: "i-lucide-facebook",
    url: "https://www.facebook.com/profile.php?id=61577734741087",
  },
  { name: "i-lucide-twitter", url: "https://x.com/TechtwoW61533" },
  // { name: "i-lucide-youtube", url: "https://youtube.com" },
  // { name: "i-lucide-instagram", url: "https://instagram.com" },
  {
    name: "i-lucide-linkedin",
    url: "https://www.linkedin.com/in/techtwo-work-70b021372/",
  },
  // { name: "i-lucide-github", url: "https://github.com" },
];
</script>
