<template>
  <div class="modal">
    <div class="overlay" @click="$emit('close-modal')"></div>
    <div class="modal-card">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name : 'FeedDetailView',
  props : {
    id : Number
  }
}
</script>

<style>
/* Modal */
.modal,
.overlay {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
}
.overlay {
  opacity: 0.5;
  background-color: black;
}
.modal-card {
  border-radius: 7px;
  position: relative;
  max-width: 80%;
  margin: auto;
  margin-top: 17%;
  margin-bottom: 17%;
  padding: 10px;
  background-color: white;
  min-height: 500px;
  z-index: 10;
  opacity: 1;
}
</style>