<template>
  <div class="bg-white px-5 md:px-15 pt-10 pb-10 lg:pb-20">
    <section class="text-left">
      <p
        class="pt-3 text-xl md:text-2xl lg:text-3xl mb-3 font-bold text-gray-900"
      >
        Liability limitations
      </p>
      <p class="my-5 text-sm lg:text-lg text-gray-700">
        Tech2Work Agency is not liable for the following stances:
      </p>
      <div v-for="f in liabLst" class="flex items-center my-4">
        <UIcon name="i-lucide-circle-check-big" size="20" class="mr-5" />
        {{ f }}
      </div>
      <p class="font-bold my-10">
        Tech2Work Agency saves the right to introduce this Copyright Statement
        with no prior notification.
      </p>
    </section>
  </div>
</template>

<script setup lang="ts">
const liabLst = [
  "Direct or indirect, intended or unintended damages caused by the reliance on this website",
  "Loss of business opportunity, loss of programs, in case of negligence or tort",
];
</script>
