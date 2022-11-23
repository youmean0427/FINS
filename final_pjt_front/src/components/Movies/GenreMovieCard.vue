<template>
  <div>
    <!-- <router-link :to="{ name: 'MovieDetailView', params: { id: genre_movie.id } }">
    [DETAIL]</router-link>
    <p>{{genre_movie.title}}</p> -->

    <div id="imgbox"><img id="img" :src="url" alt=""></div>
    <!-- {{genre_movie.stil_image}} -->
  </div>
</template>

<script>
export default {
    name: "GenreMovieCard",

    props: {
      genre_movie: Object
    },
    computed:{
      url(){
        return 'https://image.tmdb.org/t/p/original/' + this.genre_movie.poster
        // if(!this.genre_movie.stil_image){
        //   // console.log('왜 undefined?', this.genre_movie)
        //   return 'https://image.tmdb.org/t/p/original/' + this.genre_movie.poster
        // } else {
        //   return this.genre_movie.stil_image
        // }
      }
    }
}
</script>

<style>
  #imgbox{
    width: 200px;
    height: 200px;
    overflow: hidden;
    margin:4px;
  }
  #img{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>