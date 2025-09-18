<template>
  <UContainer class="py-10 space-y-8">
    <h2 class="text-2xl font-bold">{{ $t("privacy_policy_details_title") }}</h2>

    <ul>
      <li v-for="section in sections" class="my-2">
        <a :href="`#${section.id}`"
          ><span class="font-semibold">{{
            $t(`privacy_policy_details_title_${section.id}`) ?? section.title
          }}</span></a
        >
      </li>
    </ul>

    <USeparator class="py-5" />

    <div
      v-for="section in sections"
      :key="section.id"
      :id="section.id"
      class="space-y-4"
    >
      <h2 class="text-2xl font-semibold text-primary">
        {{ $t(`privacy_policy_details_title_${section.id}`) ?? section.title }}
      </h2>
      <div v-for="part in section.parts" :key="part.subtitle" class="space-y-2">
        <h3 v-if="part.subtitle" class="text-xl font-medium text-gray-800">
          {{
            $t(
              `privacy_policy_details_subtitle_${section.id}_${section.parts.indexOf(part)}`,
            ) ?? part.subtitle
          }}
        </h3>
        <p class="text-base">
          {{
            $t(
              `privacy_policy_details_summary_${section.id}_${section.parts.indexOf(part)}`,
            ) ?? part.summary
          }}
        </p>
        <ul v-if="part.details" class="list-disc pl-5 text-sm space-y-1">
          <li v-for="item in part.details" :key="item">
            {{
              $t(
                `privacy_policy_details_details_${section.id}_${section.parts.indexOf(part)}_${part.details.indexOf(item)}`,
              ) ?? item
            }}
          </li>
        </ul>
      </div>
    </div>
  </UContainer>
</template>

<script setup lang="ts">
const sections: Ref<any> = ref([]);
const { data } = await useFetch("/api/global/get-privacy-detail");
sections.value = data.value;

/* const sections: Array<any> = [
  {
    title: "1. What information do we collect?",
    id: "title-1",
    parts: [
      {
        subtitle: "Personal information you disclose to us",
        summary: "We collect personal information that you provide to us.",
        details: [
          "Full name",
          "Phone number",
          "Email address",
          "Job title",
          "Username",
          "Mailing address",
          "Billing information",
          "Company details",
          "Profile photo",
          "Account credentials",
          "Chat and support history",
          "Survey responses",
          "Uploaded files",
          "Social media profiles",
          "Any other information you choose to provide",
        ],
      },
      {
        subtitle: "Sensitive Information",
        summary:
          "We do not intentionally collect or process sensitive personal data unless required by law.",
      },
    ],
  },
  {
    title: "2. How do we process your information?",
    id: "title-2",
    parts: [
      {
        summary:
          "We process your personal information for various purposes, depending on your interaction with us.",
        details: [
          "To facilitate account creation and login process",
          "To provide and maintain our services",
          "To respond to user inquiries and support requests",
          "To send administrative information and alerts",
          "To personalize user experience",
          "To improve our website and services",
          "To manage user accounts and preferences",
          "To request user feedback",
          "To send promotional and marketing communications",
          "To conduct analytics and performance monitoring",
          "To enforce our terms, conditions and policies",
          "To comply with legal obligations",
          "To detect and prevent fraud",
          "To secure and monitor infrastructure",
          "To protect vital interests of users",
        ],
      },
    ],
  },
  {
    title: "3. What legal bases do we rely on?",
    id: "title-3",
    parts: [
      {
        summary:
          "We process your data based on one or more of the following legal bases under the GDPR framework:",
        details: [
          "Your consent",
          "The performance of a contract",
          "Compliance with legal obligations",
          "Vital interests",
          "Public interest or official authority",
          "Legitimate business interests",
        ],
      },
    ],
  },
  {
    title: "4. When and with whom do we share your personal information?",
    id: "title-4",
    parts: [
      {
        summary:
          "We may share your data with trusted third parties or as required by law.",
        details: [
          "Service providers and partners",
          "Analytics and tracking platforms",
          "Government agencies (if legally required)",
          "In case of business transfers or mergers",
          "With your consent or at your direction",
        ],
      },
    ],
  },
  {
    title: "5. Do we use cookies and other tracking technologies?",
    id: "title-5",
    parts: [
      {
        summary:
          "We use cookies and similar technologies to enhance user experience and analyze usage.",
        details: [
          "Session cookies",
          "Persistent cookies",
          "Third-party cookies (Google Analytics, etc.)",
          "Web beacons and tracking pixels",
          "Browser fingerprinting",
        ],
      },
    ],
  },
  {
    title: "6. How do we handle your social logins?",
    id: "title-6",
    parts: [
      {
        summary:
          "If you choose to register or log in using a social media account, we may receive certain information from that provider.",
      },
    ],
  },
  {
    title: "7. How long do we keep your information?",
    id: "title-7",
    parts: [
      {
        summary:
          "We retain personal information only for as long as necessary to fulfill the purposes outlined in this policy.",
        details: [
          "While your account is active",
          "As required to comply with legal obligations",
          "For historical record-keeping (anonymized if possible)",
        ],
      },
    ],
  },
  {
    title: "8. How do we keep your information safe?",
    id: "title-8",
    parts: [
      {
        summary:
          "We implement appropriate technical and organizational security measures.",
        details: [
          "Data encryption",
          "Access controls and authentication",
          "Regular system monitoring",
          "Employee training",
          "Secure data storage solutions",
        ],
      },
    ],
  },
  {
    title: "9. Do we collect information from minors?",
    id: "title-9",
    parts: [
      {
        summary:
          "We do not knowingly collect or solicit data from individuals under 13 years of age.",
      },
    ],
  },
  {
    title: "10. What are your privacy rights?",
    id: "title-10",
    parts: [
      {
        summary:
          "Depending on your location, you may have certain rights regarding your personal data.",
        details: [
          "Right to access",
          "Right to rectification",
          "Right to deletion",
          "Right to object or restrict processing",
          "Right to data portability",
          "Right to withdraw consent",
          "Right to lodge a complaint with a data protection authority",
        ],
      },
    ],
  },
  {
    title: "11. Controls for Do-Not-Track features", 
    id: "title-11",
    parts: [
      {
        summary:
          "Most browsers offer a Do-Not-Track feature; we currently do not respond to such signals.",
      },
    ],
  },
  {
    title: "12. Do we make updates to this policy?",
    id: "title-12",
    parts: [
      {
        summary:
          "Yes, we will update this policy as necessary to stay compliant with relevant laws.",
      },
    ],
  },
  {
    title: "13. How can you contact us about this notice?",
    id: "title-13",
    parts: [
      {
        summary:
          "If you have questions or comments about this policy, you may contact us at:",
        details: [
          "Email address",
          "Phone number",
          "Mailing address",
          "Online contact form",
        ],
      },
    ],
  },
  {
    title: "14. How can you review, update, or delete your data?",
    id: "title-14",
    parts: [
      {
        summary:
          "You can request to review, update, or delete your personal information by contacting us directly.",
      },
    ],
  },
  {
    title: "15. Additional Information for International Users",
    id: "title-15",
    parts: [
      {
        summary:
          "If you are accessing our services from outside your country, your data may be processed in other jurisdictions.",
      },
    ],
  },
]; 
*/
</script>
