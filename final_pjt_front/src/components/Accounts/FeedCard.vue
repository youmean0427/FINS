<template>
  <div>
    <h5>{{ feed.id }}</h5>
    <p>{{ feed.title }}</p>
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

</style>