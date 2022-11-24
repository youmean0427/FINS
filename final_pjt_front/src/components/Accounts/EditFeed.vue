<template>
  <div style="width:100%">
    <br>
    <div class="stillbox">
      <EditFeedStills 
        class="stillitems"
        v-for="(image, key) in still_images"
        :key="image.id"
        :image="image"
        @selectedImg="getImgId(key)"
        :imgid = image.id
      />
    </div>
    <br>
    <div class="editfeedcon">
      <input type="text" v-model="feedContent">
      <b-button @click="editFeed">수정완료</b-button>
    </div>
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
    console.log('sills', this.still_images)
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
      this.$emit('selectedImg', this.still_images[imageId].image_path)
      this.selectedImgId = imageId
    },
    editFeed(){
      const content = this.feedContent
      let image_path = ''
      if(this.selectedImgId === 0){
        image_path = this.still_images[this.selectedImgId].image_path
      } else if(!this.selectedImgId){
        image_path = this.img
      } else {
        image_path = this.still_images[this.selectedImgId].image_path
      }
      console.log('요청정보 :::: ', content, image_path)
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
  .stillbox{
    display: flex;
    height: 400px;
    justify-content: center;
    flex-wrap: wrap;
  }
  .editfeedcon{
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    padding-right: 10px;
    bottom: 10px;
  }
  .editfeedcon input{
    width : 80%;
    border-radius: 7px;
  }
  .editfeedcon>input:hover{
    border: 1px solid navy;
  }
  .editfeedcon>button{
    background-color: aliceblue;
    color: navy;
  }
</style>