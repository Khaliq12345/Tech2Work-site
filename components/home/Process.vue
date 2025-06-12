<template>
  <div class="flex justify-center w-full">
    <div class="w-full max-w-5xl mx-5">
      <div class="bg-white shadow-lg rounded-xl overflow-hidden">
        <button
          @click="isOpen = !isOpen"
          class="w-full flex justify-between items-center p-6 text-left text-xl font-semibold text-gray-800 bg-gray-100 hover:bg-gray-200 transition"
        >
          <span class="text-3xl font-bold"
            >Our Software Development Process</span
          >
          <svg
            :class="{ 'rotate-180': isOpen }"
            class="w-5 h-5 transition-transform"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M19 9l-7 7-7-7"
            />
          </svg>
        </button>

        <div
          v-if="isOpen"
          class="p-6 space-y-6 text-gray-700 text-[15px] leading-relaxed"
        >
          <p class="">
            Engaging in software development projects entails a complex and
            iterative process, necessitating meticulous planning, skillful
            execution, and continuous improvement. At Inoxoft, we recognize the
            significance of extracting insights from each stage of the software
            development lifecycle, encompassing business analysis and the
            development of a software project, to effectively navigate from
            inception to launch while managing development costs.
          </p>

          <div>
            <h3 class="font-bold text-xl mb-1">1. Project Initiation</h3>
            <p class="">
              During the discovery phase, as part of our software consulting
              services, we delve deeply into gaining comprehensive insights into
              your business needs, uncovering opportunities, and defining clear
              goals for the project. In-depth consultations, market research,
              and stakeholder interviews, integral to our software consulting
              approach, help us identify pain points and lay the foundation for
              a transformative software solution tailored to your project.
            </p>
          </div>

          <div>
            <h3 class="font-bold text-xl mb-1">2. Project Planning</h3>
            <p class="">
              To guarantee a successful and efficient execution of software
              products, we emphasize meticulous planning. Collaborating with our
              team, you formulate a detailed roadmap, delineate the project
              scope, set deadlines, and allocate resources. The process is
              accompanied by clear communication and effective coordination to
              promptly achieve the best results.
            </p>
          </div>

          <div>
            <h3 class="font-bold text-xl mb-1">3. Design</h3>
            <p class="">
              The design phase bridges the gap between concept and reality. Our
              design team creates wireframes, mockups, and prototypes that
              visualize the final product. This stage includes User Experience
              (UX) Design, User Interface (UI) Design and prototyping.
            </p>
          </div>

          <div>
            <h3 class="font-bold text-xl mb-1">4. Agile Development</h3>
            <p class="">
              Agile development, with its emphasis on iterative and incremental
              progress, along with continuous feedback and course correction
              throughout the development process, showcases a fascinating
              ability to adapt to changes. This, coupled with the collaborative
              approach fostered by agile methodologies, contributes to
              successful project outcomes. The end result is a product that
              genuinely aligns with the evolving needs of the target audience.
              This approach is further enhanced when guided by effective
              technology consulting.
            </p>
          </div>

          <div>
            <h3 class="font-bold text-xl mb-1">5. Quality Assurance Testing</h3>
            <p class="">
              Inoxoft is committed to delivering a seamless user experience, and
              to ensure this, we implement rigorous quality assurance testing,
              leveraging a robust quality management system. Our QA engineers
              meticulously evaluate every aspect of the web product, conducting
              comprehensive tests to identify and resolve potential issues or
              bugs. As part of our custom web app development services, we also
              offer
              <a href="#" class="text-blue-600 underline"
                >QA automation testing services</a
              >
              for both mobile and web applications.
            </p>
          </div>

          <div>
            <h3 class="font-bold text-xl mb-1">6. Delivery and Deployment</h3>
            <p class="">
              In this pivotal stage of software development process, our
              dedicated team meticulously configures your software for
              deployment, considering all technical specifications and
              requirements. Our goal is not just to deliver software but to
              ensure a successful launch that aligns seamlessly with your
              business objectives.
            </p>
          </div>

          <div>
            <h3 class="font-bold text-xl mb-1">7. Maintenance and Support</h3>
            <p class="">
              Your software is in good hands. We understand that software
              development is an ongoing process. Once your software is deployed,
              we offer a comprehensive maintenance and support service to ensure
              that it continues to meet your needs and perform at its best.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const isOpen = ref(false);
</script>

<style scoped>
.rotate-180 {
  transform: rotate(0deg);
}
</style>
