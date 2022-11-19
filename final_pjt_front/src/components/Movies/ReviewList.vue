<template>
    <div class="">
        <h3>Review List</h3>
        <ReviewItem
            v-for="review in movieReviewSet"
            :key="review.id"
            :review = "review"
        />
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
