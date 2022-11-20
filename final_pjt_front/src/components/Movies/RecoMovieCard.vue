<template>
  <div>
    <!-- Keyword에 맞는 영화 페이지 -->
    <!-- Router로 KeywordMovieView로 떠납시다. params keyword_id -->
    <button>Keyword</button>{{ keyword }}
  </div>
</template>

<script>
export default {
  name: 'RecoMovieCard',
  props: {
    keyword: Object,
  }
}

// Back에서 Keyword 받아오는 url 만들면 시작
</script>

<style>

</style>