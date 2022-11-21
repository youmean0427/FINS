<template>
  <div>
    <h1>{{ username }}</h1>
    <div v-if='isMyPage'>
      <h1>마이페이지</h1>
      <router-link :to="{ name: 'ProfileEditView' }">회원정보 수정</router-link>
    </div>
    <FeedList :likeMovies="likeMovies"/>

    <button @click="followCheck">{{isfollow}} </button>

  </div>
</template>

<script>
import FeedList from '@/components/Accounts/FeedList.vue'
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'ProfileView',
    components: {
      FeedList,
    },
    data(){
      return {
        username : this.$route.params.username,
        likeMovies : [],

        isfollow : '팔로우'

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

      // 이건 팔로우기능-----------
  
    },
    created(){
      this.getFollowings()
    },
      // 팔로우 목록 받기
    methods:{
      getFollowings(){
        this.$store.dispatch('getFollowings', this.username)
        this.followingList = this.$store.state.followingList
        for (const vm of this.followingList){
          if (vm === this.username){
            this.isfollow = '언팔로우'
            return
        } else {
          this.isfollow = '팔로우'
        }
        }
      },
    // 팔로우 요청
      followCheck(){
        this.getFollowings()
        return this.$store.dispatch('follow', this.username)
      }
    // -----------여기까지 팔로우기능
    
    }
}
</script>

<style>

</style>