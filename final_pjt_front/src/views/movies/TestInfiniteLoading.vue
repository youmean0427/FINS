<template>
  <div>
    <h1>Infinite Page</h1>    
    <MovieCard
      v-for="movie in movieList"
      :key="movie.id"
      :movie="movie"
    />
    <infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
  </div>
</template>

<script>
import MovieCard from '@/components/Movies/MovieCard'
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    
    name : 'MovieView',
    components:{
        MovieCard,
        InfiniteLoading
    },
    data(){
        return{
            limit: 0,
            movieList:[],
        }
    },
    created(){
        this.getMovies()
        // this.$http.get('http://127.0.0.1:8000/api/v1/movies/limit/' + this.limit)
        //     .then((response) => {
        //         this.movieList = response.data
        //     })
    },
    methods:{
        infiniteHandler($state){
            this.limit += 10
            axios({
            method:'get',
            url: `${API_URL}/api/v1/movies/limit/${this.limit}`,
            })
            .then(response => {
                    setTimeout(() => {
                        if(response.data.length){
                            this.movieList = this.movieList.concat(response.data)
                            $state.loaded(); // 데이터 로딩중 
                            this.limit += 10
                            if(this.movieList.legth / 10 == 0){
                                $state.complete()
                            }
                        } else {
                            $state.complete()
                        }
                    }, 1000)
                }).catch(error => {
                    console.error(error)
                })
        },
        // https://cntechsystems.tistory.com/58 참고 
    }

}
</script>

<style>

</style>