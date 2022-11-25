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
        this.$emit('showFeedModal', id)
    }
    }
}

</script>

<style>
  .cardgroup{
    margin-top: 30px;
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    width:100%;
  }
  .carditem{
    width: 29%;
    max-width: 500px;
    max-height: 500px;
    position: relative;
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    flex-shrink: 0;
    position: relative;
    overflow: hidden;
    margin-right:18px;
    margin-bottom: 18px;
    background-color: transparent;
  }
  .carditem::after{
    content: "";
    display: block;
    padding-bottom: 100%;
  
}

  

  
</style>