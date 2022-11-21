<template>
  <div>
    <h1>KeywordMovieCard</h1>
    <router-link :to="{ name: 'MovieDetailView', params: { id: keyword_movie.id } }">
      [DETAIL]
    </router-link>
    <p>{{keyword_movie.title}}</p>
    <img :src="keyword_movie.stil_image" alt="">
    
    <hr>
  </div>
</template>

<script>
export default {
    name: "KeywordMovieCard",
    props: {
        keyword_movie:Object
    }
}
</script>

<style>

</style>