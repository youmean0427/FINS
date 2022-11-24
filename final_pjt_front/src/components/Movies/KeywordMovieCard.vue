<template>
  <div>

    <router-link :to="{ name: 'MovieDetailView', params: { id: keyword_movie.id } }">
      [DETAIL]
    </router-link>

    <!-- {{keyword_movie.poster}} -->
    <p>{{keyword_movie.title}}</p>
    <img :src="url" width="25%" alt="">
    
    <hr>
  </div>
</template>

<script>
export default {
    name: "KeywordMovieCard",
    props: {
        keyword_movie:Object
    },

    computed:{
    url(){
        return 'https://image.tmdb.org/t/p/original/' + this.keyword_movie.poster
      }
    }
  }

</script>

<style>

</style>