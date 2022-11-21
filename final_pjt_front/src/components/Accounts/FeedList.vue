<template>
  <div>
    <h1>FeedList</h1>
    <FeedCard
      v-for="movie in likeMovies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import FeedCard from '@/components/Accounts/FeedCard.vue'

export default {
    name: 'FeedList',
    components: {
        FeedCard
    },
    computed:{
      // user(){
      //   return 
      // }
    },
    props:{
      likeMovies : Object
    }
}

</script>

<style>

</style>