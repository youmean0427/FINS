<template>
  <div>
    <b-button @click="toggleOnOff">당신을 위한 추천영화</b-button>
    
    <div v-show="!isActive"><InfiniteMovieList/></div>

    <!-- button toggle -->
    <div v-show="isActive"><UserMovieList/></div>

  </div>
</template>

<script>
import InfiniteMovieList from '@/views/movies/InfiniteMovieList'
import UserMovieList from '@/components/Movies/UserMovieList'
export default {
    name : 'MovieView',
    data() {
        return {
        isActive: false
        }
    },
    components:{
        InfiniteMovieList,
        UserMovieList,
    },
    methods:{
        toggleOnOff: function() {
            this.isActive = !this.isActive;
        }

       
    }

}
</script>

<style>

</style>