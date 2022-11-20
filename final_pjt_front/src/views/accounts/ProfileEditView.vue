<template>
  <div>
    <h1>회원정보 수정</h1>
    <form @submit.prevent="editProfile">
      <label for="username">닉네임 : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="email"> 이메일 : </label>
      <input type="text" id="email" v-model="email">
      <p id="validEmail">{{validEmail}}</p><br>
      <br>
      <label for="profile_img"> 프로필사진 : </label>
      <input v-if="profile_img" type="image" id="profile_img" v-model="profile_img"><br>
      
      <input @click="editProfile" type="button" value="EditProfile">
    </form> 
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name : 'ProfileEditView',
  data(){
    return{
      email : null,
      username : '',
      profile_img :null, 
      validEmail :'',
      is_valid_e : false,
    }
  },
  created(){
    this.getUser()
  },
  methods:{
    isValidEmail(){
      if (!this.email) {
        this.validEmail = ''
      } else {
        if (!this.email.includes('@')){
          this.validEmail = '유효한 이메일 형식을 입력하세요!'
          this.is_valid_e = false
          return
        } else if (!this.addr.includes('.')){
          this.validEmail = '유효한 이메일 형식을 입력하세요!'
          this.is_valid_e = false
          return
        } else if(this.email.includes('@') && this.addr.includes('.')){
          this.validEmail = ''
          this.is_valid_e = true
          return
        } else {
          this.is_valid_e = false
        }
      }
    },
    getUser(){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.email = res.data.email
          this.username = res.data.username
          this.profile_img = res.data.profile_img
        })
        .catch((err) => {
          console.log(err)
        })
      },
      editProfile(){
        const username = this.username
        const email = this.email
        const profile_img = this.profile_img
        const payload = {
          username,
          email,
          profile_img
        }
        this.$store.dispatch('editProfile', payload)
      }
  }
}
</script>

<style>

</style>