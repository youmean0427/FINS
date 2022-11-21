<template>
  <div>
    <h5>{{ feed.id }}</h5>
    <p>{{ feed.title }}</p>
      <img @click="clickfeed(feed.id)" :src="poster" style="width:300px;">
    <!-- <router-link :to="{ name: 'FeedDetailView', params: { id: feedId } }">
      여기에 이미지
    </router-link> -->
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