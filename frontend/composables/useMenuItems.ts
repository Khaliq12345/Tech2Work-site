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
          icon: "i-lucide-file-text",
          description: "In our company, we're not just IT professionals.",
          to: "",
        },
        {
          label: "Contacts",
          icon: "i-lucide-file-text",
          description: "Reach us today.",
          to: "",
        },
      ],
    },
    // {
    //   label: "Services",
    //   icon: "i-lucide-briefcase-business",
    //   to: "",
    //   children: [
    //     {
    //       label: "Web Development",
    //       icon: "i-lucide-file-text",
    //       description: "Define shortcuts for your application.",
    //       to: "",
    //     },
    //     {
    //       label: "MVP development",
    //       icon: "i-lucide-file-text",
    //       description: "Display a modal/slideover within your application.",
    //       to: "",
    //     },
    //     {
    //       label: "UI UX Design",
    //       icon: "i-lucide-file-text",
    //       description: "Display a toast within your application.",
    //       to: "",
    //     },
    //     {
    //       label: "AI & ML Based WebApps",
    //       icon: "i-lucide-file-text",
    //       description: "Display a toast within your application.",
    //       to: "",
    //     },
    //   ],
    // },
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
      label: "Portfolio",
      icon: "i-lucide-shield-plus",
      to: "/portfolio",
    },
  ]);
  return {
    items,
  };
}

