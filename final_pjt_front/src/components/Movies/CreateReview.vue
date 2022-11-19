<template>
  <div class="review_form">
      <div>
          <h3>{{review.username}} | {{review.content}}</h3>

      </div>
      <hr>
      <h1>댓글 작성</h1>
        <form @submit.prevent="createReview">
            <label for="content">내용 ㅣ </label>
            <input type="text" id="content" v-model.trim="content">
            <input type="submit" id="sumbit">
        </form>
        <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'CreateReview',
    data() {
        return{
            content: null,
        }
    },
    computed:{
        isLogin() {
        return this.$store.getters.isLogin
        },
        review(){
            // movieId 넘겨주면 review_set 리턴해주는 actions 랑 mutations를 만들자
            movie = this.$store.state.movies
            console.log(this.$store.state.movies[this.movieId])
            return {username:'블랙팬서', content : '하하'}
        },
    },
    props:{
        movieId : Number,
    },

    methods: {
        createReview(){
            if (this.isLogin === false){
                console.log('로그인이 필요한 서비스입니다')
                alert('로그인이 필요한 서비스입니다.')
                this.$router.push({name : 'LogInView'})            // 로그인 페이지로 이동하는 버튼을 추가하는 것으로 바꾸기
                return
            } else {
                console.log('로그인이 필요한 서비스입니다만..?')
                const content = this.content
                if(!content) {
                    alert('내용을 입력하세요')
                    return
                }
                axios({
                    method: 'post',
                    url: `${API_URL}/api/v1/movies/1/createreview/`, //!!!!!!!!!!!!!!!!!!로그인 기능 구현 후 바꿀 부분
                    headers: {
                        Authorization: `Token ${this.$store.state.token}`
                    },
                    data: {
                        content : content,
                    }
                })
                .then((res) => {
                    console.log(res)
                    this.$router.push({name: 'MovieView'})
                })
                .catch(() => {this.$router.push({name: 'MovieView'})})
            }
        }
    }

}
</script>

<style>
    .review_form{
        margin-bottom: 300px;
    }
</style>