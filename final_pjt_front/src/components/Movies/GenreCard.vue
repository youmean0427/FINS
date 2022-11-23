<template>
  <div @click="moveToGenreList" class="col-md-4 mb-2">
    <p class="btn btn-rounded btn-lg btn-block">{{ genre.genre_name }}</p>
  </div>
</template>

<script>

export default {
    name: 'GenreCard',
    props: {
      genre: Object
    },
    methods:{
      moveToGenreList(){
        this.$router.push({ name: 'GenreMovieListView', params: { id: this.genre.id } })
      }
    }
}
</script>

<style>
  .gencard{
    text-align: center;
    height: auto;
    border: 1px groove rgb(31, 31, 31);
    border-radius: 50px;
    margin: 2px 10px 2px 10px;
    font-size: 0.8em;
    color:rgba(46, 106, 124, 0.61);
    font-weight: bold;
  }
  .gencard:hover{
    /* background-color: rgba(88, 88, 88, 0.61); */
    /* color: white; */
    transition-delay: 0.3 ease;
  }
</style>