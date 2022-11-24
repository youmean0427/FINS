<template>
  <div class="carddiv">
      <img class="cardimg" @click="clickfeed(feed.id)" :src="poster">
  </div>
</template>

<script>
export default {
    name: 'FeedCardTypeItems',
    props:{
      feed : Object
    },
    computed:{
      poster(){
        return this.feed.image_path
      },
      feedId(){
        return this.feed.id
      }
    },
    methods:{
      clickfeed(id){
        this.$emit('showFeed', id)
      }
    }
}
</script>

<style>
  .cardimg{
    object-fit: cover;
    width : -webkit-fill-available;

    -webkit-transform: scale(1);
    transform: scale(1);
    -webkit-transition: .3s ease-in-out;
    transition: .3s ease-in-out;
  }
  .carddiv{
    display: block;
    overflow: hidden;
    object-fit: cover;

    position: absolute;
    top: 0;
    left: 0;
  }

  .carddiv:hover img{
    -webkit-transform: scale(1.08);
    transform: scale(1.08);
    opacity: 1;
  }

</style>