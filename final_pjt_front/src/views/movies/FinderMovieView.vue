
<template>
  <div class="finderheader">
    <img src="@/assets/Finder.png" alt="" width="150px">
    <hr>
    <h4 class="font_font">⬅ 🙅‍♀️  ❤ ➡ </h4>
  
    <FinderMovie/>
  </div>
</template>

<script>
import FinderMovie from "@/components/Movies/FinderMovie.vue"
export default {
  name: 'FinderMovieView',
  components: {
    FinderMovie
  },
  created() {

  }
}
</script>

<style>
.finderheader{
  margin: 50px 0 0 0;
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