<template>
  <div>

    <h5>Write_user : {{ review.write_user }}</h5>
    <h5>Content : {{ review.content }}</h5>
    <h5>Created_at : {{ review.created_at }}</h5>
    <hr>
    <!-- <p>{{ movie.title }}</p> -->


  </div>
</template>

<script>
export default {
    name: 'ReviewList',
    props: {
    review: Object,
<<<<<<< HEAD
  }
=======
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
      }
    },
    created(){
      // console.log(this.nowUser, this.review.write_user)
      if (this.nowUser === this.review.write_user) {
        this.isAuth = true
      }  else {
        this.isAuth = false
      }
      this.getReview()
    }
 
>>>>>>> Search_Problem
}
</script>

<style>

</style>