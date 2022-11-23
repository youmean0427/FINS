<template>
    <div>
        
        <br>
        <ReviewItem
            v-for="review in movieReviewSet"
            :key="review.id"
            :review = "review"
        />
        <br>
        <br>
    </div>
</template>

<script>
    import ReviewItem from '@/components/Movies/ReviewItem'

    export default {
    name: 'ReviewList',
    components: {
        ReviewItem,
    },
    computed: {
        // reviewList() {
            // return this.$store.state.movies
        // }
    },
    props: {
        movieReviewSet : Array
    }
    }
</script>

<style>
.movie-list {
text-align: start;
}
</style>
