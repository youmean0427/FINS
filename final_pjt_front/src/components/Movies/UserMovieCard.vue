<template>
    <div>
  
      <h5>{{ movie[1] }}</h5>
      <p>{{ movie[2] }}</p>
      <img :src="movie[4]" style="width:300px;">
  
      <router-link :to="{ name: 'MovieDetailView', params: { id: movie[0] } }">
        [DETAIL]
      </router-link>
      
      <hr>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserMovieCard',
    props: {
      movie: Array,
    }
  }
  </script>
  
  <style>
  
  </style>
  