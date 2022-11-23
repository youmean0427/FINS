<template>
  <div class="movieCardFrame">
    <MovieCard
       data-aos="fade-right"
      v-for="movie in movieList"
      :key="movie.id"
      :movie="movie"
    />
    <b-button>더보기</b-button>
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
  },
}
</script>

<style>
  .movie-list {
    text-align: start;
  }
  .movieCardFrame{
    display: flex;
    justify-content: center;
    flex-flow: row wrap;
    padding: 1rem;
    height: 100%;  
  }   
</style>
