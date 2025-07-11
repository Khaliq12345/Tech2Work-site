<template>
  <div class="flex justify-center items-center bg-gray-100 px-5 md:px-15">
    <section class="text-left">
      <p
        class="hidden lg:block pt-3 text-2xl md:text-4xl lg:text-5xl mb-3 font-bold text-gray-900"
      >
        Tech2Work Agency
      </p>
      <p class="my-5 text-lg lg:text-3xl text-gray-700">
        We build forward-thinking digital products that enable startups and
        growing businesses to achieve their goals.
      </p>
      <CustomModal>
          <template #trigger>
           <UButton
        class="font-bold rounded-full text-white py-3 px-8 my-5 text-md lg:text-2xl"
        >BOOK A CALL !</UButton>
          </template>
          <template #content>
            <RequestProposal />
          </template>
        </CustomModal>
      
    </section>
    <div class="hidden lg:flex h-160 w-300">
      <img src="~/assets/imgs/logo4.png" alt="" />
    </div>
  </div>
</template>
