
export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event);
  const query = getQuery(event)
  const params = {
    locale: query.locale
  }
  const response = await $fetch(`${event.path}`, {
    baseURL: config.API_URL,
    params: params
  });
  return response;
});
