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
      <p><button @click="likeMovie">{{ this.input_value }}</button></p>

      <p> {{ this.movie.movie_like_user }} </p>
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
            this.$router.go(this.$router.currentRoute)
            return this.$store.dispatch('like_movie', this.movie.id)
        },

        islike(){
            
            
            // if(mlu.includes(nup)){
            //     return '싫어요'
            //     } else {
            //     return '좋아요'
            // }


            // if(this.$store.state.likeCheck){
            //     return '싫어요'
            // } else {
            //     return '좋아요'
            // }

            axios({
                method: "get",
                url: `http://127.0.0.1:8000/accounts/user/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
            })
            .then((res) => {
                // console.log(res);
                console.log("데이터를 받았어요!");
                this.user_id = res.data.id;
                // console.log(this.user_id)
                // console.log((this.movie.movie_like_user))
                
                for (const i in this.movie.movie_like_user ){
                    console.log("이것이다", this.movie.movie_like_user[i])
                    if (((this.user_id) === (this.movie.movie_like_user[i]))) {
                    this.input_value = "싫어요"
                    }
                }
                
                
            })
            .catch((err) => {
                console.log("데이터를 받지 못했어요");
                console.log(err);
            });
        },
        
        
        
        
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
        videoUrl(){
            const keykey = this.movie.video_path
            // console.log(keykey)
            // String 변환
            const index_e = String(keykey).indexOf('=')
            // console.log(index_e)
            const youtube_key = String(keykey).slice(index_e+1)
            // console.log(youtube_key)
            return 'https://www.youtube.com/embed/'+ youtube_key
        },
        
    },
    mounted() {
        this.islike()

    },

    created() {
        this.getMovieDetail()
        this.islike()

        
    },
    
    
}
</script>

<style>

</style>