<template>
  <div>
    <h1>KeywordMovieCard</h1>
    {{keyword_movie.title}}
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