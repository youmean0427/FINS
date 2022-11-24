<template>
  <div style="margin-right: 20%; margin-left: 20%;">

        <form @submit.prevent="createReview">
            <div class="input-group mb-2" >
            <input type="text" style="text-align:center;  border:none;" class="form-control" id="content" v-model.trim="content">
          
            <button class="btn btn-outline-secondary" type="submit" id="submit" style="border:none">+</button>
            </div>
            <img src="@/assets/Line_00.png" alt="" width="100%px" >
        </form>
          
    <!-- <progress></progress> -->



             
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'CreateReview',
    data() {
        return{
            content: null
        }
    },
    computed:{
        isLogin() {
            return this.$store.getters.isLogin
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
                    url: `${API_URL}/api/v1/movies/${this.movieId}/createreview/`, //!!!!!!!!!!!!!!!!!!로그인 기능 구현 후 바꿀 부분
                    headers: {
                        Authorization: `Token ${this.$store.state.token}`
                    },
                    data: {
                        content : content,
                    }
                })
                .then(() => {
                    // this.$router.push({name: 'MovieDetailView'})
                    // go를 씀 
                    this.$router.go(this.$router.currentRoute)
                })
                .catch(() => {
                    // this.$router.push({name: 'MovieView'
                    alert('댓글 작성 실패!')
                })
            }
        }
    },

}
</script>

<style>


    
</style>