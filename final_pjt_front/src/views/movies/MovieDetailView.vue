<template>
  <div style="margin-left: 20%; margin-right: 20%;">
    <img src="@/assets/Movie.png" alt="" width="150px">
      <!-- <h1>MovieDetail</h1> -->
      <hr>
      <div id="layout_01">
    
        
        <h1>여백</h1>
        <img :src="poster" style="width:300px;" alt="">
        <h1>여백</h1>
        <div id="layout_02">
            <img :src="this.stil_image[0].image_path" class="size_size_0" alt="">
        <div id="layout_01">
            <img :src="this.stil_image[1].image_path" class="size_size_1" alt="">
            <img :src="this.stil_image[2].image_path" class="size_size_2" alt="">
        </div>
        </div>
       
        <!-- <img :src="movie.stil_image" style="width:300px;" alt=""> -->
        </div>

        <br>
        <br>
        <div id="layout_01">
            <div width="600px">
            <iframe 
            width="600px"
            height="400px"
            :src="videoUrl"></iframe>
            </div>
            <h1>여백</h1>
            <div id="layout_02">
                <h2 class="font_font_big">{{movie.title}}</h2>
                <hr>
                <!-- <p v-if="loggedIn"><button @click="likeMovie">{{ this.input_value }}</button></p> -->
                <p v-if="loggedIn"><img type='button' @click="likeMovie" :src='require(`@/assets/${lovevalue}.png`)' width="50px"></p>
                
                <!-- 좋아요 유저 확인용 -->
                <!-- <p>{{ movie.movie_like_user}}</p> -->
                <p class="font_font">{{movie.overview}}</p>
                
            </div>
        </div>

        <br>
        <br>
        <RecoMovieList :movieKeyword= 'movie' />
        <br>
        
        <br>
        <!-- <p>댓글 : {{movie.review_set}}</p> -->
        <img src="@/assets/Reviews.png" alt="" width="150px">
        <br>
        <hr>
        <br>
        <CreateReview :movieId = 'movie.id'/>
        <ReviewList :movieReviewSet ='movie.review_set'/>





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
            // input_value: '좋아요',
            lovevalue: 'Love',
            movie_key: 0,
            stil_image: [],
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
                this.movie_key = res.data.movie_key;
                this.getStil()
                
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

        // ________________Like__________________
      
        islike(){

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
                    this.lovevalue = "Unlove"
                    }
                }
                
                
            })
            .catch((err) => {
                console.log("데이터를 받지 못했어요");
                console.log(err);
            });
        },

         // ________________Stil__________________

         getStil(){
            console.log(this.movie_key)
            axios({
                method: "get",
                url: `http://127.0.0.1:8000/api/v1/movie/${this.movie_key}/stills`,
            
            })
            .then((res) => {
                // console.log(res);
                console.log("데이터를 받았어요!");
                console.log(res.data)
                this.stil_image = res.data
                
            
                
                
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
        //_______________________ No ____________________
        // islike(){
        //     if(this.$store.state.likeCheck){
        //         return '싫어요'
        //     } else {
        //         return '좋아요'
        //     }
        // },

        // __________________YOUTUBE__________________
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
        // __________________END YOUTUBE__________________

        // __________________LOGIN__________________
        loggedIn(){
            return this.$store.getters.isLogin
    }
    },

    created() {
        this.getMovieDetail()
        this.islike()
       

        
    },
    
    
}
</script>

<style>
/* 가로로 정렬 */
#layout_01 {
    display: flex;
    flex-direction: row;

    justify-content: center;

    
}

#layout_02 {
    display: flex;
    flex-direction: column;

    justify-content: center;

    
}
.font_font {
         font-family: 'NanumGothic';
        font-style: normal;
        /* font-weight: 700; */
        font-size: 20px;
        /* line-height: 37px; */

        color: #000000;
    }

.font_font_big {
    font-family: 'NanumGothic';
    font-style: normal;
    /* font-weight: 700; */
    font-size: 30px;
    /* line-height: 37px; */

    color: #000000;
}
.size_size_0 {
/* position: absolute; */
width: 500px;
height: 200px;
left: 868.65px;
top: 0px;

transform: rotate(5deg);
}

.size_size_1 {
/* position: absolute; */
width: 300px;
height: 150px;
left: 868.65px;
top: 0px;

transform: rotate(-10deg);
}

.size_size_2 {
/* position: absolute; */
width: 300px;
height: 150px;
left: 868.65px;
top: 0px;

transform: rotate(10deg);
}


</style>