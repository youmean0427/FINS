<template>
  <img @click="selectedImg()" :src="image.image_path" style="width : 100px;">
</template>

<script>
export default {
  name :'EditFeedStills',
  props : {
    image : Object,
    imageId : Number,
  },
  methods:{
    selectedImg(){
    
      this.$emit('selectedImg',)
    }
  }
}
</script>

<style>

</style>