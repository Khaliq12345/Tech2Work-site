<template>
  <div class="justify-center w-full">
    <div class="w-full mx-5">
      <div class="bg-white shadow-lg rounded-xl overflow-hidden">
        <button
          @click="isOpen = !isOpen"
          class="w-full flex justify-between items-center p-6 text-left text-xl font-semibold text-gray-800 bg-gray-100 hover:bg-gray-200 transition"
        >
          <span class="text-2xl font-bold">{{ title }}</span>
          <svg
            :class="{ 'rotate-180': isOpen }"
            class="w-5 h-5 transition-transform"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M19 9l-7 7-7-7"
            />
          </svg>
        </button>
        <div
          v-if="isOpen"
          class="p-6 space-y-6 text-gray-700 text-[15px] leading-relaxed"
        >
          <div>
            <p class="text-left">
              {{ content }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const isOpen = ref(false);

defineProps<{
  title: string;
  content: string;
}>();
</script>

<style scoped>
.rotate-180 {
  transform: rotate(0deg);
}
</style>
