<template>
  <div class="imgbox">
    <img class="btn"  @click="selectedImg()" :src="image.image_path">
  </div>
</template>

<script>
export default {
  name :'EditFeedStills',
  props : {
    image : Object,
    imageId : Number,
    active:[],
  },
  methods:{
    selectedImg(){
      this.$emit('selectedImg',)
    }
  },
  created(){
    // console.log('stillimages==========', this.image)
  }
}
</script>

<style>
  .imgbox{
    max-width: 200px;
    max-height: 120px;
    overflow: hidden;
  }
  .imgbox img{
    object-fit: cover;
    width: 100%;
  }
</style>