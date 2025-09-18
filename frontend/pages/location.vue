<template>
  <NuxtLayout name="default">
    <p
      class="text-xl md:text-2xl lg:text-3xl mt-10 font-bold text-gray-900 uppercase text-center"
    >
      {{ $t("location_title") }}
    </p>
    <map-view class="my-10" />
    <Contact />
  </NuxtLayout>
</template>

<script lang="ts" setup></script>
