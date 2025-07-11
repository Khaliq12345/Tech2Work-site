<script setup lang="ts">
const colorMode = useColorMode();

const isDark = computed({
  get() {
    return colorMode.value === "dark";
  },
  set() {
    colorMode.preference = colorMode.value === "dark" ? "light" : "dark";
  },
});
</script>

<template>
  <ClientOnly v-if="!colorMode?.forced">
    <div class="flex items-center">
      
      <UButton
        :icon="isDark ? 'i-heroicons-moon' : 'i-heroicons-sun'"
        color="neutral"
        variant="ghost"
        :label="isDark ? 'Dark Mode': 'Light Mode'"
        @click="isDark = !isDark"
      />
    </div>

    <template #fallback>
      <div class="size-8" />
    </template>
  </ClientOnly>
</template>
