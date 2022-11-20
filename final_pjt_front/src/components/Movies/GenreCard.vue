<template>
  <div>
    <h5>GenreCard</h5>
    <!-- params 작성하세요 -->
    <!-- <router-link :to="{ name: 'GenreMovieListView' }">
      [Genre]
    </router-link> -->
    <router-link :to="{ name: 'GenreMovieListView', params: { id: genre.id } }">
      {{ genre.id}}
      {{ genre.genre_name }}
    </router-link>
    



    <hr>


  </div>
</template>

<script>

export default {
    name: 'GenreCard',
    props: {
      genre: Object
    }
}
</script>

<style>

</style>