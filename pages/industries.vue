<template>
  <NuxtLayout name="default">
    <IndustriesHeroSection
      bgimg="'/imgs/industries/bg1.jpg'"
      title="Product Development Industry"
      desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution."
      :features="[
        { name: 'experts', value: '170+' },
        { name: 'experts', value: '170+' },
        { name: 'experts', value: '170+' },
        { name: 'experts', value: '170+' },
      ]"
    />
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
    <IndustriesTrustedSection
      text="Request a free one-hour consultation from our healthcare experts and
          get a detailed estimate"
    />
    <IndustriesServicesSection
      :items="[
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
      ]"
    />
    <IndustriesSolutions
      :items="[
        {
          class: 'bg-gradient-to-br from-white to-gray-400',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
          features: [
            'End-to-end product development',
            'Business analysis and solution design',
            'Scalable MVP and beyond',
          ],
        },
        {
          class: 'bg-gradient-to-br from-white to-gray-400',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
          features: [
            'End-to-end product development',
            'Business analysis and solution design',
            'Scalable MVP and beyond',
          ],
        },
        {
          class: 'bg-gradient-to-br from-white to-gray-400',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
          features: [
            'End-to-end product development',
            'Business analysis and solution design',
            'Scalable MVP and beyond',
          ],
        },
        {
          class: 'text-white bg-gradient-to-br from-black to-gray-400',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
          features: [
            'End-to-end product development',
            'Business analysis and solution design',
            'Scalable MVP and beyond',
          ],
        },
        {
          class: 'text-white bg-gradient-to-br from-black to-gray-400',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
          features: [
            'End-to-end product development',
            'Business analysis and solution design',
            'Scalable MVP and beyond',
          ],
        },
        {
          class: 'text-white bg-gradient-to-br from-black to-gray-400',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
          features: [
            'End-to-end product development',
            'Business analysis and solution design',
            'Scalable MVP and beyond',
          ],
        },
      ]"
    />
    <IndustriesServicesSectionFlip
      :items="[
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
        {
          class: 'lg:flex-1/3',
          title: 'Product Development',
          desc: 'Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.',
          icon: 'i-lucide-mail',
        },
      ]"
    />
    <IndustriesFeaturesSection
      :items="[
        {
          class: 'lg:flex-1/4',
          title: 'Product Development',
          icon: 'i-lucide-mail',
        },
        {
          class: 'lg:flex-1/4',
          title: 'Product Development',
          icon: 'i-lucide-aperture',
        },
        {
          class: 'lg:flex-1/4',
          title: 'Product Development',
          icon: 'i-lucide-apple',
        },
        {
          class: 'lg:flex-1/4',
          title: 'Product Development',
          icon: 'i-lucide-archive-restore',
        },
        {
          class: 'lg:flex-1/4',
          title: 'Product Development',
          icon: 'i-lucide-chart-column-increasing',
        },
        {
          class: 'lg:flex-1/4',
          title: 'Product Development',
          icon: 'i-lucide-circuit-board',
        },
        {
          class: 'lg:flex-1/4',
          title: 'Product Development',
          icon: 'i-lucide-crown',
        },
        {
          class: 'lg:flex-1/4',
          title: 'Product Development',
          icon: 'i-lucide-crosshair',
        },
      ]"
    />
    <IndustriesReasonsSection
      :items="[
        {
          title: 'Overview',
          content: `Our custom medical software development company guarantees high-quality products and on-time releases. Here’s how we deliver exceptional value:`,
        },
        {
          title: 'Cost-Effective & Timely Delivery',
          content: `We offer a variety of engagement models to suit your budget and project timeframe. This ensures cost-effectiveness and timely delivery of custom healthcare software development services without compromising on quality.`,
        },
        {
          title: 'Effective Project Management',
          content: `Our experienced team utilizes industry best practices for project management. We employ an iterative custom healthcare application software development approach, ensuring regular progress updates with on-time demos to foster clear communication throughout the development lifecycle.`,
        },
        {
          title: 'Personalized Approach',
          content: `Our team goes beyond just software development: we have a team of healthcare professionals and software developers who understand the unique needs of the healthcare industry. This combined expertise allows us to offer advanced custom healthcare software design and development that perfectly align with your requirements.`,
        },
      ]"
    />
    <IndustriesTrustedSection
      text="Talk to our experts and find the best solution that suits your needs"
    />
    <IndustriesProcess
      :processes="[
        {
          name: '01 Estimation & Planning',
          description: `During the discovery phase, we deep dive into gaining comprehensive insights of your business needs, uncovering opportunities, and defining clear goals for the project. In-depth consultations, market research, and stakeholder interviews help us identify pain points, and lay the foundation for your healthcare technology software.`,
        },
        {
          name: '02 Agile Development',
          description: `Inoxoft provides custom software development for the healthcare industry with different architectural patterns defined by our experts. With iterative and incremental progress followed by continuous feedback and course correction throughout the development process, we will present to you a product that truly meets the evolving needs of the target audience.`,
        },
        {
          name: '03 UX/UI Design',
          description: `In our UX/UI design process, we delve into UX research, and map out intuitive user journeys. Our goal is to create sleek UI designs for website or mobile app development solutions that promote swift and effortless adoption, and is easy for users of all age groups, regardless of their level of tech proficiency.`,
        },
        {
          name: '04 Quality Assurance Testing',
          description: `We provide rigorous quality assurance testing to guarantee flawless product functionality. The team of the QA engineers evaluate every aspect of the developed product, performing comprehensive tests to identify and resolve any potential issues or bugs.`,
        },
        {
          name: '05 Delivery & Deployment',
          description: `We comply with the highest standards of delivering final products that exceed all expectations and will configure your solution on a secure and reliable hosting platform. Our custom healthcare software development company is well-versed in web and mobile deployment guidelines and requirements.`,
        },
        {
          name: '06 Maintenance & Support',
          description: `As your reliable partner, we will ensure ongoing maintenance and support for the product’s continued success. Our dedicated team of custom healthcare software consultants provides timely assistance, support, troubleshooting, and user training, maximizing the longevity and value of the web product.`,
        },
      ]"
    />
    <TechStack />
    <FAQ />
    <Contact />
  </NuxtLayout>
</template>

<script lang="ts" setup></script>
