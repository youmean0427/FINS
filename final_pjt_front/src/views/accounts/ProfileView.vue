<template>
  <div id="profileView">
    <h1>{{ username }}</h1>
    <div v-if='isMyPage'>
      <h1>마이페이지</h1>
      <router-link :to="{ name: 'ProfileEditView' }">회원정보 수정</router-link>
    </div>
    <FeedList :likeMovies="likeMovies"/>

    <button v-if="isNotMyPage" @click="followCheck">{{isfollow}} </button>

    <FeedDetailView v-if="showModal" @close-modal="showModal = false">
      <FeedModal :id="modalId" />
    </FeedDetailView> 
    <FeedList :likeMovies="likeMovies" @showFeedDetail="feedModal"/>
  </div>
</template>

<script>
import FeedDetailView from '@/views/accounts/FeedDetailView'
import FeedList from '@/components/Accounts/FeedList.vue'
import FeedModal from '@/components/Accounts/FeedModal.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ProfileView',
    components: {
      FeedList,
      FeedDetailView,
      FeedModal,
    },
    data(){
      return {
        username : this.$route.params.username,
        likeMovies : [],

        isfollow : '팔로우',

        showModal : false,
        modalId : '',
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
      isNotMyPage(){
        return this.isMyPage ? false : true
      }
  
    },
    created(){
      this.getFollowings()
      this.feeds()
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
      },
      feeds(){
        axios({
          method:'get',
          url: `${API_URL}/user/feedlist/${this.username}/`,
        })
        .then((res) => {
          this.likeMovies = res.data
          // console.log(typeof(res.data))
        })
        .catch(() => {return false})
      },
      feedModal(id){
        console.log('modal~~~~~~~~~~~~~~~~~~',id)
        this.modalId = id
        this.showModal = true
      }
    // -----------여기까지 팔로우기능
    
    }
}
</script>

<style>
  #profileView{
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>