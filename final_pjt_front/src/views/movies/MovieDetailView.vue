<template>
  <div style="margin-left: 10%; margin-right: 10%; margin-top: 3%;">
    <div>
    <img src="@/assets/Movie.png" alt="" width="150px">
      <!-- <h1>MovieDetail</h1> -->
      <hr>
        
      <div id="layout_01">
    
        
        <br>
        <img :src="poster" style="width:300px;" class= "poster_size" alt="">
        <br>
        <div id="layout_02">
            <img :src="this.stil_image[0].image_path" class="size_size_0 img2" alt="">
        <div id="layout_01">
            <img :src="this.stil_image[1].image_path" class="size_size_1 img2" alt="">
            <img :src="this.stil_image[2].image_path" class="size_size_2 img2" alt="">
        </div>
        </div>
       
        <!-- <img :src="movie.stil_image" style="width:300px;" alt=""> -->
        </div>

        <br>
        <br>
        <div id="layout_01">
            <div width="600px" style="margin-right: 20px">
            <iframe 
            width="600px"
            height="400px"
            
            :src="videoUrl"></iframe>
            </div>
            
            
            <div id="layout_02">
                <h2 >{{movie.title}}</h2>
                <hr>
                <!-- <p v-if="loggedIn"><button @click="likeMovie">{{ this.input_value }}</button></p> -->
                <p v-if="loggedIn"><img type='button' class='afterlike' @click="likeMovie" :src='require(`@/assets/${lovevalue}.png`)' width="50px"></p>
                
                <!-- 좋아요 유저 확인용 -->
                <!-- <p>{{ movie.movie_like_user}}</p> -->
                <p style="line-height:1.8">{{movie.overview}}</p>
                
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
         
            lovevalue: 'Unlove',
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
                console.log(this.user_id)
                // console.log(this.user_id)
                // console.log((this.movie.movie_like_user))
                
                for (const i in this.movie.movie_like_user ){
                    console.log("이것이다", this.movie.movie_like_user[i])
                    if (((this.user_id) === (this.movie.movie_like_user[i]))) {
       
                    this.lovevalue = "Love"
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
                url: `http://127.0.0.1:8000/api/v1/movie/${this.movie.id}/stills`,
            
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

 @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@800&display=swap');
    
* {
  font-family: 'Nanum Gothic', sans-serif;
  color: black;
}
/* 가로로 정렬 */

#layout_01 {
    display: flex;
    flex-direction: row;

    justify-content: center;

    
}
.img2 {
  animation: rotate_image 6s linear infinite, scale1 6s linear infinite;
  transform-origin: 50% 50%;
}

#layout_02 {
    display: flex;
    flex-direction: column;

    justify-content: center;

    
}

.size_size_0 {
/* position: static; */
width: 500px;
height: 200px;
left: 868.65px;
top: 0px;
overflow: hidden;
transform: rotate(5deg);
}

.size_size_1 {
/* position: absolute; */
width: 300px;
height: 150px;
left: 868.65px;
top: 0px;
overflow: hidden;
transform: rotate(-10deg);
}

.size_size_2 {
/* position: absolute; */
width: 300px;
height: 150px;
left: 868.65px;
top: 0px;
overflow: hidden;
transform: rotate(10deg);


}

.size_size_0:hover{
transform: scale(1.2) ;
transition: 0.5s ease;
z-index: 2;

}

.size_size_1:hover{
transform: scale(1.2) ;
transition: 0.5s ease;
z-index: 2;
}

.size_size_2:hover{
transform: scale(1.2) ;
transition: 0.5s ease;
z-index: 2;
}

.poster_size:hover{
transform: scale(1.05);
transition: 0.5s ease;
z-index: 2;
}
.afterlike:hover{
transform: scale(1.2);
transition: 0.5s ease;
}






</style>