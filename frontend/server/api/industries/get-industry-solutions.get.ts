export default defineEventHandler(async (event) => {
  const query = getQuery(event)
  const params = {
    industry: query.industry
  }
  const config = useRuntimeConfig(event);
  const response = await $fetch(`${event.path}`, {
    baseURL: config.API_URL,
    params: params, 
  });
  return response;
});
