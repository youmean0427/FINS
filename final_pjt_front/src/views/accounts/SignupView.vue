<template>
  <div>
    <div id="layout_03">
      <form @submit.prevent="signUp">
        <div style="z-index: 2;  position: absolute;">
              
              <img v-if="username" src="@/assets/Line_01.png" alt="" width="300px">
              </div>
              <div style="z-index: 1;">
                <img src="@/assets/ID.png" alt="" width="125px" >
        </div>
        <br>
        <div class="input-group" >
        <input type="text" id="username" v-model="username" style="text-align:center; border:none; width:300px" class="form-control"><br>
        </div>
         <img src="@/assets/Line_00.png" alt="" width="300px" >
        <br>
        <br>
        <div style="position: relative;">
              <div style="z-index: 2;  position: absolute;">
                <img v-if="!validEmail && email" src="@/assets/Line_02.png" alt="" width="300px">
                </div>
                <div style="z-index: 1;">
                <img src="@/assets/Email.png" alt="" width="250px">
              </div>
        </div>
        <br>
        <div class="input-group" >
        <input @keyup="isValidEmail" type="email" id="email" v-model="email" style="text-align:center; border:none; width:300px" class="form-control">
        </div>
          <img src="@/assets/Line_00.png" alt="" width="300px" >
        <br>
        <p id="validEmail">{{validEmail}}</p><br>


        <div style="position: relative;">
                <div style="z-index: 2;  position: absolute;">
                <img v-if="!validPwd" src="@/assets/Line_01.png" alt="" width="300px">
                </div>
                <div style="z-index: 1;">
                <img src="@/assets/PASSWORD.png" alt="" width="250px">
                </div>
        </div>
        <br>
        <div class="input-group" >
        <input @keyup="isValidPwd" type="password" id="password1" v-model="password1" style="text-align:center; border:none; width:300px" class="form-control">
        </div>
        <img src="@/assets/Line_00.png" alt="" width="300px" >

        <br>
        <p id="validPwd">{{validPwd}}</p>
        <br>

        <div style="position: relative;">
              <div style="z-index: 2;  position: absolute;">
                <img v-if="!validPwd2 && password2" src="@/assets/Line_02.png" alt="" width="300px">
                </div>
                <div style="z-index: 1;">
                <img src="@/assets/PASSWORD_check.png" alt="" width="250px">
              </div>
        </div>
        <br>
        <div class="input-group" >
        <input @keyup="isValidPwd2" type="password" id="password2" v-model="password2" style="text-align:center; border:none; width:300px" class="form-control">
        </div>
        <img src="@/assets/Line_00.png" alt="" width="300px" >
        
        <br>

        <p id="validPwd2">{{validPwd2}}</p> <br>
        <img src="@/assets/Signup_page.png" @click="signUp" class='signup_h' type="button" width="200px">
      </form> 
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'SignUpView',
  data() {
    return {
      username: '',
      password1: '',
      password2: '',
      email : '',
      validEmail :'',
      is_valid_e : false,
      validPwd : '숫자와 문자를 포함하여 8자리 이상 작성해주세요',
      is_valid_pwd : false,
      validPwd2: '',
      is_valid_pwd2 : false,
      name_pwd_distance : 0,
      email_pwd_distance : 0,


    }
  },
  computed:{
    linIdx(){
      return this.email.indexOf('@')
    },
    addr(){
      return this.email.slice(this.linIdx)
    },
  },
  methods: {
    // 비밀번호와 아디디, 이메일이 유사하면 400에러남
    // 유사도 판별을 위해 node.js라이브러리 사용
    // npm install fast-levenshtein
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
    isValidPwd(){
      if (!this.password1){
        this.is_valid_pwd = false
        return
      } else if (this.password1 && this.password1.length < 8){
        this.validPwd = '8자리 이상 입력해주세요!'
        this.is_valid_pwd = false
      } else if (this.password1 && !/[0-9]/.test(this.password1)){
        this.validPwd = '숫자를 포함하여 입력해주세요!'
        this.is_valid_pwd = false
      } else if (this.password1 &&!/[A-Za-z]/.test(this.password1)){
        this.validPwd = '문자를 포함하여 입력해주세요!'
        this.is_valid_pwd = false
      } else {
        this.validPwd = ''
        this.is_valid_pwd = true
      }
    },
    isValidPwd2(){
      console.log(this.password1 == this.password2)
      if(!this.password1){ return }
      else if (!this.password2){ 
        this.is_valid_pwd2 = false
        return 
      } 
      else if (! (this.password1 == this.password2)){
        this.validPwd2 =  '비밀번호가 다릅니다'
        this.is_valid_pwd2 = false
      } else {
        this.validPwd2 = ''
        this.is_valid_pwd2 = true
      }
    },
    similiarInfo(){
      const levenshtein = require('fast-levenshtein')
      this.name_pwd_distance = levenshtein.get(this.username, this.password1)
      console.log('name_pwd_distance', this.name_pwd_distance)
      const emailId = this.email.slice(0,this.linIdx)
      this.email_pwd_distance = levenshtein.get(emailId, this.password1)
      console.log('email_pwd_distance', this.email_pwd_distance)
    },
    signUp() {
      this.similiarInfo()
      if (!this.password1){
        // alert('비밀번호를 입력하세요!')
        this.validPwd = '비밀번호를 입력하세요!'
        return
      }
      if(!this.password2){
        this.validPwd = '비밀번호 확인이 필요합니다'
        return
      }
      if (this.email_pwd_distance < 5) {
        this.validPwd = '이메일과 비밀번호가 유사합니다'
        // alert('이메일과 비밀번호가 유사합니다')
        return
      }
      else if (this.name_pwd_distance < 5){
        this.validPwd = '이름과 비밀번호가 유사합니다'
        // alert('이름과 비밀번호가 유사합니다')
        return
      }
      else if (!this.is_valid_e){
        this.validEmail = '유효한 이메일을 입력하세요!'
        // alert('유효한 이메일을 입력하세요!')
        return
      }
      else if (!this.is_valid_pwd2 || !this.is_valid_pwd){
        this.validPwd = '유효한 비밀번호를 입력하세요!'
        // alert('유효한 비밀번호를 입력하세요!')
        return
      }
      else{
        const username = this.username
        const email = this.email
        const password1 = this.password1
        const password2 = this.password2
  
        const payload = {
          // username,
          // password1,
          // password2,
          username: username,
          email : email,
          password1: password1,
          password2: password2,
        }
        console.log(payload)
        this.$store.dispatch('signUp', payload)
      }

    },

    // __________ Actor ____________
    getActor(){
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
        
      })
      .catch((err) => {
        console.log('유저정보를 불러오기에 실패했습니다.')
        console.log(err)
      })
    },
  }
}
</script>

<style>

.signup_h:hover{
transform: scale(1.2);
transition: 0.5s ease;
}


</style>