<template>
  <div class="content">
    <h1>{{title}}</h1>
    <div>
      <img :src="feed.image_path" style="width:500px;">
      <p>한줄평 : {{feed.content}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "FeedModal",
  data(){
    return{
      feed : '',
    }
  },
  computed:{
    title(){
      return '하하'
      // state에 있는 영화 데이터에서 영화 feed.movie_id에 맞는 ..
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
    feedInfo(){
      axios({
          method:'get',
          url: `${API_URL}/user/feed/${this.id}/`,
        })
        .then((res) => {
          this.feed = res.data
        })
        .catch(() => {return false})
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
