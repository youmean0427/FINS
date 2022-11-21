<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">닉네임 : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="email"> 이메일 : </label>
      <input @keyup="isValidEmail" type="email" id="email" v-model="email">
      <p id="validEmail">{{validEmail}}</p><br>

      <label for="password1"> 비밀번호 : </label>
      <input @keyup="isValidPwd" type="password" id="password1" v-model="password1">
      <p id="validPwd">{{validPwd}}</p>
      <br>

      <label for="password2"> 비밀번호 확인 : </label>
      <input @keyup="isValidPwd2" type="password" id="password2" v-model="password2">
      <p id="validPwd2">{{validPwd2}}</p> <br>
      <input @click="signUp" type="button" value="SignUp">
    </form> 
  </div>
</template>

<script>
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
      const validEmailTag = document.querySelector('#validPwd')
      if (!this.password1){
        // alert('비밀번호를 입력하세요!')
        this.validPwd = '비밀번호를 입력하세요!'
        validEmailTag.style.color = 'red'
        return
      }
      if(!this.password2){
        this.validPwd = '비밀번호 확인이 필요합니다'
        document.querySelector('#validPwd2').style.color = 'red'
        return
      }
      if (this.email_pwd_distance < 5) {
        this.validPwd = '이메일과 비밀번호가 유사합니다'
        validEmailTag.style.color = 'red'
        // alert('이메일과 비밀번호가 유사합니다')
        return
      }
      else if (this.name_pwd_distance < 5){
        this.validPwd = '이름과 비밀번호가 유사합니다'
        validEmailTag.style.color = 'red'
        // alert('이름과 비밀번호가 유사합니다')
        return
      }
      else if (!this.is_valid_e){
        document.querySelector('#validEmail').style.color = 'red'
        this.validEmail = '유효한 이메일을 입력하세요!'
        // alert('유효한 이메일을 입력하세요!')
        return
      }
      else if (!this.is_valid_pwd2 || !this.is_valid_pwd){
        this.validPwd = '유효한 비밀번호를 입력하세요!'
        validEmailTag.style.color = 'red'
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

    }
  }
}
</script>
