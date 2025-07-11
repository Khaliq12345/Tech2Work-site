import type { NavigationMenuItem } from "@nuxt/ui";

export function useMenuItems() {
  const route = useRoute();
  //  route.name?.toString().includes
  const items = ref<NavigationMenuItem[]>([
    {
      label: "Home",
      icon: "i-lucide-home",
      to: "/",
    },
    {
      label: "About Us",
      icon: "i-lucide-info",
      description: "In our company, we're not just IT professionals.",
      to: "/about",
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
