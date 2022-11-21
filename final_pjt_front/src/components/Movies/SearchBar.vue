<template>
  <div>
    <h1>SearchBar</h1>
    <div>
          <input 
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
        }
    },
    methods: {
      getKeyword(){
        this.$router.push({ name: 'search', params:{ keyword : this.keyword}})
      },
    }
}
</script>

<style>

</style>