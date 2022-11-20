<template>
  <div>
    <h1>Movie Page</h1>
    <button @click="toggleOnOff">User Recommend</button>
    
    <div v-show="!isActive"><MovieList/></div>

    <!-- button toggle -->
    <div v-show="isActive"><UserMovieList/></div>

  </div>
</template>

<script>
import MovieList from '@/components/Movies/MovieList'
import UserMovieList from '@/components/Movies/UserMovieList'
export default {
    name : 'MovieView',
    data() {
        return {
        isActive: false
        }
    },
    components:{
        MovieList,
        UserMovieList,
    },
    
    created(){
        this.getMovies()


    },
    methods:{
        getMovies(){
            this.$store.dispatch('getMovies')
        },
        toggleOnOff: function() {
            this.isActive = !this.isActive;
        }

       
    }

}
</script>

<style>

</style>