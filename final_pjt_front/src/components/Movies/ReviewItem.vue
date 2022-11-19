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
  }
}
</script>

<style>

</style>