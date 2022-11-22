<template>
  <div class="contentPage">
    <h3>{{title}}</h3>
    <div>
      <img :src="url" :content="feed.content" style="max-width:100%;">
      <p>한줄평 : {{content}}</p>
    </div>
    <div v-if="isMyPage">
      <button v-if="!showEdit" @click="clickEdit">수정</button>
      <button v-if="!showEdit">삭제</button>
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
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
