<template>
  <div>

    <div id="layout_03">
        <div>
        <form @submit.prevent="logIn">
          <div style="position: relative;">
            <div style="z-index: 2;  position: absolute;">
              <img src="@/assets/Line_01.png" alt="" width="300px">
            </div>
            <div style="z-index: 1;">
              <img src="@/assets/ID.png" alt="" width="125px" >
            </div>
          </div>
          <br>
          <div class="input-group" >
           <input type="text" id="username" style="text-align:center;" class="form-control"  v-model="username" ><br>
          </div>
          <br>
             <div style="position: relative;">
                <div style="z-index: 2;  position: absolute;">
                <img src="@/assets/Line_01.png" alt="" width="300px">
                </div>
                <div style="z-index: 1;">
                <img src="@/assets/PASSWORD.png" alt="" width="250px">
                </div>
              </div>
          <br>

          <div class="input-group" >
          <input type="password" id="password" style="text-align:center;" class="form-control" v-model="password"><br>
          </div>
          <p style="color:red">{{alert}}</p>
          <input type="submit" value="logIn">
        </form>
        </div>


        
    </div>
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


<style>
  #layout_03 {
    height: 100vh;

        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>