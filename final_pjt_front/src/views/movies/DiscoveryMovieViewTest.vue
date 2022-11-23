<template>
    <div>
        <div>
        <!-- 영화 검색 input bar -->
        <div>
          <input 
            
            @keyup.enter="searchMovie(keyword)"
            v-model.trim="keyword"
            type="text"
            placeholder="search movie">
           <button @click="searchMovie" variant="outline-success"> + </button>
        </div>
        <div v-if="searchMovieListLen">
          <div>
              <div>
              <SearchMovieCard 
               v-for="(movie, idx) in searchMovieList" 
              :key="idx"
              :movie="movie"
              />
              </div>
          </div>
        </div>
        <div v-else>
          <h5>
              검색결과가 존재하지 않습니다.
          </h5>
        </div>
      </div>
    </div>
</template>

<script>
import SearchMovieCard from '@/components/Movies/SearchMovieCard'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

// KEy
// const API_KEY = '8d2390a7f14da4093a0836c65dfb59a2'

export default {
    name: 'SearchView',
    components:{
        SearchMovieCard,


    },
    data(){
        return{
            keyword : null,
        }
    },
    computed:{
      searchMovieList(){
        return this.$store.state.searchMovieList
      },
      searchMovieListLen(){
        const smll = this.$store.getters.searchMovieListLen
        if (smll > 0){
          return true
        } else {
          return false
        }
      }
    },
    // 검색 DB로 바꾸기
    methods:{
      //   searchMovie(){
      //   const params = {
      //     api_key: API_KEY,
      //     language: 'ko_KR',
      //     query: this.keyword,
      //   }
      //   if (this.keyword){
      //     // this.$store.dispatch('search_movie', this.keyword)
      //     const API_URL_SEARCH_MOVIE = `https://api.themoviedb.org/3/search/movie?` 
      //     axios({
      //     method: 'get',
      //     url: API_URL_SEARCH_MOVIE,
      //     params : params,
      //     })
      //     .then((response) => {
      //       console.log('검색된 키워드에 일치하는 영화목록입니다.')
      //       console.log(response)
      //       console.log('====================================')
      //       this.$store.dispatch('search_movie', response.data.results)
      
            
            
      //     })
      //     .catch((error) => {
      //       // 검색한 키워드의 영화 결과가 없으면 영화 결과가 없다는 페이지로 ..
      //       console.log(error)
      //     })
      //   }
      //   this.keyword = null
      // },
      searchMovie(keyword){
        if(this.keyword) {
          this.$router.go(this.$router.push({ name : 'SearchView', params: {keyword: keyword} }))
        }
      },

    },
    created(){
        this.keyword = this.$route.params.keyword
        const API_URL_SEARCH_MOVIE = `${API_URL}/api/v1/search/${this.keyword}/` 
        axios({
          method: 'get',
          url: API_URL_SEARCH_MOVIE,
        })
        .then((response) => {
          console.log('검색된 키워드에 일치하는 영화목록입니다.')
          this.$store.dispatch('search_movie', response.data.results)

        })
        .catch((error) => {
          console.log(error)
        })
      this.keyword = null
    },



}
</script>

<style>

</style>