<template>
  
        
  <div class="place-items-center w-full">
    <div class="w-full max-w-5xl px-5 ">
      <UAccordion :items="acItems" class="" >
          <template #default>
            <span class="text-3xl font-bold"
            >Our Software Development Process</span
          >
          </template>
          <template #content>
           <div v-for="item in items">
            <h3 class="font-bold text-xl mb-1">{{ item.title }}</h3>
            <p class="">
              {{ item.content }}
            </p>
          </div>
          </template>
        </UAccordion>
    </div>
  </div>
</template>

<script setup lang="ts">
const acItems = [{}]
const items = [
  {
    title: "Overview",
    content: `Engaging in software development projects entails a complex and
            iterative process, necessitating meticulous planning, skillful
            execution, and continuous improvement. At Inoxoft, we recognize the
            significance of extracting insights from each stage of the software
            development lifecycle, encompassing business analysis and the
            development of a software project, to effectively navigate from
            inception to launch while managing development costs.`,
  },
  {
    title: "1. Project Initiation",
    content: `During the discovery phase, as part of our software consulting
              services, we delve deeply into gaining comprehensive insights into
              your business needs, uncovering opportunities, and defining clear
              goals for the project. In-depth consultations, market research,
              and stakeholder interviews, integral to our software consulting
              approach, help us identify pain points and lay the foundation for
              a transformative software solution tailored to your project.`,
  },
  {
    title: "2. Project Planning",
    content: `To guarantee a successful and efficient execution of software
              products, we emphasize meticulous planning. Collaborating with our
              team, you formulate a detailed roadmap, delineate the project
              scope, set deadlines, and allocate resources. The process is
              accompanied by clear communication and effective coordination to
              promptly achieve the best results.`,
  },
  {
    title: "3. Design",
    content: `The design phase bridges the gap between concept and reality. Our
              design team creates wireframes, mockups, and prototypes that
              visualize the final product. This stage includes User Experience
              (UX) Design, User Interface (UI) Design and prototyping.`,
  },
  {
    title: "4. Agile Development",
    content: `Agile development, with its emphasis on iterative and incremental
              progress, along with continuous feedback and course correction
              throughout the development process, showcases a fascinating
              ability to adapt to changes. This, coupled with the collaborative
              approach fostered by agile methodologies, contributes to
              successful project outcomes. The end result is a product that
              genuinely aligns with the evolving needs of the target audience.
              This approach is further enhanced when guided by effective
              technology consulting.`,
  },
  {
    title: "5. Quality Assurance Testing",
    content: `Inoxoft is committed to delivering a seamless user experience, and
              to ensure this, we implement rigorous quality assurance testing,
              leveraging a robust quality management system. Our QA engineers
              meticulously evaluate every aspect of the web product, conducting
              comprehensive tests to identify and resolve potential issues or
              bugs. As part of our custom web app development services, we also
              offerQA automation testing services for both mobile and web applications.`,
  },
  {
    title: "6. Delivery and Deployment",
    content: `In this pivotal stage of software development process, our
              dedicated team meticulously configures your software for
              deployment, considering all technical specifications and
              requirements. Our goal is not just to deliver software but to
              ensure a successful launch that aligns seamlessly with your
              business objectives.`,
  },
  {
    title: "7. Maintenance and Support",
    content: `Your software is in good hands. We understand that software
              development is an ongoing process. Once your software is deployed,
              we offer a comprehensive maintenance and support service to ensure
              that it continues to meet your needs and perform at its best.`,
  },
];
</script>

