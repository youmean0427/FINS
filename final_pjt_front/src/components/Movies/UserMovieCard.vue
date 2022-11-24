<template>
    <div>
  
      <h5>{{ movie[1] }}</h5>
      <!-- <img :src="movie[4]" style="width:300px;"> -->

      <img class="card-img-top" :src="url" style="max-width: 15%">
     <div>
      <router-link :to="{ name: 'MovieDetailView', params: { id: movie[0] } }">
        [DETAIL]
      </router-link>
       </div>
          <!-- <div id="mcard" @click="moveDetail" class="card text-start" v-if="movie" style="max-width: 33.3%;">
        <div id="movie-view-card">
         
        </div>
        <div class="hidden-title">
            <h3 id="movieTitle">{{movie.title}}</h3>
        </div>
        </div>

    
       -->

      <hr>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserMovieCard',
    props: {
      movie: Array,
    },

    computed:{
    url(){
      if(this.movie[3]){
        return 'https://image.tmdb.org/t/p/original/' + this.movie[3]
      } else{
        return 'https://image.tmdb.org/t/p/original/' + this.movie[3]
      }
    }
  },
  }
  </script>
  
  <style>
  
  </style>
