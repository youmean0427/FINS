<template>
  <div>
    <!-- Keyword에 맞는 영화 페이지 -->

    <router-link :to="{ name: 'KeywordMovieView', params: { id: keyword.id } }">
      {{ keyword.keyword }}
      {{ keyarr }}
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'RecoMovieCard',
  data() {
    return {

    }
  },
  props: {
    keyword: Object,
  },

  created() {
    
  },
}


</script>

<style>

</style>