<template>
  <div>

    <!-- <h5>Write_user : {{ review.write_user }}</h5> -->
      <br>
      <h4>{{ review.content }}</h4>
      
      <br>
      <p> {{ review.created_at.slice(0, 10) }}</p>
    <div v-show='isAuth && loggedIn'>
      <div class="input-group" >

          <input @keyup.enter="editReview" v-show='isActive'  class="form-control" style="text-align:center; margin-right: 20%; margin-left: 20%; border:none" v-model.trim="inputData" type="text" name="">
          
        </div>
        <img src="@/assets/Line_00.png" alt=""  style="margin-right: 20%; margin-left: 20%;" v-show='isActive' width="60%" >

    <br>
    <img src="@/assets/Update.png" alt="" width="50px" height="20px" type="button" @click="createReviewInput" v-show='!isActive' >
    <img src="@/assets/Update.png" alt="" width="50px" height="20px" type="button" @click="editReview" v-show='isActive'>
    |
    <img src="@/assets/Delete.png" width="50px" height="20px" @click="deleteReview" type="button">

    </div>
    <hr>
    <!-- <p>{{ movie.title }}</p> -->


  </div>
</template>

<script>
export default {
    name: 'ReviewList',
    props: {
    review: Object,
    },

    data() {
        return {
        isActive:false,
        inputData:'',
        nowUser: this.$store.state.now_user_pk,
        isAuth: false,
        }
    },
    methods: {
      deleteReview() {
        this.$store.dispatch('delete_review', this.review.id)
        this.$router.go(this.$router.currentRoute)
      },

      createReviewInput() {
        this.isActive = true
        // console.log(this.isActive)
      },

      editReview() {
        const payload = {
          'reviewId' : this.review.id,
          'inputData' :  this.inputData
        }
        this.$store.dispatch('edit_review', payload)
      },
      getReview() {
        this.inputData = this.review.content
      },
    },
    created(){
        // console.log(this.nowUser, this.review.write_user)
        if (this.nowUser === this.review.write_user) {
          this.isAuth = true
        }  else {
          this.isAuth = false
        }
        this.getReview()
    },
    computed: {
      loggedIn(){
            return this.$store.getters.isLogin
      }
    }
    
 

}
</script>

<style>
 @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@800&display=swap');
    
* {
  font-family: 'Nanum Gothic', sans-serif;
}

#layout_01 {
    display: flex;
    flex-direction: row;

    justify-content: space-between;

    
}
</style>