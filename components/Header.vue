<template>
  <header class="sticky top-0 z-50 bg-white shadow">
    <div class="px-5 py-3 bg-black flex flex-wrap justify-center text-center text-white">
      <div class="pl-3">
        Start building your software today. Book a call
      </div>
      <div class="flex">
        <span class=" flex items-center gap-2 pl-6">
          <UIcon name="i-lucide-mail" class="size-4" /> tech2work@gmail.com
        </span>
        <span class=" flex items-center gap-2 px-5">
          <UIcon name="i-lucide-phone" class="size-4" /> +229 0198988765
        </span>
      </div>
    </div>
    <nav class="container mx-auto flex items-center justify-between py-4 px-3">
      <NuxtLink to="/" class="text-2xl font-bold text-black">
        Tech2Work<span class="text-gray-600">Agency</span>
      </NuxtLink>
      <UButton @click="isMobileSidebarOpen = true" :disabled="isMobileSidebarOpen"
        class="bg-gray-100 hover:bg-gray-300 lg:hidden cursor-pointer">
        <UIcon name="i-heroicons-bars-3-bottom-left-20-solid" class="mr-3 text-2xl" />
        <!-- <h3 class="ml-3 text-lg font-semibold text-center">Dashboard</h3> -->
      </UButton>
      <!-- MD  -->
      <ul class="hidden lg:flex items-center gap-8 text-sm font-medium text-gray-700">
        <UNavigationMenu :items="items" class="w-full justify-center" />
      </ul>
      <!-- Mobile Drawer Sidebar -->
      <UDrawer direction="left" v-model:open="isMobileSidebarOpen" class="w-10/12 sm:w-6/12">
        <template #title>
        </template>
        <template #description>
        </template>
        <template #body>
          SideBar Content
        </template>
      </UDrawer>
    </nav>
  </header>
</template>


<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const isMobileSidebarOpen = ref(false);

const items = ref<NavigationMenuItem[]>([
  {
    label: 'Company',
    icon: 'i-lucide-building-2',
    to: '/getting-started',
    children: [
      {
        label: 'Introduction',
        description: 'Fully styled and customizable components for Nuxt.',
        icon: 'i-lucide-house'
      },
      {
        label: 'Installation',
        description: 'Learn how to install and configure Nuxt UI in your application.',
        icon: 'i-lucide-cloud-download'
      },
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Theme',
        icon: 'i-lucide-cog',
        description: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ]
  },
  {
    label: 'Services',
    icon: 'i-lucide-briefcase-business',
    to: '/composables',
    children: [
      {
        label: 'defineShortcuts',
        icon: 'i-lucide-file-text',
        description: 'Define shortcuts for your application.',
        to: '/composables/define-shortcuts'
      },
      {
        label: 'useOverlay',
        icon: 'i-lucide-file-text',
        description: 'Display a modal/slideover within your application.',
        to: '/composables/use-overlay'
      },
      {
        label: 'useToast',
        icon: 'i-lucide-file-text',
        description: 'Display a toast within your application.',
        to: '/composables/use-toast'
      }
    ]
  },
  {
    label: 'Industries',
    icon: 'i-lucide-box',
    to: '/components',
    active: false,
    children: [
      {
        label: 'Link',
        icon: 'i-lucide-file-text',
        description: 'Use NuxtLink with superpowers.',
        to: '/components/link'
      },
      {
        label: 'Modal',
        icon: 'i-lucide-file-text',
        description: 'Display a modal within your application.',
        to: '/components/modal'
      },
      {
        label: 'NavigationMenu',
        icon: 'i-lucide-file-text',
        description: 'Display a list of links.',
        to: '/components/navigation-menu'
      },
      {
        label: 'Pagination',
        icon: 'i-lucide-file-text',
        description: 'Display a list of pages.',
        to: '/components/pagination'
      },
      {
        label: 'Popover',
        icon: 'i-lucide-file-text',
        description: 'Display a non-modal dialog that floats around a trigger element.',
        to: '/components/popover'
      },
      {
        label: 'Progress',
        icon: 'i-lucide-file-text',
        description: 'Show a horizontal bar to indicate task progression.',
        to: '/components/progress'
      }
    ]
  },
  {
    label: 'Technologies',
    icon: 'i-lucide-gpu',
    to: '/components',
    active: false,
    children: [
      {
        label: 'Link',
        icon: 'i-lucide-file-text',
        description: 'Use NuxtLink with superpowers.',
        to: '/components/link'
      },
      {
        label: 'Modal',
        icon: 'i-lucide-file-text',
        description: 'Display a modal within your application.',
        to: '/components/modal'
      },
      {
        label: 'NavigationMenu',
        icon: 'i-lucide-file-text',
        description: 'Display a list of links.',
        to: '/components/navigation-menu'
      },
      {
        label: 'Pagination',
        icon: 'i-lucide-file-text',
        description: 'Display a list of pages.',
        to: '/components/pagination'
      },
      {
        label: 'Popover',
        icon: 'i-lucide-file-text',
        description: 'Display a non-modal dialog that floats around a trigger element.',
        to: '/components/popover'
      },
      {
        label: 'Progress',
        icon: 'i-lucide-file-text',
        description: 'Show a horizontal bar to indicate task progression.',
        to: '/components/progress'
      }
    ]
  },
  {
    label: 'Portfolio',
    icon: 'i-lucide-shield-plus',
    // badge: '3.8k',
    to: 'https://github.com/nuxt/ui',
    // target: '_blank'
  },
  {
    label: 'Pricing',
    icon: 'i-lucide-badge-dollar-sign',
    to: 'https://github.com/nuxt/ui',
    // target: '_blank'
  }
])
</script>
