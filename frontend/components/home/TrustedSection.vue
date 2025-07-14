<script setup lang="ts"></script>

<template>
  <section id="industries" class="py-20 px-10 md:px-15 bg-gray-200 text-center">
    <div class="flex flex-wrap md:flex-nowrap justify-center items-center">
      <div class="text-left mb-10 md:flex-1/2">
        <h3 class="text-xl md:text-3xl lg:text-4xl font-bold md:mb-2 uppercase">Trusted by Startups.</h3>
        <h3 class="text-xl md:text-3xl lg:text-4xl font-bold mb-5 uppercase">Rated by Experts.</h3>
        <p class="text-md md:text-xl font-semibold">
          Industry platforms like Clutch consistently rate us as a top-tier
          software development partner. That’s because our clients trust us to
          deliver meaningful, business-ready solutions on time and build to
          last.
        </p>
        <UButton
          icon="i-heroicons-arrow-right"
          trailing
          color="primary"
          class="text-white text-md md:text-xl rounded-3xl py-3 px-6 mt-10"
          variant="solid"
          label="GET A QUOTE"
          to="#"
        />
      </div>
      <!--  -->
      <div class="md:flex-1/2 place-items-center">
        <img
          src="https://static.vecteezy.com/system/resources/previews/010/385/335/non_2x/technology-partners-icon-illustration-vector.jpg"
          class="rounded-full h-50 md:h-80"
          alt=""
        />
      </div>
    </div>
  </section>
</template>

<style scoped></style>
