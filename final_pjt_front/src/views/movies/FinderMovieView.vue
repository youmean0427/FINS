
<template>
  <div style="margin-left: 20%; margin-right: 20%;">
    <img src="@/assets/Finder.png" alt="" width="150px">
    <hr>
    <h4>오른쪽은 좋아요, 왼쪽은 싫어요</h4>
  
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

 @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@800&display=swap');
    
* {
  font-family: 'Nanum Gothic', sans-serif;
  color: black;
}
</style>