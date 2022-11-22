<template>
  <div>
    <FeedCard
      v-for="feed in likeMovies"
      :key="feed.id"
      :feed="feed"
      @showFeed="feedDetail(feed.id)"
    />
  </div>
</template>

<script>
import FeedCard from '@/components/Accounts/FeedCard.vue'

export default {
    name: 'FeedList',
    components: {
        FeedCard

    },
    props:{
      likeMovies : Array
    },
     methods: {
      feedDetail(id) {
        this.$emit('showFeedDetail', id)
    }
    }
}

</script>

<style>

</style>