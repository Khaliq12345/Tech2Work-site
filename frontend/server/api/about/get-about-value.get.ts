export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event);
  const response = await $fetch(`${event.path}`, {
    baseURL: config.API_URL,
  });
  return response;
});
