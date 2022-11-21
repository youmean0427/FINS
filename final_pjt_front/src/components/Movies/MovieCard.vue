<template>
  <div>

    <h5>{{ movie.id }}</h5>
    <p>{{ movie.title }}</p>
    <p>
      <img :src="movie.stil_image" style="width:300px;">
    </p>

    <p>
      <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
        [DETAIL]
      </router-link>
    </p>
    
    <hr>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>
