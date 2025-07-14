import type { NavigationMenuItem } from "@nuxt/ui";

export function useMenuItems() {
    const items = ref<NavigationMenuItem[]>([
        {
            label: "Company",
            icon: "i-lucide-building-2",
            to: "",
            children: [
                {
                    label: "About Us",
                    // icon: 'i-lucide-file-text',
                    description: "In our company, we're not just IT professionals.",
                    to: "",
                },
                {
                    label: "Client Reviews",
                    // icon: 'i-lucide-file-text',
                    description: "What is said about us",
                    to: "",
                },
                {
                    label: "Benefits",
                    // icon: 'i-lucide-file-text',
                    description: "Your Interest.",
                    to: "",
                },
                {
                    label: "Blog",
                    // icon: 'i-lucide-file-text',
                    description: "For further interactions.",
                    to: "",
                },
                {
                    label: "Vacancies",
                    // icon: 'i-lucide-file-text',
                    description: "Find more about.",
                    to: "",
                },
                {
                    label: "Contacts",
                    // icon: 'i-lucide-file-text',
                    description: "Reach us today.",
                    to: "",
                },
            ],
        },
        {
            label: "Services",
            icon: "i-lucide-briefcase-business",
            to: "",
            children: [
                {
                    label: "Web Development",
                    icon: "i-lucide-file-text",
                    description: "Define shortcuts for your application.",
                    to: "",
                },
                {
                    label: "MVP development",
                    icon: "i-lucide-file-text",
                    description: "Display a modal/slideover within your application.",
                    to: "",
                },
                {
                    label: "UI UX Design",
                    icon: "i-lucide-file-text",
                    description: "Display a toast within your application.",
                    to: "",
                },
                {
                    label: "AI & ML Based WebApps",
                    icon: "i-lucide-file-text",
                    description: "Display a toast within your application.",
                    to: "",
                },
            ],
        },
        {
            label: "Industries",
            icon: "i-lucide-box",
            to: "",
            active: false,
            children: [
                {
                    label: "Development",
                    to: "",
                    icon: "i-lucide-code-xml",
                },
                {
                    label: "Data Analysis",
                    to: "",
                    icon: "i-lucide-database-zap",
                },
                {
                    label: "AI Automation",
                    to: "",
                    icon: "i-lucide-bot",
                },
                {
                    label: "Optimisation",
                    to: "",
                    icon: "i-lucide-sun",
                },
            ],
        },
        {
            label: "Technologies",
            icon: "i-lucide-gpu",
            to: "",
            active: false,
            children: [
                {
                    label: "Python",
                    icon: "i-lucide-terminal",
                    description: "Use NuxtLink with superpowers.",
                    to: "",
                },
                {
                    label: "Vue / Nuxt JS",
                    icon: "i-lucide-squares-subtract",
                    description: "Display a modal within your application.",
                    to: "",
                },
                {
                    label: "Supabase & co",
                    icon: "i-lucide-database",
                    description: "Display a list of links.",
                    to: "",
                },
                {
                    label: "AI Techs",
                    icon: "i-lucide-brain-circuit",
                    description: "Display a list of pages.",
                    to: "",
                },
            ],
        },
        {
            label: "Portfolio",
            icon: "i-lucide-shield-plus",
            // badge: '3.8k',
            to: "",
            // target: '_blank'
        },
        {
            label: "Pricing",
            icon: "i-lucide-badge-dollar-sign",
            to: "",
            // target: '_blank'
        },
    ]);
    return {
        items
    };
}