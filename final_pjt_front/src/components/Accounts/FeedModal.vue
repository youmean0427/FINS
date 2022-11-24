<template>
  <div class="container">
    <div class="row contentPage">
      <div class="col-6 feedleft">
          <img v-if="testImg" :src="testurl" alt="">
          <img v-else :src="url" :content="feed.content" style="width:100%;">
      </div>
      <div class="col-6 feedright">
        <div class="userprofile">
          <img src="https://user-images.githubusercontent.com/87971876/203572590-35117aa5-e24e-4c08-9402-489b2c9888da.png" alt="">
          <p>{{username}}</p>
        </div>
        <hr>
        <div v-if="showEdit" class="rightmiddle">
            <EditFeed :still_images="still_images" 
                    :content="feed.content" :img="feed.image_path" 
                    :feedId="feed.id" @changedImg="updateFeed" @selectedImg="selectedImg"/>
        </div>
        <div v-else class="rightmiddle">
          <div style="width:100%">
            <h4>{{title}}</h4>
            <p>한줄평 : {{content}}</p>
          </div>
          <div class="feedbtns" style="width:100%">
            <b-button v-if="!showEdit" @click="likeFeed" class="heartbtn"><img :src="hearturl" alt="사진없음"></b-button>
            <div v-if="isMyPage">
              <b-button class="feededitbtn" @click="clickEdit">수정</b-button>
              <b-button class="feededitbtn" v-b-modal.modal-1>삭제</b-button>
              <b-modal ref="my-modal" hide-footer id="modal-1" title="BootstrapVue">
                <p class="my-4">{{title}}을 프로필 피드에서 삭제하시겠습니까?</p>
                <b-button class="mt-3" variant="outline-danger" block @click="hideModal">취소</b-button>
                <b-button class="mt-3" variant="outline-warning" block @click="deleteFeed">삭제하기</b-button>
              </b-modal>
            </div>
          </div>
        </div>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import EditFeed from '@/components/Accounts/EditFeed.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "FeedModal",
  components:{
    EditFeed,
  },
  data(){
    return{
      feed : '',
      movie : [],
      showEdit : false,
      still_images : [],
      testImg : false,
      testurl : '',
      liekstatus : false
    }
  },
  computed:{
    title(){
      return this.movie.title
    },
    url(){
      return this.feed.image_path
    },
    content(){
      return this.feed.content
    },
    hearturl(){
      if (this.likestatus){
        return 'https://user-images.githubusercontent.com/87971876/203576382-75664732-87ee-4657-acad-fdad8d9c1c18.png'
      } else {
        return 'https://user-images.githubusercontent.com/87971876/203677620-815c452a-e650-4980-843a-bdc7865bf159.png'
      }
    }
  },
  props: {
    id: Number,
    user : String,
    username : String,
  },
  created(){
    this.feedInfo()
  },
  methods:{
    likeFeed(){
      // 로그인한 상태가 아니면 로그인하라고 alert
      this.liekstatus = this.$store.dispatch('like_feed', this.feed.id)
    },
    selectedImg(url){
      this.testImg = true
      this.testurl = url
    },
    getStill(id){
      axios({
          method:'get',
          url: `${API_URL}/api/v1/movie/${id}/stills/`,
        })
        .then((res) => {
          this.still_images = res.data
          console.log('요청받은 데이터 ====', this.movie.movie_key)
        })
        .catch(() => {return false})
    },
    clickEdit(){
      this.showEdit = true
    },
    feedInfo(){
      axios({
          method:'get',
          url: `${API_URL}/user/feed/${this.id}/`,
        })
        .then((res) => {
          this.feed = res.data
          this.getStill(this.feed.movie_id)
          console.log('피드정보', this.feed )
        })
        .catch(() => {return false})
    },
    isMyPage(){
        if (this.isLogin === false){
          return false
        } else {
          return this.$store.dispatch('isMyPage', this.username)
        }
      },
    updateFeed(data){
      this.showEdit = false
      console.log(data)
      this.feed.image_path = data[0]
      this.feed.content = data[1]
      this.testImg = false
    },
    hideModal(){
      this.$refs['my-modal'].hide()
    },
    deleteFeed(){
      axios({
          method:'delete',
          url: `${API_URL}/user/feed/${this.id}/`,
          headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
        })
        .then(() => {
          console.log('피드 삭제됨')
        })
        .catch(() => {return false})
        this.$refs['my-modal'].hide()
        this.$router.push({ name: 'ProfileView', params: { username: this.username } })
    }

  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .contentPage{
    /* display: flex;
    flex-flow: row wrap; */
    height: 100%;
    max-height: inherit;
    width: 100%;
    padding: 0;
    margin:0;
  }
  .container{
    max-height: max-content;
    width: 100%;
    padding: 0;
    height: 100%;
  }
  .feedleft, .feedright{
    padding: 0;
    height: 100%;
  }
  .feedleft{
    height: 100%;
    background-color: black;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow: hidden;
    border-radius: 7px 0 0 7px;
  }
  .feedleft img{
    object-fit: cover;
  }
  .feedright{
    padding-top: 10px;
    text-align: left;
  }
  .userprofile{
    display: flex;
    max-width: inherit;
    padding-left:10px;
  }
  .userprofile img{
    width: 50px;
    border-radius: 50%;
  }
  .heartbtn img{
    width: 30px;
  }
  .heartbtn{
    background-color: transparent;
    border: none;
  }
  .userprofile p{
    font-size: 1.2em;
    padding-left: 10px;
    margin: 0;
    padding-top: 10px;
  }
  .rightmiddle{
    /* height: 70%; */
    display: flex;
    flex-flow: column wrap;
    align-content: space-between;
    padding-left: 10px;
    justify-content: space-between;
    height: 65%;
    
  }
  .feedbtns{
    display: flex;
    justify-content:space-between;
    width: 90%;
  }
  .feededitbtn{
    background-color: transparent;
    border: none;
    color: grey;
  }
</style>
