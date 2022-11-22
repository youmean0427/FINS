<template>
  <div class="contentPage">
    <h3>{{title}}</h3>
    <div>
      <img :src="url" :content="feed.content" style="max-width:100%;">
      <p>한줄평 : {{content}}</p>
    </div>

    <b-button v-if="!showEdit" @click="likeFeed">좋아요</b-button>
    <div v-if="isMyPage">
      <b-button v-if="!showEdit" @click="clickEdit">수정</b-button>

       <b-button v-b-modal.modal-1>삭제</b-button>
        <b-modal ref="my-modal" hide-footer id="modal-1" title="BootstrapVue">
          <p class="my-4">{{title}}을 프로필 피드에서 삭제하시겠습니까?</p>
          <b-button class="mt-3" variant="outline-danger" block @click="hideModal">취소</b-button>
          <b-button class="mt-2" variant="outline-warning" block @click="deleteFeed">삭제하기</b-button>
        </b-modal>
      <EditFeed v-if="showEdit" :still_images="still_images" 
                :content="feed.content" :img="feed.image_path" 
                :feedId="feed.id" @changedImg="updateFeed" />
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
    }
  },
  props: {
    id: Number,
    user : String,
  },
  created(){
    this.feedInfo()
  },
  methods:{
    getStill(){
      axios({
          method:'get',
          url: `${API_URL}/api/v1/movie/${this.movie.movie_key}/stills/`,
        })
        .then((res) => {
          this.still_images = res.data
        })
        .catch(() => {return false})
    },
    clickEdit(){
      this.showEdit = true
      this.getStill()
    },
    feedInfo(){
      axios({
          method:'get',
          url: `${API_URL}/user/feed/${this.id}/`,
        })
        .then((res) => {
          this.feed = res.data
          this.movie = this.$store.state.movies[this.feed.movie_id]
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
</style>
