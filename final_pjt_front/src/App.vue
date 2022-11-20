<template>
  <div id="app">

    <!-- nav component로 만들까유?  -->
    <nav>
      <router-link :to="{ name: 'MovieView' }">Movie</router-link> |
      <router-link :to="{ name: 'DiscoveryMovieView' }">Discovery</router-link> |
      <router-link :to="{ name: 'FinderMovieView' }">Finder</router-link> |
      <!-- <router-link :to="{ name: 'CreateReview' }">Review</router-link> | -->


      <!-- <router-link :to="{ name: 'ProfileView', params: { username: username } }">프로필</router-link> | -->
      
      <router-link :to="{ name: 'ProfileView', params: {username: 1}}">프로필</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">회원가입</router-link> | 
      <router-link :to="{ name: 'LogInView' } ">로그인</router-link> | 
      <button @click="logout">로그아웃</button> | 
     
      <!-- <router-link :to="{ name: 'CreateReview' }">Review</router-link> | -->

      
    </nav>
    
    <router-view/>

    <!-- 이거 첫화면에 뛰우고 싶음 근데 계속 유지됨  -->
    <TodayMovie/>


  </div>
</template>

<script>
import TodayMovie from './components/Movies/TodayMovie.vue'
export default {
    name: "App",
    components: {
      TodayMovie
    },
    methods:{
      logout(){
  
          return this.$store.dispatch('logout')
      }
    },
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
