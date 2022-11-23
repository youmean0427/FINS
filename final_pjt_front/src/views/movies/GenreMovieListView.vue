<template>  
    <div class="genreMovieFrame">
        <MovieCard
            v-for="genre_movie in genre_movie"
            :key="genre_movie.id"
            :movie="genre_movie"

        />
    </div>  
</template>

<script>
import MovieCard from "@/components/Movies/MovieCard.vue/"
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'GenreMovieListView',
    components: {
        MovieCard
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
        justify-content: center;
        flex-flow: row wrap;
        padding: 1rem;
        height: 100%;
    }
</style>