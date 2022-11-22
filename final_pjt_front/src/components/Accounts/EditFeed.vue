<template>
  <div>
    <br>
    <input type="text" v-model="feedContent">
    <br>
    <EditFeedStills 
      v-for="(image, key) in still_images"
      :key="image.id"
      :pk="key"
      :image="image"
      @imageId="getImgId"
      :imgid = image.id
    />
    <br>
    <p>선택한 이미지 = {{selectedImgId}}</p>
    <button @click="editFeed">수정완료</button>
  </div>
</template>

<script>
import EditFeedStills from '@/components/Accounts/EditFeedStills'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'EditFeed',
  data(){
    return{
      selectedImgId : '',
      feedContent : ''
    }
  },
  components:{
    EditFeedStills,
  },
  created(){
    this.set()
  },
  props :{
    still_images : Array,
    content : String,
    img : String,
    feedId : Number,
  },
  methods:{
    set(){
      this.feedContent = this.content
    },
    getImgId(imageId){
      console.log(this.still_images)
      this.selectedImgId = imageId
    },
    editFeed(){
      const content = this.feedContent
      let image_path = ''
      if(!this.selectedImgId){
        image_path = this.img
      } else {
        image_path = this.still_images[this.selectedImgId].image_path
      }

      axios({
          method:'put',
          url: `${API_URL}/user/feed/${this.feedId}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
          data :{
            content : content,
            image_path : image_path
          }
        })
        .then((res) => {
          console.log(res.data)
          this.$emit('changedImg', [image_path, content])
        })
        .catch(() => {return false})
    }
  }
}
</script>

<style>

</style>