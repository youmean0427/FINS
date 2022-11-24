<template>
  <div>
     <div class="row cardbody" >
        
        <input type="radio" class="btn-check" name="genre" id="0" @click="checkSelected(0)" v-model="picked"  value="0" autocomplete="off" >
        <label class="btn btn-outline-dark" for="0">액션</label>

        <input type="radio" class="btn-check " name="genre" id="1" @click="checkSelected(1)" v-model="picked" value="1" autocomplete="off" />
        <label class="btn btn-outline-dark" for="1">모험</label>

        <input type="radio" class="btn-check " name="genre" id="2" @click="checkSelected(2)" v-model="picked" value="2" autocomplete="off" />
        <label class="btn btn-outline-dark" for="2">애니메이션</label>

        <input type="radio" class="btn-check" name="genre" id="3" @click="checkSelected(3)" v-model="picked" value="3" autocomplete="off" />
        <label class="btn btn-outline-dark" for="3">코미디</label>

        <input type="radio" class="btn-check" name="genre" id="4" @click="checkSelected(4)" v-model="picked" value="4" autocomplete="off" />
        <label class="btn btn-outline-dark" for="4">범죄</label>

        <input type="radio" class="btn-check" name="genre" id="5" @click="checkSelected(5)" v-model="picked" value="5" autocomplete="off" />
        <label class="btn btn-outline-dark" for="5">다큐멘터리</label>

        <input type="radio" class="btn-check" name="genre" id="6" @click="checkSelected(6)" v-model="picked" value="6" autocomplete="off" />
        <label class="btn btn-outline-dark" for="6">드라마</label>

        <input type="radio" class="btn-check" name="genre" id="8" @click="checkSelected(8)" v-model="picked" value="8" autocomplete="off" />
        <label class="btn btn-outline-dark" for="8">판타지</label>

        <input type="radio" class="btn-check" name="genre" id="14" @click="checkSelected(14)" v-model="picked" value="14" autocomplete="off" />
        <label class="btn btn-outline-dark" for="14">SF</label>
        
        <input type="radio" class="btn-check" name="genre" id="13" @click="checkSelected(13)" v-model="picked" value="13" autocomplete="off" />
        <label class="btn btn-outline-dark" for="13">로맨스</label>
      <!-- <GenreCard
        v-for="genre in genreList"
        :key="genre.id"
        :genre="genre"       
      /> -->
      </div>
      <button @click="resetActive" type="button" class="btn btn-link btn-rounded" style="color: #939597;" data-mdb-ripple-color="dark">
        선택초기화
      </button>
    </div>
</template>

<script>
export default {
    name: "GenreCardList",
    data(){
      return{
        picked: ''
      }
    },
    props: {
      genreList: Array
    },
    methods:{
      checkSelected(id){
        this.$emit('selectedGenre', id)
      },
      resetActive(){
        // 쿼리셀렉터안쓰고해결함
        //@click="checkSelected(2)" v-model="picked" value="2"
        this.picked = ''
      }
    }
}
</script>

<style> 
 .cardbody{
  display: flex;
  justify-content: center;
  flex-flow: row wrap;
  padding: 1rem;
  height: 100%;  
 }
 .btn-group{
  display: row;
  flex-direction: row wrap;
 }
 .btn-group {
  font-size: 0.8em;
 }
 .cardbody > *{
    width: 50% !important;
 }

</style>