<template>
  <div>
    <h1>DiscoveryMovieView</h1>
    <!-- 서치 수정 -->

    <input 
    @keyup.enter="searchMovie"
    v-model.trim="keyword"
    type="text"
    >
    <button @click="searchMovie"> + </button>


    <div>
        <SearchMovieCard 
        v-for="(movie, idx) in searchMovieList" 
        :key="idx"
        :movie="movie"
        />
    </div>
    

    <GenreCardList :genreList="genre" />
    
  </div>
</template>

<script>
import GenreCardList from '@/components/Movies/GenreCardList.vue';
import SearchBar from '@/components/Movies/SearchBar.vue';
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

// const API_KEY = '8d2390a7f14da4093a0836c65dfb59a2'

export default {
    name: "DiscoveryMovieView",
    components: {
      GenreCardList,
      SearchBar
    },
    data() {
        return {
             genre : null,
            // Array -> null


        };
    },


    methods: {
        getGenreList() {
            axios({
                method: "get",
                url: `${API_URL}/api/v1/discoverymovie/`
            })
                .then((res) => {
                console.log(res);
                console.log("데이터를 받았어요!");
                this.genre = res.data;
            })
                .catch((err) => {
                console.log("데이터를 받지 못했어요!");
                console.log(err);
            });
        },


        // SE
         searchMovie(){
        const params = {
          api_key: API_KEY,
          language: 'ko_KR',
          query: this.keyword,
        }
        if (this.keyword){
          // this.$store.dispatch('search_movie', this.keyword)
          const API_URL_SEARCH_MOVIE = `https://api.themoviedb.org/3/search/movie?` 
          axios({
          method: 'get',
          url: API_URL_SEARCH_MOVIE,
          params : params,
          })
          .then((response) => {
            console.log('검색된 키워드에 일치하는 영화목록입니다.')
            console.log(response)
            console.log('====================================')
            this.$store.dispatch('search_movie', response.data.results)

          })
          .catch((error) => {
            // 검색한 키워드의 영화 결과가 없으면 영화 결과가 없다는 페이지로 ..
            console.log(error)
          })
        }
        // this.keyword = null
      },


       
    },
    created() {
        this.$store.state.searchMovieList=null
        this.getGenreList();
        this.searchMovie();
        
        //SE
        // this.keyword = this.$route.params.keyword
        // console.log(this.keyword)
        
   
    },
}
</script>

<style>

</style>