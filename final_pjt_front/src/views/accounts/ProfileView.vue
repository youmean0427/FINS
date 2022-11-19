<template>
  <div>
    <h1>ProfileView</h1>
    <FeedList/>
  </div>
</template>

<script>
import FeedList from '@/components/Accounts/FeedList.vue'

export default {
    name: 'ProfileView',
    components: {
      FeedList
    }
}
</script>

<style>

</style>