<template>
    <div>
       <img src="@/assets/your_fins.png" width="25%" alt="">
       <div class="movieCardFrame">
        <UserMovieCard
          v-for="movie in this.user_movie_list"
          :key="movie.id"
          :movie="movie"
        />
       </div>
      </div>
  </template>
  
  <script>
  import UserMovieCard from '@/components/Movies/UserMovieCard'
  import axios from 'axios'


  const API_URL = 'http://127.0.0.1:8000'
  export default {
    name: 'UserMovieList',
    data() {
      return {
        user_movie_list: []
      }

    },
    components: {
        UserMovieCard,
    },
    computed: {
      movieList() {
        return this.$store.state.movies
      }
    },
    methods: {
        getUserMovieList() {
            axios({
                method: "get",
                url: `${API_URL}/api/v1/movies/${this.$store.state.now_user}`
            })
            .then((res) => {
                console.log(res);
                this.user_movie_list = res.data
                console.log("데이터를 받았어요!")
            })
            .catch((err) => {
                console.log("데이터를 받지 못했어요");
                console.log(err);
            });
        },
    },
    created() {
      this.getUserMovieList()
    }
  }
  </script>
  
  <style>
  .movie-list {
  }
  </style>
  