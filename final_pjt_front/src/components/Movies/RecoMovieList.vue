<template>
  <div>
    <h1>RecoMovieCard</h1>
    <RecoMovieCard
      v-for="keyword in movieKeyword"
      :key="keyword.id"
      :keyword="keyword"
    />
    {{keyarr}}

  </div>
</template>

<script>
import RecoMovieCard from '@/components/Movies/RecoMovieCard.vue';
export default {
    name: "RecoMovieList",
     data() {
        return {
          keyarr :[],
          eachkeyword: ''
      }
    },
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
    },
    created() {

      for (const i of (this.movieKeyword) ) {
        this.keyarr.push(i)
      }
    }

}
</script>

<style>

</style>