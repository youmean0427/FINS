<template>
  <div>
     <div class="row cardbody ">
      <GenreCard
        v-for="genre in genreList"
        :key="genre.id"
        :genre="genre"       
      />
      </div>
    </div>
</template>

<script>

import GenreCard from '@/components/Movies/GenreCard.vue'

export default {
    name: "GenreCardList",
    components: {
        GenreCard
    },
    props: {
      genreList: Array
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
</style>