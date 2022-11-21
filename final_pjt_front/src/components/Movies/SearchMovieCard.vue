<template>
  <div>
    <div v-if="movie" style="max-width: 20rem;">
      <span>
        <img  :src="movieURL" alt="" style="width: 100%;">
      </span>
      
      <div>
        <!-- <p>{{title}}</p> -->
        <span 
          style="font-size:0.6em; 
          max-width: calc(100% - 38px); 
          overflow: hidden; 
          text-overflow: ellipsis; 
          display: -webkit-box;
          -webkit-line-clamp: 3; 
          -webkit-box-orient: vertical;"
        >
        <!-- {{overview}} -->
        </span>
        
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "SearchMovieCard",
  props:{
    movie: Object,
  },
  computed:{
    title() {
      return this.movie.title
    },
    overview() {
      return this.movie.overview
    },
    movieURL(){
      // TMDB에서 영화 poster url을 불러올때 BASE URL 사용
      const url = this.$store.state.BASE_POSTER_PATH + this.movie.poster_path
      return url
    }
  },
  methods:{
    // 보고싶은 영화 리스트에 추가하는 메서드
    wantWatchMovie(){
      this.$store.dispatch('want_watch_movie', this.movie)
    }
  }
  
}
</script>

<style>
  

</style>