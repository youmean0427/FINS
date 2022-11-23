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
  methods:{
    // 30개 영화씩 리스트로 보내주는 함수
    // 함수를 호출할 때마다 카운트 + 1
    // 표출하는용 리스트를 새로 쌓아 지금 있는 리스트 + 새로 만드는 리스트
    // 위로 올라가기 버튼이 있어야겠네
  }
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
