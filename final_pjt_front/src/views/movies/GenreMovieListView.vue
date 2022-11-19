<template>  
    <div>
        <h1>GenreMovieListView</h1>
        <GenreMovieCard/>
    </div>  
</template>

<script>
import GenreMovieCard from "@/components/Movies/GenreMovieCard.vue/"

export default {
    name: 'GenreMovieListView',
    components: {
        GenreMovieCard
    }
}
</script>

<style>

</style>