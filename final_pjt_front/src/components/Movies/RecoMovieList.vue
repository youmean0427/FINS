<template>
  <div>
    <h1>RecoMovieCard</h1>
    <RecoMovieCard
      v-for="keyword in movieKeyword"
      :key="keyword.id"
      :keyword="keyword"
    />
    <hr>
    <!-- {{ movieKeyword }} -->
  

  </div>
</template>

<script>
import RecoMovieCard from '@/components/Movies/RecoMovieCard.vue';
export default {
    name: "RecoMovieList",
     data() {
        return {
          keyarr :[],
          eachkeyword: '',
          keyarr_result: [],
          top : []
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
    methods: {
    },

    created() {

    }

}
</script>

<style>

</style>