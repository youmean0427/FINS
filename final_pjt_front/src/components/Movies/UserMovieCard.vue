<template>
      
        <div id="mcard" @click="moveDetail" class="card text-start" v-if="movie" style="max-width: 29%;">
          <div id="movie-view-card">
            <img class="card-img-top" :src="url">
          </div>
          <!-- <div class="hidden-title">
              <h3 id="movieTitle">{{movie[1]}}</h3>
          </div> -->
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
  methods:{
    moveDetail(){
      this.$router.push({ name: 'MovieDetailView', params: { id: this.movie[0]  } })
    },
  },
  }
  </script>
  