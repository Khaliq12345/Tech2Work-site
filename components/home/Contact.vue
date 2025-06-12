<template>
  <div class="flex flex-wrap gap-8 py-12 md:py-20 container mx-auto px-4">
    <!-- Bloc principal de contact -->
    <UCard
      class="col-span-1 lg:col-span-2 shadow-xl p-6 flex flex-col justify-center w-full bg-gradient-to-br from-black to-gray-400"
    >
      <div class="flex flex-wrap lg:flex-nowrap justify-center gap-5">
        <div class="space-y-6 lg:flex-1/2 text-center lg:text-left">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
            Let’s Build Together
          </h2>
          <p class="text-gray-600 dark:text-gray-300 text-base">
            Reach out to our sales managers for tailored software development
            solutions and professional guidance.
          </p>
          <UButton
            icon="i-heroicons-phone"
            color="primary"
            class="text-white text-xl rounded-3xl py-3 px-6 mt-3"
            variant="solid"
            label="Contact Us"
            to="#"
          />
          <!-- Team Members -->
          <div class="flex flex-wrap text-white gap-8 mt-5 justify-center">
            <div
              v-for="person in people"
              :key="person.name"
              class="flex items-center gap-4"
            >
              <img
                :src="person.image"
                alt="Photo"
                class="w-16 h-16 rounded-full object-cover shadow"
              />
              <div>
                <div class="font-semibold">{{ person.name }}</div>
                <div class="text-sm">{{ person.role }}</div>
                <a
                  :href="person.linkedin"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="inline-block mt-1 text-white hover:underline"
                >
                  <Icon name="mdi:linkedin" class="w-5 h-5" />
                </a>
              </div>
            </div>
          </div>
        </div>

        <!--  -->
        <div
          class="bg-white shadow-md rounded-xl p-8 w-full space-y-6 lg:flex-1/2"
        >
          <h2
            class="text-2xl md:text-3xl font-bold text-gray-900 leading-tight"
          >
            START BUILDING YOUR <br />
            SOFTWARE. CONTACT US NOW
          </h2>

          <form @submit.prevent="sendEmail" class="space-y-5">
            <div>
              <input
                v-model="form.name"
                required
                type="text"
                placeholder="Name *"
                class="w-full border-b border-gray-300 focus:outline-none focus:border-blue-600 pb-2"
              />
            </div>
            <div>
              <input
                v-model="form.email"
                required
                type="email"
                placeholder="E-mail *"
                class="w-full border-b border-gray-300 focus:outline-none focus:border-blue-600 pb-2"
              />
            </div>
            <div>
              <textarea
                v-model="form.message"
                required
                placeholder="What we can do for you? *"
                rows="2"
                class="w-full border-b border-gray-300 focus:outline-none focus:border-blue-600 pb-2 resize-none"
              ></textarea>
            </div>
            <!-- Submit Button -->
            <div class="flex items-center justify-between pt-2">
              <button
                type="submit"
                class="bg-white border border-gray-800 text-gray-800 px-6 py-2 rounded-full font-semibold hover:bg-gray-100 transition"
              >
                SEND A MESSAGE
              </button>
              <div
                class="text-gray-500 flex items-center gap-1 text-sm hover:text-gary-800"
              >
                <span>@Tech2Work</span>
              </div>
            </div>
          </form>
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
const form = ref({
  name: "",
  email: "",
  message: "",
});

const people = [
  {
    name: "Oleksii Kamynin",
    role: "Full-Stack Dev",
    image: "https://randomuser.me/api/portraits/men/32.jpg",
    linkedin: "https://linkedin.com/in/oleksii",
  },
  {
    name: "Natalia Zamai",
    role: "Data Engineer",
    image: "https://randomuser.me/api/portraits/women/44.jpg",
    linkedin: "https://linkedin.com/in/natalia",
  },
];

function sendEmail() {
  const subject = encodeURIComponent(`Contact from ${form.value.name}`);
  const body = encodeURIComponent(
    `Name: ${form.value.name}\nEmail: ${form.value.email}\n\nMessage:\n${form.value.message}`,
  );
  const mailto = `mailto:tech2work@gmail.com?subject=${subject}&body=${body}`;
  window.location.href = mailto;
}
</script>

<style scoped>
/* Aucun style personnalisé nécessaire grâce à Tailwind/Nuxt UI */
</style>
