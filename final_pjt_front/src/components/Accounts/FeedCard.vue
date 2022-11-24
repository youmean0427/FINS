<template>
  <div>
    <img @click="clickfeed(feed.id)" :src="poster" style="width:300px;">
  </div>
</template>

<script>
export default {
    name: 'FeedCard',
    props:{
      feed : Object
    },
    computed:{
      poster(){
        if(!this.feed.image_path){
          return 'https://user-images.githubusercontent.com/87971876/203553951-12ae7f24-9ba6-4563-934c-60928d7746d4.png'
        }else {
          return this.feed.image_path
        }
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

</style>