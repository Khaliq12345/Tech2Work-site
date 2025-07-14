export default defineEventHandler(async (event) => {
    const query = getQuery(event);
    const config = useRuntimeConfig(event);
    const params = {
        subject: query.subject,
        content: query.content,
        mail_from: query.mail_from,
    };
    const response = await $fetch(`${event.path}`, {
        baseURL: config.API_URL,
        method: 'POST',
        params: params,
    });
    return response;
});
