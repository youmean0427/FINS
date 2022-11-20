<template>
  <div>
    <h1>SearchBar</h1>
    <div class="main-input-group">
          <input 
            class="inputBox"
            @keyup.enter="getKeyword"
            v-model.trim="keyword"
            type="text"
            placeholder="search movie">
           <button @click="getKeyword" variant="outline-success"> + </button>
    </div>
  </div>
</template>

<script>
export default {
    name: "SearchBar",
    data() {
        return {
        keyword:null,
        search:'search'
        }
    },
    methods: {
      getKeyword(){
        this.$router.push({ name: 'search', params:{ keyword : this.search}})
      },
    }
}
</script>

<style>

</style>