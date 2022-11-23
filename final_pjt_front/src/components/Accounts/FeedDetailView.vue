<template>
  <div class="modal_c">
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
  },
}
</script>

<style>
/* Modal */
.modal_c,
.overlay {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  display: flex;
  justify-content: center;
  align-content: center;
}
.overlay {
  opacity: 0.5;
  background-color: black;
}
.modal-card {
  border-radius: 7px;
  position: relative;
  width: 70%;
  height: 70%;
  margin: auto;
  margin-top: 5%;
  margin-bottom: 14%;
  background-color: white;
  max-height: 700px;
  z-index: 10;
  opacity: 1;
  
}
</style>