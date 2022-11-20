<template>
  <div>
    <h1>GenreCardList</h1>
    <GenreCard
      v-for="genre in genreList"
      :key="genre.id"
      :genre="genre"       
    />
  </div>
</template>

<script>

import GenreCard from '@/components/Movies/GenreCard.vue'

export default {
    name: "GenreCardList",
    components: {
        GenreCard
    },
    props: {
      genreList: Array
    }
}
</script>

<style>

</style>