<template>
  <div>
     <div class="">
      <div class="mask d-flex align-items-center h-100">
        <div class="container">
          <div class="row" style="align-items: center;">
            <div class="col-md-10 col-lg-8 col-xl-7 mx-auto">
              <div class="card mb-2">
                <div class="card-body d-flex justify-content-between py-2">
                  <div class="input-group input-group-lg">
                    <span class="input-group-text border-0 px-1"><font-awesome-icon @click="searchMovie" icon="fa-search" class="fas fa-search fa-1x"/></span>
                    <input 
                      id="form-control"
                      class="form-control form-control-lg rounded"
                      @keyup.enter="searchMovie"
                      v-model.trim="keyword"
                      type="search"
                      placeholder="search movie">
                  </div>
                  <p class="mb-0 d-flex flex-row align-self-center" style="color: #939597;"><span class="font-weight-bold pe-1">{{resultsLen}} </span>results</p>
                  <!-- <b-button @click="searchMovie" variant="outline-success"> + </b-button> -->
                </div>
              </div>
            </div>
            <div class="card" style="width:746px;">
                <h6 class="mt-3 mb-4" style="color: #939597;">장르별 영화검색</h6>
                    <GenreCardList :genreList="genre" />
                <div class="d-flex justify-content-between align-items-center mt-4">
                  <div>
                    <button type="button" class="btn btn-link btn-rounded" style="color: #939597;" data-mdb-ripple-color="dark">
                      선택초기화
                    </button>
                  </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="keyword">
        <div v-if="searchMovieListLen">
            <div>
            <SearchMovieCard 
            v-for="(movie, idx) in searchMovieList" 
            :key="idx"
            :movie="movie"
            />
            </div>
        </div>
        <div v-else>
          <p>
              <span id="keywordnotfound">{{keyword}}</span>에 대한 검색결과가 존재하지 않습니다.
          </p>
        </div>
      </div>
    </div>





  </div>
</template>

<script>
import GenreCardList from '@/components/Movies/GenreCardList.vue';
import SearchMovieCard  from '@/components/Movies/SearchMovieCard.vue';
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

// const API_KEY = '8d2390a7f14da4093a0836c65dfb59a2'



export default {
    name: "DiscoveryMovieView",
    components: {
      GenreCardList,
      SearchMovieCard 
    },
    data() {
        return {
             genre : null,
            keyword : null,
            lst : [],
        };
    },

    // SE

    computed:{
      resultsLen(){
        return this.lst.length
      },
      searchMovieList(){
        return this.$store.state.searchMovieList
      },
      searchMovieListLen(){
        console.log('searchMovieListLen',this.lst.length)
        if (this.lst){
          return true
        } else {
          return false
        }
      },
    },


    methods: {
        getGenreList() {
            axios({
                method: "get",
                url: `${API_URL}/api/v1/discoverymovie/`
            })
                .then((res) => {
                console.log('getGenreList',res);
                this.genre = res.data;
            })
                .catch((err) => {
                console.log('getGenreList',err);
            });
        },
        //------------------------------------------------------------------------------CUSTOM search
        searchMovie(){
          if (this.keyword){
            // this.$store.dispatch('search_movie', this.keyword)
            const API_URL_SEARCH_MOVIE = `${API_URL}/api/v1/search/${this.keyword}` 
            axios({
              method: 'get',
              url: API_URL_SEARCH_MOVIE,
            })
              .then((response) => {
                // console.log('검색된 키워드에 일치하는 영화목록입니다.')
                // console.log(response)
                // console.log('====================================')
                this.$store.dispatch('search_movie', response.data)
                this.lst = this.$store.state.searchMovieList
              })
              .catch((error) => {
                console.log(error)
              })
            }
          },
    },
    created() {
        this.$store.state.searchMovieList=null
        this.getGenreList();
        this.searchMovie();
    },
}
</script>

<style>
  #input-group-text{
    background-color: none;
  }
  #keywordnotfound{
    font-weight: bold;
  }
  #form-control {
  border-color: transparent;
  }

  .input-group>.form-control:focus {
    border-color: transparent;
    box-shadow: inset 0 0 0 1px transparent;
  }
</style>