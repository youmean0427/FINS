<template>
  <div>
    <h1>{{ username }}</h1>
    <div v-if='isMyPage'>
      <h1>마이페이지</h1>
      <router-link :to="{ name: 'ProfileEditView' }">회원정보 수정</router-link>
    </div>
    <FeedList :likeMovies="likeMovies"/>
  </div>
</template>

<script>
import FeedList from '@/components/Accounts/FeedList.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'ProfileView',
    components: {
      FeedList,
    },
    data(){
      return {
        username : this.$route.params.username,
        likeMovies : [],
      }
    },
    computed:{
       isLogin() {
            return this.$store.getters.isLogin
        },
      // 접속한 사용자가 프로필 사용자인지 확인하고 true,false를 리턴
      isMyPage(){
        if (this.isLogin === false){
          return false
        } else {
          return this.$store.dispatch('isMyPage', this.username)
        }
      },
    },
    created(){
      this.user()
    },
    methods:{
      user(){
        // http://127.0.0.1:8000/user/profile/mincho3/
        // like_movies.[num].id
        axios({
        method: 'get',
        url: `${API_URL}/user/profile/${this.username}/`,
      })
        .then((res) => {
          this.likeMovies = res.data.like_movies
          console.log(this.likeMovies)
        })
        .catch(() => {return false})
      
      }
    }
}
</script>

<style>

</style>