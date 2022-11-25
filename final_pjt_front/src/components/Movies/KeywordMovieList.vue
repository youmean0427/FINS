<template>
    <div class="movieCardFrame2">
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
  .movieCardFrame2 {
    display: flex;
    justify-content: center;
    flex-flow: row wrap;
    /* height: 100%; */
    /* width: 30%; */
    /* padding-left: 10%; */
    /* align-items: flex-end; */
    flex-wrap: wrap;}
  </style>