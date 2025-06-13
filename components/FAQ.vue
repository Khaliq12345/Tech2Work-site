<template>
  <section id="industries" class="py-20 px-10 md:px-15 bg-gray-200 text-center">
    <div class="text-left flex flex-wrap lg:flex-nowrap gap-y-5 mb-10">
      <h3 class="lg:flex-1/4 text-4xl font-bold mb-5 uppercase">
        Frequently Asked Questions
      </h3>
      <div class="w-full lg:flex-1/2 justify-center place-items-center">
        <IndustriesReasonCard
          v-for="item in items"
          class="mb-5 place-items-center"
          :title="item.title"
          :content="item.content"
        />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const items = [
  {
    title:
      "What are the key features I should consider in custom healthcare software?",
    content: `Our custom medical software development company guarantees high-quality products and on-time releases. Here’s how we deliver exceptional value:`,
  },
  {
    title: "How much does custom healthcare software development cost?",
    content: `We offer a variety of engagement models to suit your budget and project timeframe. This ensures cost-effectiveness and timely delivery of custom healthcare software development services without compromising on quality.`,
  },
  {
    title:
      "What about integrating custom healthcare software with existing systems?",
    content: `Our experienced team utilizes industry best practices for project management. We employ an iterative custom healthcare application software development approach, ensuring regular progress updates with on-time demos to foster clear communication throughout the development lifecycle.`,
  },
  {
    title:
      "How can I find a reputable custom healthcare software development company?",
    content: `Our team goes beyond just software development: we have a team of healthcare professionals and software developers who understand the unique needs of the healthcare industry. This combined expertise allows us to offer advanced custom healthcare software design and development that perfectly align with your requirements.`,
  },
  {
    title:
      "What are some of the challenges associated with custom healthcare software development?",
    content: `Custom healthcare software development comes with its own set of challenges, but with careful planning and a skilled development team, these hurdles can be overcome:
            Strict regulations and the ever-present threat of cyberattacks necessitate robust security measures throughout the development process.
            Working with a development team familiar with HIPAA and other relevant regulations helps ensure your software meets compliance standards.
            Clear communication with stakeholders and an agile development methodology allow for adapting to changing requirements throughout the development process.`,
  },
];
</script>
