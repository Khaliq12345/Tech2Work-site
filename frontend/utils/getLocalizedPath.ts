export function getLocalizedPath(path: string): string {
  const { locale } = useI18n();
  if (locale.value && locale.value !== 'en') {
    return `/${locale.value}${path}`;
  }
  return path;
}