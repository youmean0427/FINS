<template>

    <div id="mcard" @click="moveDetail" class="card text-start" v-if="movie" style="max-width: 33.3%;">
      <div id="movie-view-card">
        <img class="card-img-top" :src="url" alt="movieImg">
      </div>
      <div class="hidden-title">
          <h5 id="movieTitle">{{movie.title}}</h5>
      </div>
      
    </div>
    
</template>

<script>
export default {
  name: 'MovieCard',
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
      if(this.movie.still_image){
        return this.movie.still_image
      } else{
        return 'https://image.tmdb.org/t/p/original/' + this.movie.poster
      }
    }
  },
  
}
</script>

<style>
  .hidden-title h5{
    padding-top: 50%;
  }
  .hidden-title{
    z-index: 2;
    width: 100%;
    position: absolute;
    text-align : center;
    transform: translate(-50%, -50%);
    /* font-weight: bold; */
    display:none;
    color:rgb(59, 59, 59);
    /* background-color: rgba(228, 228, 228, 0.886); */
    background: rgb(255,255,255);
    background: linear-gradient(90deg, rgba(255,255,255,0.8) 40%, rgb(121, 128, 121, 0.8) 100%);
    top : 50%;
    left: 50%;
    height: 100%;
   }
  #movie-view-card img{
    width:inherit;
    object-fit: cover;
  }
  #movie-view-card{
    overflow: hidden;
    width : 100%;
    vertical-align : middle;
    transition: .5s ease;
    border-radius : 6px;
   }
   #movie-view-card:hover{
     transition: .5 ease;
     z-index: 1;
   }
   #movie-view-card:hover + .hidden-title{
    transition: .5 ease;
    display: block;
   }
   #movie-view-card + .hidden-title:hover{
    transition: .5 ease;
    display: block;
   }
  #card{
    border:none;
    /* margin-bottom: 20px; */
  }
  
  #card-frame{
    border:none;
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 10px;
    margin-left:5px;
  }

  /* 중앙 정렬 */
  /* .layout_03 {
        display: flex;
        justify-content: center;
        align-items: center;
    } */

</style>
