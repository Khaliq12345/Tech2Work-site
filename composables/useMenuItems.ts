import type { NavigationMenuItem } from "@nuxt/ui";

export function useMenuItems() {
    const items = ref<NavigationMenuItem[]>([
        {
            label: "Company",
            icon: "i-lucide-building-2",
            to: "/getting-started",
            children: [
                {
                    label: "About Us",
                    // icon: 'i-lucide-file-text',
                    description: "In our company, we're not just IT professionals.",
                    to: "/components/link",
                },
                {
                    label: "Client Reviews",
                    // icon: 'i-lucide-file-text',
                    description: "What is said about us",
                    to: "/components/link",
                },
                {
                    label: "Benefits",
                    // icon: 'i-lucide-file-text',
                    description: "Your Interest.",
                    to: "/components/link",
                },
                {
                    label: "Blog",
                    // icon: 'i-lucide-file-text',
                    description: "For further interactions.",
                    to: "/components/link",
                },
                {
                    label: "Vacancies",
                    // icon: 'i-lucide-file-text',
                    description: "Find more about.",
                    to: "/components/link",
                },
                {
                    label: "Contacts",
                    // icon: 'i-lucide-file-text',
                    description: "Reach us today.",
                    to: "/components/link",
                },
            ],
        },
        {
            label: "Services",
            icon: "i-lucide-briefcase-business",
            to: "/composables",
            children: [
                {
                    label: "Web Development",
                    icon: "i-lucide-file-text",
                    description: "Define shortcuts for your application.",
                    to: "/composables/define-shortcuts",
                },
                {
                    label: "MVP development",
                    icon: "i-lucide-file-text",
                    description: "Display a modal/slideover within your application.",
                    to: "/composables/use-overlay",
                },
                {
                    label: "UI UX Design",
                    icon: "i-lucide-file-text",
                    description: "Display a toast within your application.",
                    to: "/composables/use-toast",
                },
                {
                    label: "AI & ML Based WebApps",
                    icon: "i-lucide-file-text",
                    description: "Display a toast within your application.",
                    to: "/composables/use-toast",
                },
            ],
        },
        {
            label: "Industries",
            icon: "i-lucide-box",
            to: "/components",
            active: false,
            children: [
                {
                    label: "Development",
                    to: "/components/link",
                    icon: "i-lucide-code-xml",
                },
                {
                    label: "Data Analysis",
                    to: "/components/modal",
                    icon: "i-lucide-database-zap",
                },
                {
                    label: "AI Automation",
                    to: "/components/navigation-menu",
                    icon: "i-lucide-bot",
                },
                {
                    label: "Optimisation",
                    to: "/components/pagination",
                    icon: "i-lucide-sun",
                },
            ],
        },
        {
            label: "Technologies",
            icon: "i-lucide-gpu",
            to: "/components",
            active: false,
            children: [
                {
                    label: "Python",
                    icon: "i-lucide-terminal",
                    description: "Use NuxtLink with superpowers.",
                    to: "/components/link",
                },
                {
                    label: "Vue / Nuxt JS",
                    icon: "i-lucide-squares-subtract",
                    description: "Display a modal within your application.",
                    to: "/components/modal",
                },
                {
                    label: "Supabase & co",
                    icon: "i-lucide-database",
                    description: "Display a list of links.",
                    to: "/components/navigation-menu",
                },
                {
                    label: "AI Techs",
                    icon: "i-lucide-brain-circuit",
                    description: "Display a list of pages.",
                    to: "/components/pagination",
                },
            ],
        },
        {
            label: "Portfolio",
            icon: "i-lucide-shield-plus",
            // badge: '3.8k',
            to: "https://github.com/nuxt/ui",
            // target: '_blank'
        },
        {
            label: "Pricing",
            icon: "i-lucide-badge-dollar-sign",
            to: "https://github.com/nuxt/ui",
            // target: '_blank'
        },
    ]);
    return {
        items
    };
}