<template>
  <header class="sticky top-0 z-50 bg-white shadow">
    <!-- Top Line -->
    <div
      class="px-5 py-3 text-sm md:text-md bg-black hidden md:flex flex-wrap justify-center text-center text-white"
    >
      <div class="pl-3">{{ $t("header_title_1") }}</div>

      <div class="flex flex-wrap justify-center pt-2 md:pt-0">
        <a
          href="mailto:contact@tech2work.tech"
          class="flex items-center gap-2 pl-10 transition-colors"
        >
          <UIcon name="i-lucide-mail" class="size-4" /> contact@tech2work.tech
        </a>
        <a
          href="tel:+2290162369889"
          class="flex items-center gap-2 px-5 transition-colors"
        >
          <UIcon name="i-lucide-phone" class="size-4" /> +229 0162369889
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
        <UNavigationMenu
          :items="items"
          class="w-full justify-center"
          variant="link"
          color="error"
        >
        </UNavigationMenu>
        <LanguageSelector />
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
        <template #description> {{ $t("header_title_2") }} </template>
        <template #body>
          <USeparator class="py-3 mb-3" />
          <UNavigationMenu
            :items="items"
            orientation="vertical"
            class="w-full justify-center"
            variant="link"
            color="error"
            ,
          >
          </UNavigationMenu>
          <!--  :ui="{link:'text-black hover:text-red-500',  linkLeadingIcon:'text-black hover:text-red-500' }"
            -->
          <LanguageSelector class="mt-4" />
        </template>
      </UDrawer>
    </nav>
  </header>
</template>

<script setup lang="ts">
const isMobileSidebarOpen = ref(false);
const { items } = useMenuItems();
</script>
