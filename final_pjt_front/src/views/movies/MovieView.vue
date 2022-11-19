<template>
  <div>
    <h1>Movie Page</h1>
    <MovieList/>

  </div>
</template>

<script>
import MovieList from '@/components/Movies/MovieList'
export default {
    name : 'MovieView',
    components:{
        MovieList,
    },
    created(){
        this.getMovies()
    },
    methods:{
        getMovies(){
            this.$store.dispatch('getMovies')
        }
    }

}
</script>

<style>

</style>