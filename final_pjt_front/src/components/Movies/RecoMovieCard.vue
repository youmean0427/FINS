<template>
  <div>
    <!-- Keyword에 맞는 영화 페이지 -->
    
    <router-link :to="{ name: 'KeywordMovieView', params: { id: keyword.id } }">
      {{ keyword.keyword }}
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'RecoMovieCard',
  props: {
    keyword: Object,
  }
}


</script>

<style>

</style>