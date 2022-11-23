<template>
    <div class="cardgroup" >
      <FeedCardTypeItems
        class="carditem"
        v-for="feed in likeMovies"
        :key="feed.id"
        :feed="feed"
        @showFeed="feedDetail(feed.id)"
      />
    </div>
</template>

<script>
import FeedCardTypeItems from '@/components/Accounts/FeedCardTypeItems.vue'

export default {
    name: 'FeedCardType',
    components: {
        FeedCardTypeItems

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
  .cardgroup{
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    max-width: 100%;
  }
  .carditem{
    width: 30%;
    position: relative;
    align-items: stretch;
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    flex-shrink: 0;
    position: relative;
    margin: 3px;
    overflow: hidden;
  }
  .carditem::after{
    content: "";
    display: block;
    padding-bottom: 100%;
  }

  

  
</style>