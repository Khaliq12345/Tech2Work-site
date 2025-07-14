<template>
  <div class="flex flex-wrap gap-8 container mx-auto">
    <UCard
      class="col-span-1 lg:col-span-2 shadow-xl p-0 md:p-3 lg:p-4 flex flex-col justify-center w-full bg-gradient-to-br from-black to-gray-400"
    >
      <div class="flex flex-wrap lg:flex-nowrap justify-center gap-5">
        <!--  -->
        <div
          class="bg-white text-black shadow-md rounded-xl p-8 w-full space-y-6 lg:flex-1/2"
        >
          <h2 class="text-xl md:text-2xl font-bold uppercase leading-tight">
            Request for proposal
          </h2>
          <p class=" ">Let’s discuss how we can help with your project.</p>
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
                placeholder="Project description *"
                rows="2"
                class="w-full border-b border-gray-300 focus:outline-none focus:border-blue-600 pb-2 resize-none"
              ></textarea>
            </div>
            <!-- Submit Button -->
            <div class="flex gap-5 items-center justify-between pt-2">
              <UButton
                type="submit"
                icon="i-lucide-arrow-up-from-dot"
                color="primary"
                class="text-white text-xl rounded-3xl py-3 px-10 mt-3"
                variant="solid"
                >Send</UButton
              >
              <div
                class="text-gray-500 flex items-center gap-1 text-sm hover:text-gary-800"
              >
                <span>@Tech2Work</span>
              </div>
            </div>
          </form>
          <p class="mt-2 text-md">
            By clicking «Send» you confirm, that you understand and agree to the
            Privacy Policy
          </p>
        </div>
        <!--  -->
        <div class="hidden lg:block space-y-6 lg:flex-1/2 text-center px-10">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
            Let’s Build Together
          </h2>
          <p class="text-gray-600 dark:text-gray-300 text-base mb-15">
            Reach out to our team for tailored software development solutions
            and professional guidance.
          </p>
          <div
            v-for="f in features"
            :key="f"
            class="flex text-left items-center my-4"
          >
            <UIcon name="i-lucide-circle-check-big" size="20" class="mr-5" />
            {{ f }}
          </div>
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
const features = [
  "5+ years in software development",
  "200+ successfully delivered projects",
  "We focus on your needs, not generic solutions",
  "Transparent planning and execution from day one",
  "End-to-end product development",
];
const form = ref({
  name: "",
  email: "",
  message: "",
  files: [] as File[],
});

function sendEmail() {
  const subject = encodeURIComponent(`Contact from ${form.value.name}`);
  const body = encodeURIComponent(
    `Name: ${form.value.name}\nEmail: ${form.value.email}\n\nMessage:\n${form.value.message}`,
  );
  const mailto = `mailto:tech2work@gmail.com?subject=${subject}&body=${body}`;
  window.location.href = mailto;
}

function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement;
  if (target.files) {
    form.value.files = Array.from(target.files);
  }
}
</script>
