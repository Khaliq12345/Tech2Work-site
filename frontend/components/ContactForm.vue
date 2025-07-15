<template>
  <form @submit.prevent="sendEmailFunc" class="space-y-5">
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
        :loading="sending"
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
</template>

<script setup lang="ts">
import { useSendMail } from "~/utils/useSendMail";
const { sendEmail } = useSendMail();
const sending = ref(false);
const form = ref({
  name: "",
  email: "",
  message: "",
});

async function sendEmailFunc() {
  sending.value = true;
  const subject = `You have a new inquiry from your website`;
  const body = `
    <div style="font-family: Arial, sans-serif; padding: 20px; background-color: #f9f9f9;">
      <div style="background-color: #ffffff; max-width: 600px; margin: auto; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
        <div style="background-color: #2196f3; height: 10px;"></div>
        <div style="padding: 40px 30px; text-align: center;">
          <h2 style="color: #2196f3;">Congratulations</h2>
          <p style="font-size: 18px; color: #333;">You have a new inquiry from your website</p>
        </div>
        <div style="padding: 0 30px 30px;">
          <p><strong>Name:</strong> ${form.value.name}</p>
          <p><strong>Email:</strong> <a href="mailto:${form.value.email}">${form.value.email}</a></p>
          <p><strong>Message:</strong></p>
          <p style="white-space: pre-line;">${form.value.message}</p>
        </div>
      </div>
    </div>
  `;
  await sendEmail(subject, body);
  sending.value = false;
  form.value = {
    name: "",
    email: "",
    message: "",
  };
}
</script>
