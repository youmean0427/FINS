<template>
  <div style="margin-left: 10%; margin-right: 10%;">
    <!-- {{this.$route.params}} -->
    
    <h2 style='text-transform: uppercase' >{{this.keyword_name}}</h2>
    <hr>
    <KeywordMovieList :movie="movie"/>
    
  
    
  
  </div>

</template>

<script>

import axios from 'axios'
import KeywordMovieList from '@/components/Movies/KeywordMovieList'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: "KeywordMovieView",
    data() {
        return {
            movie: null,
            keyword_name : this.$route.params.keyword_name
            // null 값 오류 확인
        };
    },
    components: {
      KeywordMovieList
    },
    methods:{
      getMovieDetail() {
              axios({
                  method: "get",
                  url: `${API_URL}/api/v1/movies/keyword/${this.$route.params.id}`
              })
              .then((res) => {
                  console.log(res);
                  console.log("데이터를 받았어요?");
                  this.movie = res.data;
              })
              .catch((err) => {
                  console.log("데이터를 받지 못했어요");
                  console.log(err);
              });
          },
    },
    created() {
      this.getMovieDetail();
    },

}
</script>

<style>

</style>