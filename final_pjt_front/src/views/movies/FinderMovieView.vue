
<template>
  <div class="finderheader">
    <img src="@/assets/Finder.png" alt="" width="150px">
    <hr>
    <div class="iconbox">
      <div class="font_font"> <span>⬅ </span>
          <img src="https://user-images.githubusercontent.com/87971876/203677620-815c452a-e650-4980-843a-bdc7865bf159.png" alt="">  
      </div> 
      <div class="font_font">
        <img :src='require(`@/assets/Love.png`)' alt="">  <span>➡ </span> 
      </div>

    </div>
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
.font_font img{
  max-width: 100px;
}
.font_font span{
  max-width: 50px;
}
.iconbox{
    display: flex;
    justify-content: space-between;
    position: absolute;
    width: 50%;
    top: 50%;
    z-index: 0;
    left: 38%;
}

</style>