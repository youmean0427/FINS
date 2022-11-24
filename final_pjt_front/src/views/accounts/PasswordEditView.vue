<template>
  <div>
    <div id="layout_03">
    <form @submit.prevent="changePwd">
      
      <img src="@/assets/New_password.png" alt="" width="300px">
      <br>

      <div class="input-group">
        <input @keyup="isValidPwd" type="password" id="password1" 
        style="text-align:center; border:none; width: 100%;"  class="form-control"
        v-model="password1">
      </div>
      
      <img src="@/assets/Line_00.png" alt="" width="300px">

      <br>
      <br>
      <p id="validPwd">{{validPwd}}</p>
      <br>

      <img src="@/assets/change_password.png" alt="" width="300px">
      <br>
      <div class="input-group" >
           <input @keyup="isValidPwd2" type="password" id="password2" style="text-align:center; border:none; width: 100%;" v-model="password2"
           class="form-control" >
      </div>

      <img src="@/assets/Line_00.png" alt="" width="300px">
      <br>
      <br>
      <p id="validPwd2">{{validPwd2}}</p> 
      
      <br>
      <img src="@/assets/Edit_button.png" @click="changePwd" type="button" width="40%">
    </form>
  </div>
  </div>
</template>

<script>
export default {
  name : "PasswordEditView",
  data(){
    return{
      password1: null,
      password2: null,
      validPwd : '숫자와 문자를 포함하여 8자리 이상 작성해주세요',
      is_valid_pwd : false,
      validPwd2: '',
      is_valid_pwd2 : false,
    }
  },
  methods:{
    isValidPwd(){
      this.is_valid_pwd = false
      if (! this.password1){
        return
      } else if (this.password1 && this.password1.length < 8){
        this.validPwd = '8자리 이상 입력해주세요!'
      } else if (this.password1 && !/[0-9]/.test(this.password1)){
        this.validPwd = '숫자를 포함하여 입력해주세요!'
      } else if (this.password1 &&!/[A-Za-z]/.test(this.password1)){
        this.validPwd = '문자를 포함하여 입력해주세요!'
      } else {
        this.validPwd = ''
        this.is_valid_pwd = true
      }
    },
    isValidPwd2(){
      console.log(this.password1 == this.password2)
      if(!this.password1){ return }
      else if (!this.password2){ return } 
      else if (! (this.password1 == this.password2)){
        this.validPwd2 = '비밀번호가 다릅니다'
      } else {
        this.validPwd2 = ''
        this.is_valid_pwd2 = true
      }
    },
    changePwd(){
      if(this.is_valid_pwd2 === false){
        alert('비밀번호가 다릅니다!')
        return
      } else {
        const new_password1 = this.password1
        const new_password2 = this.password2
        const payload = {
          new_password1,
          new_password2,
        }
        this.$store.dispatch('changePwd', payload)
      }

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