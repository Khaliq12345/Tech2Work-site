<template>
  <header class="sticky top-0 z-50 bg-white shadow">
    <!-- Top Line -->
    <div
      class="px-5 py-3 bg-black flex flex-wrap justify-center text-center text-white"
    >
      <div class="pl-3">Start building your software today. Book a call</div>
      <div class="flex pt-2 md:pt-0">
        <span class="flex items-center gap-2 pl-10">
          <UIcon name="i-lucide-mail" class="size-4" /> tech2work@gmail.com
        </span>
        <span class="flex items-center gap-2 px-5">
          <UIcon name="i-lucide-phone" class="size-4" /> +229 0198988765
        </span>
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
import type { NavigationMenuItem } from "@nuxt/ui";

const isMobileSidebarOpen = ref(false);

const items = ref<NavigationMenuItem[]>([
  {
    label: "Company",
    icon: "i-lucide-building-2",
    to: "/getting-started",
    children: [
      {
        label: "About Us",
        // icon: 'i-lucide-file-text',
        description: "In our company, we're not just IT professionals.",
        to: "/components/link",
      },
      {
        label: "Client Reviews",
        // icon: 'i-lucide-file-text',
        description: "What is said about us",
        to: "/components/link",
      },
      {
        label: "Benefits",
        // icon: 'i-lucide-file-text',
        description: "Your Interest.",
        to: "/components/link",
      },
      {
        label: "Blog",
        // icon: 'i-lucide-file-text',
        description: "For further interactions.",
        to: "/components/link",
      },
      {
        label: "Vacancies",
        // icon: 'i-lucide-file-text',
        description: "Find more about.",
        to: "/components/link",
      },
      {
        label: "Contacts",
        // icon: 'i-lucide-file-text',
        description: "Reach us today.",
        to: "/components/link",
      },
    ],
  },
  {
    label: "Services",
    icon: "i-lucide-briefcase-business",
    to: "/composables",
    children: [
      {
        label: "Web Development",
        icon: "i-lucide-file-text",
        description: "Define shortcuts for your application.",
        to: "/composables/define-shortcuts",
      },
      {
        label: "MVP development",
        icon: "i-lucide-file-text",
        description: "Display a modal/slideover within your application.",
        to: "/composables/use-overlay",
      },
      {
        label: "UI UX Design",
        icon: "i-lucide-file-text",
        description: "Display a toast within your application.",
        to: "/composables/use-toast",
      },
      {
        label: "AI & ML Based WebApps",
        icon: "i-lucide-file-text",
        description: "Display a toast within your application.",
        to: "/composables/use-toast",
      },
    ],
  },
  {
    label: "Industries",
    icon: "i-lucide-box",
    to: "/components",
    active: false,
    children: [
      {
        label: "Development",
        to: "/components/link",
        icon: "i-lucide-code-xml",
      },
      {
        label: "Data Analysis",
        to: "/components/modal",
        icon: "i-lucide-database-zap",
      },
      {
        label: "AI Automation",
        to: "/components/navigation-menu",
        icon: "i-lucide-bot",
      },
      {
        label: "Optimisation",
        to: "/components/pagination",
        icon: "i-lucide-sun",
      },
    ],
  },
  {
    label: "Technologies",
    icon: "i-lucide-gpu",
    to: "/components",
    active: false,
    children: [
      {
        label: "Python",
        icon: "i-lucide-terminal",
        description: "Use NuxtLink with superpowers.",
        to: "/components/link",
      },
      {
        label: "Vue / Nuxt JS",
        icon: "i-lucide-squares-subtract",
        description: "Display a modal within your application.",
        to: "/components/modal",
      },
      {
        label: "Supabase & co",
        icon: "i-lucide-database",
        description: "Display a list of links.",
        to: "/components/navigation-menu",
      },
      {
        label: "AI Techs",
        icon: "i-lucide-brain-circuit",
        description: "Display a list of pages.",
        to: "/components/pagination",
      },
    ],
  },
  {
    label: "Portfolio",
    icon: "i-lucide-shield-plus",
    // badge: '3.8k',
    to: "https://github.com/nuxt/ui",
    // target: '_blank'
  },
  {
    label: "Pricing",
    icon: "i-lucide-badge-dollar-sign",
    to: "https://github.com/nuxt/ui",
    // target: '_blank'
  },
]);
</script>
