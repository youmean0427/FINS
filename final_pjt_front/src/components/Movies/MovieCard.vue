<template>
  <div>

    <h5>{{ movie.id }}</h5>
    <p>{{ movie.title }}</p>

    <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
      [DETAIL]
    </router-link>
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
