<template>
  <div>
    <h1>DiscoveryMovieView</h1>
    <GenreCardList/>
  </div>
</template>

<script>
import GenreCardList from '@/components/Movies/GenreCardList.vue';

export default {
    name: "DiscoveryMovieView",
    components: {
      GenreCardList
    }
}
</script>

<style>

</style>