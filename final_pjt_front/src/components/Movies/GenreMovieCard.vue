<template>
  <div>
    <h5>GenreMovieCard</h5>
    <router-link :to="{ name: 'MovieDetailView', params: { id: genre_movie.id } }">
    [DETAIL]</router-link>
    {{genre_movie.title}}

    <!-- 데이터에 스틸컷이나 포스터 정보가  없음 -->
    {{genre_movie}}
    <!-- {{genre_movie.stil_image}} -->
  </div>
</template>

<script>
export default {
    name: "GenreMovieCard",

    props: {
      genre_movie: Object
    }
}
</script>

<style>

</style>