<template>
  <div>
    
    <!-- Keyword에 맞는 영화 페이지 -->
    <button type="button" class="btn btn-outline-secondary custom upper font_font">
        <router-link :to="{ name: 'KeywordMovieView', params: { id: keyword.id } }" :keyword_name="keyword.keyword" >
        {{ keyword.keyword }}
          <!-- {{ keyarr }} -->
        </router-link>
    </button>

    <!-- <KeywordMovieView/> -->
    <br>
    <br>
  </div>
</template>

<script>
// import KeywordMovieView from '@/components/Movies/KeywordMovieView'
export default {
  name: 'RecoMovieCard',
  data() {
    return {

    }
  },
  components: {
    // KeywordMovieView
  },
  props: {
    keyword: Object,
  },

  created() {
    
  },
}


</script>

<style>

.custom {
    width: 250px !important;
 
}

.upper{
    text-transform : uppercase;
}

.font_font {
         font-family: 'NanumGothic';
        font-style: normal;
        /* font-weight: 700; */
        font-size: 20px;
        /* line-height: 37px; */

        color: #000000;
    }
</style>