<template>
  <div
    class="flex justify-center items-center bg-gray-100 px-5 md:px-15 py-10 lg:pt-20"
  >
    <section class="text-left">
      <div class="">
        <p
          class="pt-3 text-xl md:text-3xl lg:text-5xl mb-3 font-bold text-gray-900"
        >
          {{ $t("term_of_use_title") }}
        </p>
        <p class="my-5 text-sm lg:text-lg text-gray-700">
          {{ $t("term_of_use_desc1") }}
          –
          <span class="font-bold">contact@tech2work.tech</span>.
          {{ $t("term_of_use_desc2") }}
        </p>
        <p class="font-bold my-10">
          {{ $t("term_of_use_desc3") }}
        </p>
        <p class="my-5">
          {{ $t("term_of_use_desc4") }}
        </p>
      </div>
    </section>
  </div>
</template>
