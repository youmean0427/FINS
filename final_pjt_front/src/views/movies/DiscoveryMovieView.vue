<template>
  <div>
    <h1>DiscoveryMovieView</h1>
    <SearchBar/>
    <GenreCardList :genreList="genre" />

  </div>
</template>

<script>
import GenreCardList from '@/components/Movies/GenreCardList.vue';
import SearchBar from '@/components/Movies/SearchBar.vue';
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

// const API_KEY = '8d2390a7f14da4093a0836c65dfb59a2'

export default {
    name: "DiscoveryMovieView",
    components: {
      GenreCardList,
      SearchBar
    },
    data() {
        return {
             genre : null,
            // Array -> null


        };
    },


    methods: {
        getGenreList() {
            axios({
                method: "get",
                url: `${API_URL}/api/v1/discoverymovie/`
            })
                .then((res) => {
                console.log(res);
                console.log("데이터를 받았어요!");
                this.genre = res.data;
            })
                .catch((err) => {
                console.log("데이터를 받지 못했어요!");
                console.log(err);
            });
        },

       
    },
    created() {
        this.getGenreList();

        // search

   
    },
}
</script>

<style>

</style>