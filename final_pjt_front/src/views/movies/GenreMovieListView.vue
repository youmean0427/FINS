<template>  
    <div class="genreMovieFrame">
        <GenreMovieCard
            v-for="genre_movie in genre_movie"
            :key="genre_movie.id"
            :movie="genre_movie"
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
    computed:{
        gid(){
            return this.genreId.id
        }
    },
    props:{
        genreId:Object,
    },
    methods: {
        getGenreMovieList(g_id) {
            axios({
                method: "get",
                url: `${API_URL}/api/v1/discoverymovie/${g_id}`
            })
                .then((res) => {
                console.log(res);
                this.genre_movie = res.data;
            })
                .catch((err) => {
                console.log(err);
            });
        },
    },
    created() {
        this.getGenreMovieList(this.gid)
    },
    watch: {
        gid(val) {
            console.log(val, 'aa')
            this.getGenreMovieList(val)
        }
    }
}
</script>

<style>
    .genreMovieFrame{
        display: flex;
        justify-content: space-around;
        flex-flow: row wrap;
        height: 100%;
        width: 100%;
    }
</style>