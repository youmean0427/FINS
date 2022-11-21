<template>
  <div>
      <h1>MovieDetail</h1>
      <iframe 
        width="600"
        height="400"
        :src="videoUrl"></iframe>

      <p>제목 : {{movie.title}}</p>
      <p>시놉시스 : {{movie.overview}}</p>
      <img :src="poster" style="width:300px;" alt="">
      <p><button @click="likeMovie">{{islike}}</button></p>
      <!-- <p> {{ movie }} </p> -->
      <hr>
      <RecoMovieList :movieKeyword= 'movie.keyword' />
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
import RecoMovieList from '@/components/Movies/RecoMovieList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: "MovieDetailView",
    data() {
        return {
            movie: '',
            // null 값 오류 확인
            // youtube_key:'kyMMq8Kz-8I'
            youtube_key: 1,
            user_id: '',
            input_value: '좋아요요'
        };
    },
    components: { 
        ReviewList,
        CreateReview,
        RecoMovieList,
    },
    // mounted:{
        
    // },
    methods: {
        getMovieDetail() {
            axios({
                method: "get",
                url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
            })
            .then((res) => {
                console.log(res);
                console.log("데이터를 받았어요!");
                this.movie = res.data;
            })
            .catch((err) => {
                console.log("데이터를 받지 못했어요");
                console.log(err);
            });
        },
        
    likeMovie() {
        return this.$store.dispatch('like_movie', this.movie.id)
        }
        
        
        
    },
    computed: {

        poster() {
            let url = ''
            // 데이터가 오기도 전에 요청이 되어서 404 Error, if문으로 해결
            if (this.movie.poster){
                url = this.$store.state.BASE_POSTER_PATH + this.movie.poster;
            }
            return url;
        },
        //============================수정 해야함=======================
        islike(){
            if(this.$store.state.likeCheck){
                return '싫어요'
            } else {
                return '좋아요'
            }
        }
    },

    created() {
        this.getMovieDetail()
        this.islike()

        
    },
    
    
}
</script>

<style>

</style>