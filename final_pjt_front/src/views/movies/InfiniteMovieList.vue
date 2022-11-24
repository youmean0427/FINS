<template>
  <div class="movieCardFrame">
    <MainMovieCard
      v-for="movie in movieList"
      :key=movie.id
      :movie="movie"
    />
    <infinite-loading @infinite="infiniteHandler" spinner="default"></infinite-loading>
  </div>
</template>

<script>
import MainMovieCard from '@/components/Movies/MainMovieCard'
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'
const URL = 'http://127.0.0.1:8000/api/v1/movies/limit/'

export default {
    
    name : 'InfiniteMovieList',
    components:{
        MainMovieCard,
        InfiniteLoading
    },
    data(){
        return{
            limit: 0,
            movieList:[],
        }
    },
    created(){
        {
        axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/v1/movies/limit/${this.limit}`,
        })
        .then(response => {
                this.movieList = response.data
                this.limit+=21
            })

        }
    },
    methods:{
        infiniteHandler($state){
            axios({
            method:'get',
            url: `${URL}${this.limit}`,
            })
            .then(response => {
                    setTimeout(() => {
                        if(response.data.length){
                            this.movieList = this.movieList.concat(response.data)
                            $state.loaded(); // 데이터 로딩중 
                            this.limit += 21
                            if(this.movieList.legth / 21 == 0){
                                $state.complete()
                            }
                        } else {
                            $state.complete()
                        }
                        console.log(this.movieList)
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
    .movieCardFrame{
    display: flex;
    justify-content: center;
    flex-flow: row wrap;
    height: 100%;  
    width: 100%;
    flex-wrap: wrap;
    /* padding-left: 10%; */
    /* align-items: flex-end; */
  }   
</style>