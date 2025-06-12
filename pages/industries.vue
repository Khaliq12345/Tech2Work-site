<template>
  <NuxtLayout name="default">
    <!--  -->
    <IndustriesHeroSection
      bgimg="'/imgs/industries/bg2.jpg'"
      title="Product Development Industry"
      desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution."
      :features="[
        { name: 'experts', value: '170+' },
        { name: 'experts', value: '170+' },
        { name: 'experts', value: '170+' },
        { name: 'experts', value: '170+' },
      ]"
    />
    <!--  -->
    <IndustriesTestimonialsSection
      :items="[
        {
          name: 'Guy Jackson',
          role: 'Lead Software Developer',
          quote:
            'They were able to handle everything we threw at them fairly easily',
          img: 'https://randomuser.me/api/portraits/men/32.jpg',
        },
        {
          name: 'Guy Jackson',
          role: 'Lead Software Developer',
          quote:
            'They were able to handle everything we threw at them fairly easily',
          img: 'https://randomuser.me/api/portraits/men/32.jpg',
        },
        {
          name: 'Guy Jackson',
          role: 'Lead Software Developer',
          quote:
            'They were able to handle everything we threw at them fairly easily',
          img: 'https://randomuser.me/api/portraits/men/32.jpg',
        },
        {
          name: 'Guy Jackson',
          role: 'Lead Software Developer',
          quote:
            'They were able to handle everything we threw at them fairly easily',
          img: 'https://randomuser.me/api/portraits/men/32.jpg',
        },
      ]"
    />
    <!-- -->
    <!-- <IndustriesTrustedSection />
    <IndustriesServicesSection
    :items="[
      {
        class:'flex-1/4 text-white bg-gradient-to-br from-black to-gray-400',
        title:'Product Development',
        desc:'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
        icon:'i-lucide-mail'
      },
      {
        class:'flex-1/4 text-white bg-gradient-to-br from-black to-gray-400',
        title:'Product Development',
        desc:'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
        icon:'i-lucide-mail'
      },
      {
        class:'flex-1/4 text-white bg-gradient-to-br from-black to-gray-400',
        title:'Product Development',
        desc:'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
        icon:'i-lucide-mail'
      },
    ]" /> -->
  </NuxtLayout>
</template>

<script lang="ts" setup></script>
