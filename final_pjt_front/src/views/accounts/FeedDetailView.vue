<template>
  <div class="modla_c">
    <div class="overlay" @click="$emit('close-modal')"></div>
    <div class="modal-card">
      <h1>{{id}}</h1>
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
.modla_c,
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
  position: relative;
  max-width: 80%;
  margin: auto;
  margin-top: 30px;
  padding: 20px;
  background-color: white;
  min-height: 500px;
  z-index: 10;
  opacity: 1;
}
</style>