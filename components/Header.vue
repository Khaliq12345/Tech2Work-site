<template>
  <header class="sticky top-0 z-50 bg-white shadow">
    <!-- Top Line -->
    <div
      class="px-5 py-3 bg-black flex flex-wrap justify-center text-center text-white"
    >
      <div class="pl-3">Start building your software today. Book a call</div>
     
      <div class="flex pt-2 md:pt-0">
        <a
          href="mailto:tech2work@gmail.com"
          class="flex items-center gap-2 pl-10 transition-colors"
        >
          <UIcon name="i-lucide-mail" class="size-4" /> tech2work@gmail.com
        </a>
        <a
          href="tel:+2290198988765"
          class="flex items-center gap-2 px-5 transition-colors"
        >
          <UIcon name="i-lucide-phone" class="size-4" /> +229 0198988765
        </a>
      </div>
    </div>
    <!-- Nav Bar -->
    <nav class="container mx-auto flex items-center justify-between py-4 px-3">
      <NuxtLink to="/" class="text-2xl font-bold text-black">
        Tech2Work<span class="text-gray-600">Agency</span>
      </NuxtLink>
      <!-- Mobile Trigger -->
      <UButton
        @click="isMobileSidebarOpen = true"
        :disabled="isMobileSidebarOpen"
        class="bg-gray-100 hover:bg-gray-300 lg:hidden cursor-pointer"
      >
        <UIcon
          name="i-heroicons-bars-3-bottom-left-20-solid"
          class="mr-3 text-2xl"
        />
      </UButton>
      <!-- Desktop View -->
      <ul
        class="hidden lg:flex items-center gap-8 text-sm font-medium text-gray-700"
      >
        <UNavigationMenu :items="items" class="w-full justify-center" />
      </ul>
      <!-- Mobile Drawer -->
      <UDrawer
        direction="left"
        v-model:open="isMobileSidebarOpen"
        class="w-10/12 sm:w-6/12 bg-white"
      >
        <template #title>
          <p class="text-2xl font-bold text-black">
            Tech2Work<span class="text-gray-600">Agency</span>
          </p>
        </template>
        <template #description> Welcome Here</template>
        <template #body>
          <USeparator class="py-3 mb-3" />
          <UNavigationMenu
            orientation="vertical"
            :items="items"
            class="w-full justify-center"
          />
        </template>
      </UDrawer>
    </nav>
  </header>
</template>

<script setup lang="ts">
const isMobileSidebarOpen = ref(false);
const { items } = useMenuItems();
</script>
