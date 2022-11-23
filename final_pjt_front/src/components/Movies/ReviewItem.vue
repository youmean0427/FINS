<template>
  <div>

    <!-- <h5>Write_user : {{ review.write_user }}</h5> -->
    <h5 class="font_font">{{ review.content }}</h5>
    <h5 class="font_font"> {{ review.created_at }}</h5>

    <div v-show='isAuth && loggedIn'>
    <input v-show='isActive' v-model="inputData" type="text" name="">
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
        nowUser: this.$store.state.now_user_id,
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
.font_font {
         font-family: 'NanumGothic';
        font-style: normal;
        /* font-weight: 700; */
        font-size: 15px;
        /* line-height: 37px; */

        color: #000000;
    }
</style>