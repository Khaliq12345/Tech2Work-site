<template>
  <section id="services" class="py-20 bg-white text-center">
     <!-- Listing -->
    <div
      class="container mx-auto grid grid-cols-1 gap-8 px-3 "
    >
      <PortfolioProjectCard
      class="bg-white text-black"
        v-for="item in items"
        :item="item"
      />
    </div>
  </section>
</template>

<script lang="ts" setup>
import type { CaseStudy } from "~/interface/caseStudy";

const items: CaseStudy[] = [
  {
    id: "0",
    title:
      "Cross-platform mobile app & Web platform for Amenity Management Company",
    description:
      "How we helped an amenity management company optimize internal processes and redefine customer experiences with a digital concierge solution.",
    location: "The USA",
    technologies: [
      "Flutter",
      "Python (Django)",
      "ReactJS",
      "AWS",
      "Typescript",
    ],
    services: [
      "App Dev",
      "Android dev",
      "Web Design",
    ],
    industries: [
      "Retail",
      "BoobaLo",
    ],
    imgUrl:
      "https://www.online-image-editor.com/styles/2019/images/power_girl.png",
  },
  {
    id: "1",
    title: "Enterprise Data Platform for Financial Services",
    description:
      "Developed a robust data platform to streamline financial data processing and analytics for a leading financial institution.",
    location: "Europe",
    technologies: [
      "Java",
      "Spring Boot",
      "Kafka",
      "PostgreSQL",
      "AWS",
      "React",
    ],
    services: [
      "App Dev",
      "Android dev",
      "Web Design",
    ],
    industries: [
      "Retail",
      "BoobaLo",
    ],
    imgUrl:
      "https://www.searchenginejournal.com/wp-content/uploads/2019/07/the-essential-guide-to-using-images-legally-online.png",
  },
  {
    id: "2",
    title: "IoT-powered Smart Refueling Solution",
    description:
      "Created an intelligent IoT platform for automated fuel delivery and management in commercial fleets.",
    location: "Canada",
    technologies: ["Node.js", "MQTT", "MongoDB", "React Native", "Azure IoT"],
   services: [
      "App Dev",
      "Android dev",
      "Web Design",
    ],
    industries: [
      "Retail",
      "BoobaLo",
    ],
    imgUrl:
      "https://admin.12grids.com/uploads/blogs/original_cover_images/Webp/benefits-of-custom-web-development-and-web-design-12grids.webp",
  },
  {
    id: "3",
    title: "Social Community Platform for Creators",
    description:
      "Developed a vibrant social platform enabling creators to build communities, share content, and monetize their work.",
    location: "UK",
    technologies: ["Vue.js", "Firebase", "GraphQL", "Stripe", "GraphQL", "Stripe", "GraphQL", "Stripe", "GraphQL", "Stripe", "GraphQL", "Stripe", "GraphQL", "Stripe", "GraphQL", "Stripe", "GraphQL", "Stripe"],
    services: [
      "App Dev",
      "Android dev",
      "Web Design",
    ],
    industries: [
      "Retail",
      "BoobaLo",
    ],
    imgUrl:
      "https://images01.nicepagecdn.com/page/10/78/website-design-preview-107805.jpg",
  },
  {
    id: "4",
    title: "AI-Powered Document Management System",
    description:
      "Built an intelligent system that automates document processing, categorization, and retrieval using advanced AI/ML algorithms.",
    location: "Germany",
    technologies: [
      "Python",
      "TensorFlow",
      "Vue.js",
      "Elasticsearch",
      "Kubernetes",
    ],
    services: [
      "App Dev",
      "Android dev",
      "Web Design",
    ],
    industries: [
      "Retail",
      "BoobaLo",
    ],
    imgUrl:
      "https://img.freepik.com/free-vector/gradient-abstract-technology-landing-page-template_23-2149164222.jpg",
  },
   {
    id: "4",
    title: "AI-Powered Document Management System",
    description:
      "Built an intelligent system that automates document processing, categorization, and retrieval using advanced AI/ML algorithms.",
    location: "Germany",
    technologies: [
      "Python",
      "TensorFlow",
      "Vue.js",
      "Elasticsearch",
      "Kubernetes",
    ],
    services: [
      "App Dev",
      "Android dev",
      "Web Design",
    ],
    industries: [
      "Retail",
      "BoobaLo",
    ],
    imgUrl:
      "https://www.shutterstock.com/shutterstock/videos/1106025969/thumb/7.jpg?ip=x480",
  },
];
</script>
