<template>
  <div>
    <h1>FeedList</h1>
    <FeedListTypeItems
      v-for="feed in likeMovies"
      :key="feed.id"
      :feed="feed"
      @showFeed="feedDetail(feed.id)"
    />
  </div>
</template>

<script>
import FeedListTypeItems from '@/components/Accounts/FeedListTypeItems.vue'

export default {
    name: 'FeedListType',
    components: {
        FeedListTypeItems

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