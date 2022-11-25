<template>
  <div>
    <img src="@/assets/Recommend.png" alt="" width="150px">
    <div >
      <div id="row">
        <div class="recobox">
        <RecoMovieCard  class="col-4"
          v-for="keyword in movieKeyword.keyword"
          :key="keyword.id"
          :keyword="keyword"
        />
        </div>
      </div>
    </div>
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
      movieKeyword:Object
    },

    computed: {
    keywordMovieList() {
      return this.$store.state.movies
      }
    },
    methods: {
    },

    created() {
   
    },
  


}
</script>

<style>
 .recobox{
   display: flex;
   flex-wrap: wrap;
 }
</style>