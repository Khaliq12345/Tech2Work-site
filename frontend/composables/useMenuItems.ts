import { ref } from 'vue';
import type { NavigationMenuItem } from "@nuxt/ui";
import { useI18n } from '#i18n';

export function useMenuItems() {
  const { t } = useI18n();

  const items = ref<NavigationMenuItem[]>([
    {
      label: t('nav_menu_home'),
      icon: "i-lucide-home",
      to: getLocalizedPath("/"),
    },
    {
      label: t('nav_menu_about'),
      icon: "i-lucide-info",
      description: "In our company, we're not just IT professionals.",
      to: getLocalizedPath("/about"),
    },
    {
      label: t('nav_menu_portfolio'),
      icon: "i-lucide-shield-plus",
      to: getLocalizedPath("/portfolio"),
    },
    {
      label: t('nav_menu_location'),
      icon: "i-lucide-locate-fixed",
      to: getLocalizedPath("/location"),
    },
  ]);

  return {
    items,
  };
}