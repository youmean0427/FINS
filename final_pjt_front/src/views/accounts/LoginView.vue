<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username"> 닉네임 : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> 비밀번호 : </label>
      <input type="password" id="password" v-model="password"><br>
      <p style="color:red">{{alert}}</p>
      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      alert : '',
    }
  },
  created(){
    this.is_valid_username()
  },
  methods: {
    is_valid_username(){
      if (!this.username) { return false }
      else{
        return this.$store.dispatch('is_user', this.username)
      }
    },
    logIn() {
      
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
            this.$store.dispatch('logIn', payload)
          } else {
            this.alert = '존재하지 않는 회원입니다'
          }
        })
        .catch(() => {return false})
    }
  }
}
</script>
