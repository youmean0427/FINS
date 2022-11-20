<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'MovieView' }">Movie</router-link> |
      <router-link :to="{ name: 'DiscoveryMovieView' }">Discovery</router-link> |
      <router-link :to="{ name: 'FinderMovieView' }">Finder</router-link> |
      <!-- <router-link :to="{ name: 'CreateReview' }">Review</router-link> | -->


      <router-link :to="{ name: 'ProfileView', params: { username: username } }">마이페이지</router-link> |
      
      <!-- <router-link :to="{ name: 'ProfileView' }">프로필</router-link> |  -->
      <router-link :to="{ name: 'SignUpView' }">회원가입</router-link> | 
      <router-link v-if="notLoggedIn" :to="{ name: 'LogInView' } ">로그인 </router-link>
      <button v-if="loggedIn" @click="logout">로그아웃 </button> | 
      <!-- <router-link :to="{ name: 'CreateReview' }">Review</router-link> | -->


    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  computed:{
    username(){
      this.$store.dispatch('request_user')
      return this.$store.state.now_user
    },
    notLoggedIn(){
      if(this.$store.getters.isLogin){
        return false
      } else {
        return true
      }
    },
    loggedIn(){
      return this.$store.getters.isLogin
    }
  },
   methods:{
    logout(){
      if (this.$route.path !== '/movies'){
        this.$store.dispatch('logout')
        return this.$router.push({ name : 'MovieView'})
      } else {
        return this.$store.dispatch('logout')
      }
    },
    
   }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
