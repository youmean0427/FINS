<template>
  <div>
      <h1>MovieDetail</h1>
      <p>제목 : {{movie.title}}</p>
      <p>시놉시스 : {{movie.overview}}</p>
      <img :src="poster" style="width:300px;" alt="">
      <!-- <p> {{ movie }} </p> -->
      <hr>
      <h3>comments</h3>
      <!-- <p>댓글 : {{movie.review_set}}</p> -->
      <ReviewList :movieReviewSet ='movie.review_set'/>
      <CreateReview :movieId = 'movie.id'/>
  </div>
</template>

<script>
import CreateReview from '@/components/Movies/CreateReview.vue'
import ReviewList from '@/components/Movies/ReviewList.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: "MovieDetailView",
    data() {
        return {
            movie: '',
            // null 값 오류 확인
        };
    },
    components: { 
        ReviewList,
        CreateReview 
    },
    // mounted:{
        
    // },
    computed: {
        poster() {
            const url = this.$store.state.BASE_POSTER_PATH + this.movie.poster;
            return url;
        }
    },
    methods: {
        getMovieDetail() {
            axios({
                method: "get",
                url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
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
        }
    },
    created() {
        this.getMovieDetail();
    },
    
    
}
</script>

<style>

</style>