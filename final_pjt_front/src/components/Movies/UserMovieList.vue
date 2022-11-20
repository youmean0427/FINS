<template>
    <div class="">
      <h3>UserMovieList</h3>
      <UserMovieCard
        v-for="movie in 6"
        :key="movie.id"
        :movie="movieList[movie]"
      />
    </div>
  </template>
  
  <script>
  import UserMovieCard from '@/components/Movies/UserMovieCard'
  
  export default {
    name: 'UserMovieList',
    components: {
        UserMovieCard,
    },
    computed: {
      movieList() {
        return this.$store.state.movies
      }
    }
  }
  </script>
  
  <style>
  .movie-list {
    text-align: start;
  }
  </style>
  