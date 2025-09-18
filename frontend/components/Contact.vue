<template>
  <div class="flex flex-wrap gap-8 py-12 md:py-20 container mx-auto px-4">
    <!-- Bloc principal de contact -->
    <UCard
      class="col-span-1 lg:col-span-2 shadow-xl p-2 md:p-6 flex flex-col justify-center w-full bg-gradient-to-br from-black to-gray-400"
    >
      <div class="flex flex-wrap lg:flex-nowrap justify-center gap-5">
        <div class="space-y-6 lg:flex-1/2 text-center lg:text-left">
          <h2 class="text-xl md:text-2xl font-bold text-white">
            {{ $t("contact_title_1") }}
          </h2>
          <p class="text-white text-base">
            {{ $t("contact_title_2") }}
          </p>

          <!-- Team Members -->
          <div
            class="flex flex-wrap text-white gap-8 my-10 md:mt-15 justify-center"
          >
            <div
              v-for="person in people"
              :key="person.name"
              class="flex items-center gap-4"
            >
              <div>
                <div class="font-semibold">{{ person.name }}</div>
                <div class="text-sm">{{ person.role }}</div>
              </div>
            </div>
          </div>
        </div>
        <!--  -->
        <div
          class="bg-white shadow-md rounded-xl p-8 w-full space-y-6 lg:flex-1/2"
        >
          <h2 class="text-xl md:text-2xl font-bold text-gray-900 leading-tight">
            {{ $t("contact_title_3") }}
            <br />
            {{ $t("contact_title_4") }}
          </h2>
          <ContactForm />
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
const { people } = useContactPeople();
</script>
