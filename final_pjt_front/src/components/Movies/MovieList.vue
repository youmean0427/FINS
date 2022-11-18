<template>
  <div class="">
    <h3>Movie List</h3>
    <MovieCard
      v-for="movie in movieList"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieCard from '@/components/Movies/MovieCard'

export default {
  name: 'MovieList',
  components: {
    MovieCard,
  },
  computed: {
    movieList() {
      return this.$store.state.movies
    }
  }
}
</script>

<style>
.movie-list {
  text-align: start;
}
</style>
