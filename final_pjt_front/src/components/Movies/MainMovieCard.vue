<template>
    <div id="mcard" @click="moveDetail" class=" text-start" v-if="movie" style="width: 29%;">
        <div id="movie-card">
            <img class="card-img-top" :src="url" alt="movieImg">
        </div>
        <div class="title">
            <h3 id="movieTitle">{{movie.title}}</h3>
        </div>
    </div>
    
</template>

<script>
export default {
  name: 'MainMovieCard',
  props: {
    movie: Object,
  },
  methods:{
    moveDetail(){
      this.$router.push({ name: 'MovieDetailView', params: { id: this.movie.id } })
    },
  },
  computed:{
    url(){
        return this.movie.still_image
    //   if(this.movie.still_image){
    //     return this.movie.still_image
    //   } else{
    //     return 'https://image.tmdb.org/t/p/original/' + this.movie.poster
    //   }
    }
  },
  
}
</script>
<style>
    #mcard{
        height: max-content;
        /* position: relative; */
        max-width: 450px;
        max-height: 450px;
        min-width: 200px;
        min-height: 200px;
        margin: 7px;
        /* bottom: 2%; */
        padding: 10px;
        overflow: hidden;
        border: none;
    }
    #movie-card{
        width: 100%;
        height: 100%;
        vertical-align: middle;
        transition: .5s ease;
        border-radius : 6px;
        overflow: hidden;
    }
    #movie-card:hover{
        transition: .5 ease;
        z-index: 1;
    }
    .card-img-top{
        overflow: hidden;
        object-fit:cover;
        display: block;
        /* position: absolute; */
    }
    #mcard:hover{
        -webkit-transform: scale(1.08);
        transform: scale(1.08);
        opacity: 1;
    }
    #mcard:hover + .title{
        /* position: absolute; */
        /* color: white; */
        font-weight: bold;
        display: block;
        z-index: 10;
    }
    .title{
        position:inherit;
        top: 10%;
        display:none;
    }
</style>