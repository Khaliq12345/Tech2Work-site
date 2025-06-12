<template>
    <UContainer class="py-12 md:py-20 lg:py-24 text-primary border-gray-400 w-full">
        <div class="flex flex-col md:flex-row md:justify-between md:items-center mb-8 md:mb-12">
            <h3 class="lg:flex-1/2 text-4xl font-bold mb-2 uppercase">OUTCOMES WE'VE ENGINEERED</h3>
            <div class="flex flex-col sm:flex-row gap-4">
                <UButton icon="i-heroicons-arrow-right" trailing color="primary" class="text-white text-xl rounded-3xl py-3 px-6" variant="solid"
                    label="ALL CASE STUDIES" to="#" />
            </div>
        </div>
        <div class=" ">
            <UCard v-if="activeCaseStudy" class="lg:col-span-10 bg-gradient-to-tr from-black to-gray-400 shadow-xl">
                <div class="flex items-center flex-wrap lg:flex-nowrap">
                    <div class="flex flex-row lg:flex-col items-start overflow-x-auto h-full flex-wrap lg:max-w-50 ">
                        <div v-for="study in caseStudies" :key="study.id"
                            class="p-2 lg:p-4 cursor-pointer transition-all duration-300 w-full" :class="{
                                'bg-gray-800 shadow-lg ring-2 ring-primary-500': activeCaseStudyId === study.id,
                                'bg-gray-700 hover:bg-gray-600': activeCaseStudyId !== study.id
                            }" @click="activeCaseStudyId = study.id">
                            <span class="text-white font-bold">
                                {{ study.title }}
                            </span>
                        </div>
                    </div>
                    <!--  -->
                    <div class="gap-8">
                        <div class="lg:order-1 px-6 py-4 md:px-8 md:py-6 lg:px-10 lg:py-8">
                            <div class="flex flex-wrap lg:flex-nowrap items-start gap-x-5">
                                <div class="lg:flex-1/2">
                                    <p class="text-sm font-semibold text-gray-500 dark:text-gray-400 mb-2">Case studies
                                    </p>
                                    <h3 class="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-4">
                                        {{ activeCaseStudy.title }}
                                    </h3>
                                    <p class="text-base text-gray-700 dark:text-gray-300 mb-4">
                                        {{ activeCaseStudy.description }}
                                    </p>
                                </div>
                                <div
                                    class="lg:flex-1/2 lg:order-2 w-full items-center justify-center place-items-center rounded-b-lg lg:rounded-l-none lg:rounded-r-lg overflow-hidden">
                                    <img v-if="activeCaseStudy.mediaType === 'image'" :src="activeCaseStudy.mediaUrl"
                                        class="max-w-full h-50 object-contain rounded-lg shadow-md" />
                                    <div v-else-if="activeCaseStudy.mediaType === 'video'"
                                        class="w-full h-50 aspect-video bg-gray-700 flex items-center justify-center text-white">
                                        <p>Video Player Placeholder</p>
                                    </div>
                                    <div class="flex mt-4 items-center text-gray-600 dark:text-gray-400 text-sm mb-4">
                                        <UIcon name="i-heroicons-map-pin" class="mr-1" />
                                        <span>{{ activeCaseStudy.location }}</span>
                                    </div>

                                    <p class="text-sm font-semibold text-white mb-2">Technologies:</p>
                                    <div class="flex flex-wrap gap-2 mb-8 text-white">
                                        <UBadge v-for="tech in activeCaseStudy.technologies" :key="tech" :label="tech"
                                            variant="subtle" size="sm" class="text-white border" />
                                    </div>
                                </div>
                            </div>
                            <!--  -->
                            <div class="flex mt-5 flex-wrap lg:flex-nowrap items-start gap-x-5">
                                <div class="lg:flex-1/2">
                                    <h4 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">The Client</h4>
                                    <p class="text-base text-gray-700 dark:text-gray-300 mb-6">
                                        {{ activeCaseStudy.clientStory }}
                                    </p>
                                </div>
                                <div class="lg:flex-1/2 ">
                                    <h4 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">Business Need
                                    </h4>
                                    <ul
                                        class="list-disc list-inside text-base text-gray-700 dark:text-gray-300 space-y-2">
                                        <li v-for="(need, index) in activeCaseStudy.businessNeed" :key="index">
                                            {{ need }}
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


            </UCard>
        </div>
    </UContainer>
</template>

<script setup lang="ts">
// --- Types pour les données des cas d'étude ---
interface CaseStudy {
    id: string;
    clientLogo: string; // Path to logo image
    title: string;
    description: string;
    location: string;
    technologies: string[];
    clientStory: string;
    businessNeed: string[]; // List of bullet points for business need
    mediaUrl: string,
    mediaType: 'image' | 'video'; // To distinguish if it's a video player or image
}

