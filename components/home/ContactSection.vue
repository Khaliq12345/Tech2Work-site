<template>
  <section id="contact" class="py-20 bg-white">
    <div class="container mx-auto text-center">
      <h2 class="text-3xl font-bold text-gray-800 mb-4">Travaillons ensemble</h2>
      <p class="text-gray-600 mb-10">Vous avez un projet ? Parlons-en.</p>
      <form @submit.prevent="handleSubmit" class="max-w-xl mx-auto grid gap-4">
        <nuxtui-input v-model="name" placeholder="Votre nom" required />
        <nuxtui-input v-model="email" type="email" placeholder="Votre email" required />
        <nuxtui-textarea v-model="message" placeholder="Votre message" rows="5" required />
        <nuxtui-button type="submit" color="dark">Envoyer</nuxtui-button>
      </form>
    </div>
  </section>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const name = ref('')
const email = ref('')
const message = ref('')

function handleSubmit() {
  console.log({ name: name.value, email: email.value, message: message.value })
  alert('Message envoyé avec succès !')
  name.value = ''
  email.value = ''
  message.value = ''
}
</script>
