<template>
    <div>
  
      <h5>{{ movie.id }}</h5>
      <p>{{ movie.title }}</p>
      <img :src="movie.stil_image" style="width:300px;">
  
      <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
        [DETAIL]
      </router-link>
      
      <hr>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserMovieCard',
    props: {
      movie: Object,
    }
  }
  </script>
  
  <style>
  
  </style>
  