// --- Données d'exemple (à remplacer par des données réelles, ex: via une API) ---
const caseStudies: CaseStudy[] = [
    {
        id: '0',
        clientLogo: '/logos/bandmilk.svg', // Assurez-vous que ces chemins sont corrects dans votre dossier public/logos
        title: 'Cross-platform mobile app & Web platform for Amenity Management Company',
        description: 'How we helped an amenity management company optimize internal processes and redefine customer experiences with a digital concierge solution.',
        location: 'The USA',
        technologies: ['Flutter', 'Python (Django)', 'ReactJS', 'AWS', 'Typescript'],
        clientStory: 'Founded in 2008, our client has grown from a small start-up into an established full-service luxury lifestyle brand with over 70 properties across the luxury amenity landscape. The company provides comprehensive amenity management, construction, design, and digital concierge services.',
        businessNeed: [
            'Handling high volumes of requests manually, leading to inefficiencies.',
            'Providing a consistent and convenient user experience to their clients.',
            'Managing resources and service personnel effectively, which impacted service delivery and client satisfaction.',
        ],
        mediaUrl: 'https://www.online-image-editor.com/styles/2019/images/power_girl.png',
        mediaType: 'image',
    },
    {
        id: '1',
        clientLogo: '/logos/equinex.svg',
        title: 'Enterprise Data Platform for Financial Services',
        description: 'Developed a robust data platform to streamline financial data processing and analytics for a leading financial institution.',
        location: 'Europe',
        technologies: ['Java', 'Spring Boot', 'Kafka', 'PostgreSQL', 'AWS', 'React'],
        clientStory: 'A global financial services firm needed a modern data platform to handle increasing data volumes and provide real-time insights.',
        businessNeed: ['Slow data processing.', 'Lack of real-time analytics.', 'Scalability issues with existing infrastructure.'],
        mediaUrl: 'https://www.searchenginejournal.com/wp-content/uploads/2019/07/the-essential-guide-to-using-images-legally-online.png',
        mediaType: 'image',
    },
    {
        id: '2',
        clientLogo: '/logos/refuels.svg',
        title: 'IoT-powered Smart Refueling Solution',
        description: 'Created an intelligent IoT platform for automated fuel delivery and management in commercial fleets.',
        location: 'Canada',
        technologies: ['Node.js', 'MQTT', 'MongoDB', 'React Native', 'Azure IoT'],
        clientStory: 'A logistics company sought to optimize fuel consumption and delivery for its large fleet of vehicles.',
        businessNeed: ['Inefficient manual refueling.', 'Lack of real-time fuel inventory.', 'High operational costs.'],
        mediaUrl: 'https://admin.12grids.com/uploads/blogs/original_cover_images/Webp/benefits-of-custom-web-development-and-web-design-12grids.webp',
        mediaType: 'image',
    },
    {
        id: '3',
        clientLogo: '/logos/tribely.svg',
        title: 'Social Community Platform for Creators',
        description: 'Developed a vibrant social platform enabling creators to build communities, share content, and monetize their work.',
        location: 'UK',
        technologies: ['Vue.js', 'Firebase', 'GraphQL', 'Stripe'],
        clientStory: 'A startup aimed to provide a dedicated space for digital creators to connect and thrive, distinct from mainstream social media.',
        businessNeed: ['Lack of tailored community tools for creators.', 'Difficulty in content monetization.', 'Need for direct fan engagement.'],
        mediaUrl: 'https://images01.nicepagecdn.com/page/10/78/website-design-preview-107805.jpg',
        mediaType: 'image',
    },
    {
        id: '4',
        clientLogo: '/logos/bintrocker.svg',
        title: 'AI-Powered Document Management System',
        description: 'Built an intelligent system that automates document processing, categorization, and retrieval using advanced AI/ML algorithms.',
        location: 'Germany',
        technologies: ['Python', 'TensorFlow', 'Vue.js', 'Elasticsearch', 'Kubernetes'],
        clientStory: 'A large enterprise faced challenges with manual document handling and inefficient information retrieval.',
        businessNeed: ['Time-consuming manual document processing.', 'Difficulty in finding specific information.', 'Need for compliance and audit trails.'],
        mediaUrl: 'https://img.freepik.com/free-vector/gradient-abstract-technology-landing-page-template_23-2149164222.jpg',
        mediaType: 'image',
    },
];

const activeCaseStudyId = ref('0');

const activeCaseStudy = computed(() => {
    return caseStudies.find(cs => cs.id === activeCaseStudyId.value);
});


</script>


<style scoped>
/* Pas de styles spécifiques ici si tout est géré par Tailwind CSS via NuxtUI */
/* Ou des ajustements mineurs si nécessaire */

/* Exemple de style pour la scrollbar sur mobile (optionnel) */
div::-webkit-scrollbar {
    height: 8px;
    /* For horizontal scroll */
    width: 8px;
    /* For vertical scroll */
}

div::-webkit-scrollbar-track {
    background: #f1f1f1;
}

div::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 4px;
}

div::-webkit-scrollbar-thumb:hover {
    background: #555;
}
</style>
