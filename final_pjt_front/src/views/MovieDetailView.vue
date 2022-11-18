<template>
  <div>
      <h1>MovieDetail</h1>
      <p>제목 : {{movie.title}}</p>
      <p>시놉시스 : {{movie.overview}}</p>
      <img :src="poster" style="width:300px;" alt="">
      <hr>
      <h3>comments</h3>
      // 컴포넌트 새로 만들어서 댓글 표출하도록!
      <p>댓글 : {{movie.review_set}}</p>

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'MovieDetailView',
    data(){
        return{
            movie : null,
        }
    },
    computed:{
        poster(){
            const url = this.$store.state.BASE_POSTER_PATH + this.movie.poster
            return url
        }
    },
    created(){
        this.getMovieDetail()
    },
    methods:{
        getMovieDetail(){
            axios({
                method:'get',
                url:`${API_URL}/api/v1/movies/${this.$route.params.id}`
            })
                .then((res) => {
                    console.log(res)
                    console.log('데이터를 받았어요?')
                    this.movie = res.data
                })
                .catch((err) => {
                    console.log('데이터를 받지 못했어요')
                    console.log(err)
                })
        }
    }
}
</script>

<style>

</style>