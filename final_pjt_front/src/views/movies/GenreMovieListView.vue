<template>  
    <div>
        <h1>GenreMovieListView</h1>
        <GenreMovieCard
            v-for="genre_movie in genre_movie"
            :key="genre_movie.id"
            :genre_movie="genre_movie"

        />
    </div>  
</template>

<script>
import GenreMovieCard from "@/components/Movies/GenreMovieCard.vue/"
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'GenreMovieListView',
    components: {
        GenreMovieCard
    },
    data() {
        return {
            genre_movie: null
        };
    },
    methods: {
        getGenreMovieList() {
                axios({
                    method: "get",
                    url: `${API_URL}/api/v1/discoverymovie/${this.$route.params.id}`
                })
                    .then((res) => {
                    console.log(res);
                    console.log("데이터를 받았어요!");
                    this.genre_movie = res.data;
                })
                    .catch((err) => {
                    console.log("데이터를 받지 못했어요!");
                    console.log(err);
                });
            },
    },
    created() {
        this.getGenreMovieList()
    },
}
</script>

<style>

</style>