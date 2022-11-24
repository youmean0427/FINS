<template>
  <div>
    <div id="layout_03">
      <form @submit.prevent="checkPassword">
        <img src="@/assets/current_password.png" alt="" width="300px">
        
        <div class="input-group" >
        <input type="password" id="password" v-model="password" style="text-align:center; border:none; width:300px;" class="form-control"><br>
        </div> 
        
        <img src="@/assets/Line_00.png" alt="" width="300px" >
        <div>
        <img src="@/assets/Edit_button.png" type="submit" value="checkPassword" width="150px">
      </div>
      </form>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PasswordCheckView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  created(){
    this.getUser()
  },
  methods:{
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
        this.username = res.data.username
      })
      .catch((err) => {
        console.log('유저정보를 불러오기에 실패했습니다.')
        console.log(err)
      })
    },
    checkPassword(){
      if (!this.password){
        alert('비밀번호를 입력하세요')
        return
      }
      axios({
        method: 'get',
        url: `${API_URL}/user/isuser/${this.username}`,
      })
        .then((res) => {
          console.log('회원테이블에 존재하는 닉네임인가요?',res.data.isUser)
          // 회원테이블에 존재하는 닉네임인지?
          if (res.data.isUser === true){
            this.alert = ''
            const username = this.username
            const password = this.password
      
            const payload = {
              username: username,
              password: password,
            }
            console.log(payload)
            axios({
              method: 'post',
              url: `${API_URL}/accounts/login/`,
              data: {
                username: payload.username,
                password: payload.password,
              }
            })
              .then((res) => {
                console.log(res)
                this.$router.push({ name: 'PasswordEditView' })
              })
              .catch((err)=>{
                console.log('왜 로그인이 안되죠?', err)
                alert('비밀번호가 일치하지 않습니다!')
                this.password = ''
              })
            } else {
              this.alert = '비밀번호가 일치하지 않습니다.'
              this.password = ''
            }
          })
        .catch(() => {return false})
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

    #layout_03 {
    height: 100vh;

        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>