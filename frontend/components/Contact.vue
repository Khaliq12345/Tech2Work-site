<template>
  <div class="flex flex-wrap gap-8 py-12 md:py-20 container mx-auto px-4">
    <!-- Bloc principal de contact -->
    <UCard
      class="col-span-1 lg:col-span-2 shadow-xl p-2 md:p-6 flex flex-col justify-center w-full bg-gradient-to-br from-black to-gray-400"
    >
      <div class="flex flex-wrap lg:flex-nowrap justify-center gap-5">
        <div class="space-y-6 lg:flex-1/2 text-center lg:text-left">
          <h2
            class="text-xl md:text-2xl font-bold text-gray-900 dark:text-white"
          >
            Let’s Build Together
          </h2>
          <p class="text-gray-600 dark:text-gray-300 text-base">
            Reach out to our team for tailored software development solutions
            and professional guidance.
          </p>

          <!-- Team Members -->
          <div class="flex flex-wrap text-white gap-8 mt-5 justify-center">
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
            <div
              class="flex text-sm md:text-md items-center flex-wrap justify-center md:justify-between pt-2 gap-5"
            >
              <UButton
                :loading="sending"
                type="submit"
                class="border text-white px-6 py-2 rounded-full font-semibold transition"
              >
                SEND A MESSAGE
              </UButton>
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
const { showToast } = useNotifications();
const sending = ref(false);
const form = ref({
  name: "",
  email: "",
  message: "",
});

const { people } = useContactPeople();

async function sendEmail() {
  sending.value = true;
  const subject = `Contact from ${form.value.name}`;
  const body = `Name: ${form.value.name}\nEmail: ${form.value.email}\n\nMessage:\n${form.value.message}`;
  const data = await $fetch("/api/global/send-email-message", {
    method: "POST",
    query: {
      subject: subject,
      content: body,
      mail_from: form.value.email,
    },
  });
  sending.value = false;
  const response = data as any;
  if (response.status == "success") {
    showToast(
      "Success !",
      "Mail Successfully Delivred",
      "i-lucide-check",
      "success",
    );
  } else {
    showToast("Error !", "Mail Not Delivred", "i-heroicons-x-mark", "error");
  }
  form.value = {
    name: "",
    email: "",
    message: "",
  };
}
</script>
