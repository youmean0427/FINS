<template>
  <div>
    <h1>RecoMovieList</h1>
    <RecoMovieCard
      v-for="keyword in movieKeyword"
      :key="keyword.id"
      :keyword="keyword"
    />
  </div>
</template>

<script>
import RecoMovieCard from '@/components/Movies/RecoMovieCard.vue';
export default {
    name: "RecoMovieList",
    components: {
      RecoMovieCard
    },

    props: {
      movieKeyword:Array
    },

    computed: {
    keywordMovieList() {
      return this.$store.state.movies
    }
  }

}
</script>

<style>

</style>