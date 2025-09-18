<script setup lang="ts"></script>

<template>
  <section id="industries" class="py-20 px-10 md:px-15 bg-gray-200 text-center">
    <div class="flex flex-wrap md:flex-nowrap justify-center items-center">
      <div class="text-left mb-10 md:flex-1/2">
        <h3 class="text-xl md:text-2xl lg:text-3xl font-bold md:mb-2 uppercase">
          {{ $t("about_trusted_section_title1") }}
        </h3>
        <h3 class="text-xl md:text-2xl lg:text-3xl font-bold mb-5 uppercase">
          {{ $t("about_trusted_section_title2") }}
        </h3>
        <p class="text-md md:text-xl font-semibold">
          {{ $t("about_trusted_section_desc") }}
        </p>
        <div class="text-lg mt-5">
          <!-- Mission -->
          <div class="mb-3">
            <div class="flex flex-wrap gap-y-2 items-center mb-2">
              <UIcon name="i-lucide-briefcase-business" />
              <span class="font-semibold px-2"
                >{{ $t("about_trusted_section_mission_title") }}
              </span>
              <div class="flex flex-wrap gap-2">
                {{ $t("about_trusted_section_mission_desc") }}
              </div>
            </div>
          </div>
          <!-- Vision -->
          <div class="mb-3">
            <div class="flex flex-wrap gap-y-2 items-center mb-2">
              <UIcon name="i-lucide-gpu" />
              <span class="font-semibold px-2"
                >{{ $t("about_trusted_section_vision_title") }}
              </span>
              <div class="w-full ml-5 text-left">
                <ul style="list-style-type: square">
                  <li>
                    {{ $t("about_trusted_section_vision_desc1") }}
                  </li>
                  <li>
                    {{ $t("about_trusted_section_vision_desc2") }}
                  </li>
                  <li>{{ $t("about_trusted_section_vision_desc3") }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--  -->
      <div class="md:flex-1/2 place-items-center">
        <img
          src="https://saigontechnology.com/wp-content/uploads/software-development-process-models.png"
          class="rounded-2xl h-50 md:h-80"
          alt=""
        />
      </div>
    </div>
  </section>
</template>

<style scoped></style>
