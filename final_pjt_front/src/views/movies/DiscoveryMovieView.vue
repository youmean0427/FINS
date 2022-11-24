<template>
  <div>
     <div class="discoverypage">
      <div class="mask d-flex align-items-center h-100">
        <div class="container">
          <div class="row" style="align-items: center;">
            <div class="col-12 col-xl-8 mx-auto">
              <div class="card mb-2">
                <div class="card-body d-flex justify-content-between py-2">
                  <div class="input-group input-group-lg">
                    <span class="input-group-text border-0 px-1"><font-awesome-icon @click="searchMovie" icon="fa-search" class="fas fa-search fa-1x"/></span>
                    <input 
                      id="form-control"
                      class="form-control form-control-lg rounded"
                      @keyup="searchMovie"
                      v-model.trim="keyword"
                      type="search"
                      placeholder="search movie">
                  </div>
                  <p class="mb-0 d-flex flex-row align-self-center" style="color: #939597;"><span class="font-weight-bold pe-1">{{resultsLen}} </span>results</p>
                  <!-- <b-button @click="searchMovie" variant="outline-success"> + </b-button> -->
                </div>
              </div>
            <div class="card" style="border:none;">
              <div v-if="keyword">
                <div v-if="searchMovieListLen">
                    <div class="movieFrame">
                      <MovieCard 
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
              <div v-else>
                <a class="genrebox btn btn-dark" @click="switchToggle" >장르별 영화검색</a>
                  <div v-if="showt">
                    <GenreCardList @selectedGenre="getGenreId" @resetGenre="genId = false"/>
                      <div v-if="genreIdSelected" >
                        <GenreMovieListView
                          :genreId="selectedGenre"       
                        />
                      </div>
                  </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>

    </div>





  </div>
</template>

<script>
import GenreCardList from '@/components/Movies/GenreCardList.vue';
import MovieCard  from '@/components/Movies/MovieCard.vue';
import GenreMovieListView from '@/views/movies/GenreMovieListView.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

// const API_KEY = '8d2390a7f14da4093a0836c65dfb59a2'



export default {
    name: "DiscoveryMovieView",
    components: {
      GenreCardList,
      MovieCard,
      GenreMovieListView
    },
    data() {
        return {
            genre : null,
            keyword : null,
            lst : [],
            showt : false,
            genId : null,
        };
    },

    // SE

    computed:{
      genreIdSelected(){
        if(this.genId){
          return true
        }else{
          return false
        }
      },
      selectedGenre() {
        return this.genId
      },
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
      getGenreId(selected){
        console.log(selected)
        // this.genreIdSelected = false
        this.genId = false
        this.genId = {'id' : Number(selected)}
      },
      switchToggle(){
        return this.showt = !this.showt
      },
        //------------------------------------------------------------------------------CUSTOM search
        searchMovie(){
          if (this.keyword){
            const API_URL_SEARCH_MOVIE = `${API_URL}/api/v1/search/${this.keyword}` 
            axios({
              method: 'get',
              url: API_URL_SEARCH_MOVIE,
            })
              .then((response) => {

                this.$store.dispatch('search_movie', response.data)
                this.lst = this.$store.state.searchMovieList
                console.log('받아온 영화리스트',this.$store.state.searchMovieList )
              })
              .catch((error) => {
                console.log(error)
              })
            }
          },
    },
    created() {
        this.$store.state.searchMovieList=null
        if(this.keyword){
          this.searchMovie();
        }
    },
}
</script>

<style>
.genrebox{
  width:100%; 
  background-color:rgb(75, 75, 75);
  border: 1px solid rgb(75, 75, 75);;
}
.discoverypage{
  width:100%;
  height: 100%;
  padding-top:50px;
}
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
  .genrelist{
    display: flex;
    justify-content: center;
    flex-flow: row wrap;
  }
  .movieFrame{
    display: flex;
    justify-content: center;
    flex-flow: row wrap;
    padding: 1rem;
    height: 100%;
    width: 100%;
  }   
</style>