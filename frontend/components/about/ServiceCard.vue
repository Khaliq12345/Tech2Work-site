<template>
  <div class="w-50 h-35 md:w-70 md:h-50 bg-white overflow-hidden">
    <div
      class="relative w-full rounded-xl h-full transition-transform duration-700 transform-style-preserve-3d"
      :class="{ 'rotate-y-180': isFlipped }"
      @mouseenter="isFlipped = true"
      @mouseleave="isFlipped = false"
    >
      <!-- Front -->
      <UCard
        variant="soft"
        class="absolute w-full h-full bg-white border-2 backface-hidden text-left shadow-2xl"
      >
        <UIcon :name="icon" size="50" class="py-2" />
        <div class="flex items-center justify-start">
          <div class="text-left">
            <h3 class="text-xl md:text-2xl font-bold">{{ title }}</h3>
          </div>
        </div>
      </UCard>
      <!-- Back -->
      <UCard
        variant="soft"
        class="absolute w-full h-full border-2 backface-hidden rotate-y-180 text-white bg-gradient-to-br from-black to-gray-100 text-center shadow-2xl"
      >
        <div class="flex items-center justify-start">
          <div class="text-left">
            <p class="font-semibold mb-2">{{ desc }}</p>
          </div>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps<{
  title: string;
  desc: string;
  icon: string;
  features: string[];
}>();

const isFlipped = ref(false);
</script>

<style scoped>
.perspective {
  perspective: 1000px;
}

.transform-style-preserve-3d {
  transform-style: preserve-3d;
}

.backface-hidden {
  backface-visibility: hidden;
}

.rotate-y-180 {
  transform: rotateY(180deg);
}
</style>
