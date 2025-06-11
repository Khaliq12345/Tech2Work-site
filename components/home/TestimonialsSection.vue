<template>
  <section id="services" class="py-20 bg-gradient-to-br from-gray-300 to-gray-50 text-center">
    <p class="text-4xl mb-20 font-bold text-gray-900">Our clients and what they say</p>
    <div class="container mx-auto flex flex-wrap lg:flex-nowrap gap-5">
      <TestimonialCard
  quote="They were able to handle everything we threw at them fairly easily."
  name="Guy Jackson"
  role="Lead Software Developer, D-BIT Systems Pty Ltd"
  avatar=""
  class="flex-2/5"
/>

<TestimonialCard
  quote="They were able to handle everything we threw at them fairly easily."
  name="Guy Jackson"
  role="Lead Software Developer, D-BIT Systems Pty Ltd"
  avatar=""
  class="flex-3/5"
/>
      </div>
      <!--  -->
      <div class="mt-5 container mx-auto flex flex-wrap lg:flex-nowrap gap-5">
     <TestimonialCard
  quote="They were able to handle everything we threw at them fairly easily."
  name="Guy Jackson"
  role="Lead Software Developer, D-BIT Systems Pty Ltd"
  avatar=""
  class="flex-3/5"
/>
        <TestimonialCard
  quote="They were able to handle everything we threw at them fairly easily."
  name="Guy Jackson"
  role="Lead Software Developer, D-BIT Systems Pty Ltd"
  avatar=""
  class="flex-2/5"
/>


      </div>
  </section>
</template>

<script lang="ts" setup>
import TestimonialCard from '~/components/home/TestimonialCard.vue'
</script>
