<template>
  <div>
    <div id="layout_03">
      <form @submit.prevent="editProfile">
        <div style="z-index: 2;  position: absolute;">
          <img src="@/assets/Line_01.png" alt="" width="300px">
          </div>
            <div style="z-index: 1;">
                <img src="@/assets/ID.png" alt="" width="125px" >
            </div>
        <br>
        <div class="input-group" >
        <input type="text" id="username" v-model="username" style="text-align:center; border:none; width:300px" class="form-control"><br></div>
        <img src="@/assets/Line_00.png" alt="" width="300px">

        <br>
        <br>
        <div style="z-index: 2;  position: absolute;">
          <img src="@/assets/Line_01.png" alt="" width="300px">
          </div>
            <div style="z-index: 1;">
                <img src="@/assets/Email.png" alt="" width="200px" >
            </div>
        <br>
        <div class="input-group" >
        <input type="text" id="email" v-model="email" style="text-align:center; border:none; width:300px" class="form-control">
        <p id="validEmail">{{validEmail}}</p><br></div>
        <img src="@/assets/Line_00.png" alt="" width="300px">
        
        <br>
        <br>
        <div class="layout_04">
        <label for="profile_img"> 프로필사진 : </label>
        <input v-if="profile_img" type="image" id="profile_img" v-model="profile_img">
        <br>
        <img src="@/assets/Edit_button.png" @click="editProfile" type="button" value="EditProfile" width="200px">
        <br>
        <router-link :to="{ name: 'PasswordCheckView' }"><img src="@/assets/change_password.png" @click="editProfile" type="button" value="EditProfile" width="200px"></router-link>
        </div>
      </form> 

    </div>
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
        console.log('유저정보를 불러오기에 실패했습니다.')
        console.log(err)
      })
    },
    editProfile(){
      console.log('프로필 수정 요청중...')
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
  .layout_04 {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

  
</style>