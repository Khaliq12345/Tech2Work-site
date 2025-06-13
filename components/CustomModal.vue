<template>
  <!-- TRIGGER BUTTON -->
  <span @click="openModal" class="inline-block">
    <slot name="trigger" />
  </span>
  <!-- BACKDROP (Teleport to body) -->
  <teleport to="body">
    <Transition name="fade">
      <div
        v-if="showModal"
        id="modal-backdrop"
        class="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
        @click="backdropClick"
      >
        <!-- MODAL CONTENT -->
        <div class="relative z-50 scale-95 animate-modal" @click.stop>
          <slot name="content" />
        </div>
      </div>
    </Transition>
  </teleport>
</template>

<script setup lang="ts">
const showModal = ref(false)

function openModal() {
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

function backdropClick(event: MouseEvent) {
  const target = event.target as HTMLElement
  if (target.id === 'modal-backdrop') {
    closeModal()
  }
}
</script>

<style scoped>
/* FADE BACKDROP ANIMATION */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
@keyframes modalFadeIn {
  0% {
    transform: scale(0.95);
    opacity: 0;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}
.animate-modal {
  animation: modalFadeIn 0.3s ease;
}
</style>
