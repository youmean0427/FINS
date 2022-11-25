<template>

    <!-- <router-link :to="{ name: 'MovieDetailView', params: { id: keyword_movie.id } }">
      [DETAIL]
    </router-link>
     -->
    
    <!-- {{keyword_movie.poster}} -->

    <div id="mcard" @click="moveDetail" class="card text-start" v-if="keyword_movie" style="max-width: 23.3%;">
      <div id="movie-view-card">
       <img class="card-img-top"  :src="url" width="25%" alt="">
        </div>    
  </div>
</template>

<script>
export default {
    name: "KeywordMovieCard",
    props: {
        keyword_movie:Object
    },
    methods:{
    moveDetail(){
      this.$router.push({ name: 'MovieDetailView', params: { id: this.keyword_movie.id } })
    },
  },
    computed:{
    url(){
        return 'https://image.tmdb.org/t/p/original/' + this.keyword_movie.poster
      }
    },

  }

</script>

<style>
 .hidden-title{
    z-index: 2;
    width: 100%;
    padding:1em;
    position: absolute;
    text-align : center;
    transform: translate(-50%, -50%);
    font-weight: bold;
    display:none;
    color:rgb(59, 59, 59);
    /* background-color: rgba(228, 228, 228, 0.886); */
    background: rgb(255,255,255);
    background: linear-gradient(90deg, rgba(255,255,255,0.8) 40%, rgb(121, 128, 121, 0.8) 100%);
    /* background: rgb(255,255,255);
    background: radial-gradient(circle, rgba(255,255,255,1) 30%, rgba(255,255,255,0.7) 100%); */
    top : 50%;
    left: 50%;
    height: 100%;
    /* padding-top:50%; */
   }

   #movie-view-card{
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
</style>