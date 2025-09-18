<template>
  <iframe
    :src="url"
    width="100%"
    :height="height"
    style="border: 0; border-radius: 12px"
    :allowfullscreen="true"
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
  />
</template>
<script setup lang="ts">
const lat = 6.366;
const lng = 2.425;
const zoom = 15;
const height = "800px";

const url = `https://www.google.com/maps?q=${lat},${lng}&z=${zoom}&output=embed`;
</script>
