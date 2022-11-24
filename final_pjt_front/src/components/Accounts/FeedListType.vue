<template>
  <div id="listFeed">
    <div id="list">
      <FeedListTypeItems
        v-for="feed in likeMovies"
        :key="feed.id"
        :feed="feed"
        @showFeed="feedDetail(feed.id)"
      />
    </div>
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
        this.$emit('showFeedModal', id)
    }
    }
}

</script>

<style>
  #listFeed{
    display: flex;
    justify-content: center;
  }
  #list{
  }
</style>