<template>
  <div>
    <h5>{{ movie.id }}</h5>
    <p>{{ movie.title }}</p>
    <img :src="poster" style="width:300px;">
  </div>
</template>

<script>
export default {
    name: 'FeedCard',
    props:{
      movie : Object
    },
    computed:{
      poster(){
        return this.movie.stil_image
      }
    }
}
</script>

<style>

</style>