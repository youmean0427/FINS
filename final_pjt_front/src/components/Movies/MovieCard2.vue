<template>
  <div>

    <h5>{{ movie.title }}</h5>
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
  name: 'MovieCard2',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>
