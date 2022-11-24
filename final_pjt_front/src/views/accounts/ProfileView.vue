<template>
  <div id="profileView">
    <h1>{{ username }}</h1>
    <div id="btns">
      <div v-if='isMyPage'>
        <router-link :to="{ name: 'ProfileEditView' }">회원정보 수정</router-link>
      </div>
      <div v-if="!isMyPage">
        <b-button @click="followCheck">{{isfollow}} </b-button>
      </div>
    </div>
    <div class="layoutBrn">
      <b-button class="btn listbtn" @click="showList = true"><img class="listbtnimg"
        src="https://user-images.githubusercontent.com/87971876/203548123-671886dc-e145-43ae-9200-497e93c14ff1.png" alt="">
      </b-button>
      <b-button class="btn listbtn" @click="showCard"><img class="listbtnimg" src="https://user-images.githubusercontent.com/87971876/203549185-61ad8416-cb3f-46c0-8c22-1a0025a14ba4.png" alt=""></b-button>
    </div>
    <FeedListType v-if="showList" :likeMovies="likeMovies" :username="username" @showFeedModal="showFeedModal"/>
    <FeedCardType v-if="!showList" :likeMovies="likeMovies" :username="username"  @showFeedModal="showFeedModal"/>

    <FeedDetailView v-if="showModal" @close-modal="closeModal">
      <FeedModal :feedId="feedId" :username="username"/>
    </FeedDetailView> 
  </div>
</template>

<script>
import FeedDetailView from '@/components/Accounts/FeedDetailView'
import FeedListType from '@/components/Accounts/FeedListType.vue'
import FeedCardType from '@/components/Accounts/FeedCardType.vue'
import FeedModal from '@/components/Accounts/FeedModal.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ProfileView',
    components: {
      FeedListType,
      FeedDetailView,
      FeedModal,
      FeedCardType,
    },
    data(){
      return {
        username : this.$route.params.username,
        likeMovies : [],

        isfollow : '팔로우',

        showModal : false,
        feedId : '',
        showList : false,
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
      showFeedModal(id){
        console.log('modal~~~~~~~~~~~~~~~~~~',id)
        this.feedId = id
        this.showModal = true
        console.log(this.showModal)
      },
    // -----------여기까지 팔로우기능
      closeModal(){
        this.showModal = false
        location.reload(true);
      },
      showCard(){
        this.showList = false
      }
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
    padding-left: 10%;
    padding-right: 10%;

  }
  #editBtn{
    background-color: rgb(113, 113, 113);
    
    width: fit-content;
    height: 2.5em;
    padding: 10px;
    border-radius: 10px;
  }
  #editBtn > a {
    color:white;
  }
  #btns{
    
  }
  .layoutBrn button {
    background-color: white;
    color: rgb(17, 17, 17);
  }
  .listbtnimg{
    object-fit:fill;
    height: 100%;
    width: 100%;
  }
  .listbtn{
    overflow: hidden;
    width:50px;
    border: none;
  }
  .listbtn:hover{
    background-color: #ffffff;
  }
</style>