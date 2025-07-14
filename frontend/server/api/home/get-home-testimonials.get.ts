export default defineEventHandler(async (event) => {
  console.log(event.path);
  const config = useRuntimeConfig(event);
  const response = await $fetch(`${event.path}`, {
    baseURL: config.API_URL,
  });
  return response;
});
