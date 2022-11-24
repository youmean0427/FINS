<template>
  <div>

    <div id="layout_03">
        <div>
        <form @submit.prevent="logIn">
          <div style="position: relative;">
            <div style="z-index: 2;  position: absolute;">
              <img v-if="username" src="@/assets/Line_02.png" alt="" width="300px">
            </div>
            <div style="z-index: 1;">
              <img src="@/assets/ID.png" alt="" width="125px" >
            </div>
          </div>
          <br>
          <div class="input-group" >
           <input type="text" id="username" style="text-align:center; border:none; width:300px;" class="form-control"  v-model="username" ><br>
          </div>
             <img src="@/assets/Line_00.png" alt="" width="300px" >
          <br>
             <div style="position: relative;">
                <div style="z-index: 2;  position: absolute;">
                <img v-if="password" src="@/assets/Line_01.png" alt="" width="300px">
                </div>
                <div style="z-index: 1;">
                <img src="@/assets/PASSWORD.png" alt="" width="250px">
                </div>
              </div>
          <br>

          <div class="input-group" >
          <input type="password" id="password"  @keyup.enter="logIn" style="text-align:center; border:none; width:300px;" class="form-control" v-model="password"><br>
          </div>
           <img src="@/assets/Line_00.png" alt="" width="300px" >
          <p style="color:red">{{alert}}</p>
          <img @click="logIn" src="@/assets/Login_page.png" class = 'login_h' width="150px">
   
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

  .login_h:hover{
transform: scale(1.2);
transition: 0.5s ease;
}

</style>