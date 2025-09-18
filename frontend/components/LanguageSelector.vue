<template>
  <select id="language" :value="currentLocale" @change="onLocaleChange">
      <option v-for="locale in locales" :key="locale.code" :value="locale.code">
        {{ locale.name }}
      </option>
    </select>
  <!-- <USelect v-model="locale" :items="options" class="max-w-40 h-10" placeholder="Locale" ></USelect>
  {{ locale }}
  <div>
    <button v-for="locale in locales" @click="setLocale(locale.code)">
      {{ locale.name }}
    </button>
    <h1>{{ $t('welcome') }}</h1>
    <select id="language" :value="currentLocale" @change="onLocaleChange">
      <option v-for="locale in locales" :key="locale.code" :value="locale.code">
        {{ locale.name }}
      </option>
    </select>
  </div> -->
</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { locale, locales, setLocale } = useI18n();
const options = locales.value.map((loc: any) => ({
  label: loc.name,
  value: loc.code,
}));

const currentLocale = locale

function onLocaleChange(event: any) {
  setLocale(event.target.value)
}

</script>