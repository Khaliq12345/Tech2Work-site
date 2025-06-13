<template>
  <section id="industries" class="py-20 px-10 md:px-15 bg-gray-200 text-center">
    <div class="flex flex-wrap md:flex-nowrap justify-center items-center">
      <div class="text-center">
        <p class="text-2xl font-bold">
        {{ text }}
        </p>
        <UButton
          icon="i-heroicons-arrow-right"
          trailing
          color="primary"
          class="text-white text-xl rounded-3xl py-3 px-6 mt-10"
          variant="solid"
          label="CONSULT NOW"
          to="#"
        />
      </div>
      <!--  -->
      <!--  -->


      <!--  -->
     
    </div>
  </section>
</template>

<script lang="ts" setup>
const showModal = ref(false)

function openModal() {
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

defineProps<{ text: string; }>();
</script>
