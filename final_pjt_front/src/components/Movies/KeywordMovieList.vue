<template>
    <div class="movieCardFrame">
      <KeywordMovieCard
        v-for="keyword_movie in movie"
        :key="keyword_movie.id"
        :keyword_movie="keyword_movie"
      />
    </div>
  </template>
  
  <script>
  import KeywordMovieCard from '@/components/Movies/KeywordMovieCard';
  export default {
      name: "KeywordMovieList",
      components: {
        KeywordMovieCard
      },
      props: {
          movie:Array
        }
  }
  </script>
  
  <style>
  
  </style>