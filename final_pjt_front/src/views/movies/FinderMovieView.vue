
<template>
  <div style="margin-left: 20%; margin-right: 20%;">
    <img src="@/assets/Finder.png" alt="" width="150px">
    <hr>
    <h4 class="font_font">오른쪽은 좋아요, 왼쪽은 싫어요</h4>
  
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
.font_font {
         font-family: 'NanumGothic';
        font-style: normal;
        /* font-weight: 700; */
        font-size: 20px;
        /* line-height: 37px; */

        color: #000000;
    }
</style>