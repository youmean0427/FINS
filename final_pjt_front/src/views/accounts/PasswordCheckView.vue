<template>
  <div>
  <h1>비밀번호 확인</h1>
    <form @submit.prevent="checkPassword">
      <label for="password"> 비밀번호 : </label>
      <input type="password" id="password" v-model="password"><br>
      <input type="submit" value="checkPassword">
    </form>
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

</style>