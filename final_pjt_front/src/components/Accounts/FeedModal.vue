<template>
  <div class="content">
    <h1>title</h1>
    <div>
      <h2>{{id}}</h2>
      <h2>{{feed.content}}</h2>
      <img :src="feed.image_path" style="width:300px;">
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
  props: {
    id: Number,
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
