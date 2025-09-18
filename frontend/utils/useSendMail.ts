export function useSendMail() {
    const { showToast } = useNotifications();
  async function sendEmail(subject: string, body: string) {
  const data = await $fetch("/api/global/send-email-message", {
    method: "POST",
    query: {
      subject: subject,
      content: body,
    },
  });
  const response = data as any;
  if (response.status == "success") {
    showToast(
      "Success !",
      "Mail Successfully Delivred",
      "i-lucide-check",
      "black",
    );
  } else {
    showToast("Error !", "Mail Not Delivred", "i-heroicons-x-mark", "error");
  }
}
  return {
    sendEmail
  };
}