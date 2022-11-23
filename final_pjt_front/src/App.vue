<template>
  <div id="app">

    <!-- nav component로 만들까유?  -->
    <nav class="nav">
      <div>
        <img class="logo" src="https://user-images.githubusercontent.com/87971876/203655544-3bfcbd1f-655d-4149-a63d-d4f8b59adb52.png" alt="로고">
      </div>
      <div id="category">
          <router-link class="logobtn" :to="{ name: 'MovieView' }"><img src="https://user-images.githubusercontent.com/87971876/203657294-a2dfa5fd-d787-4e95-9553-b79a2da62d77.png" alt="movive"></router-link>
          <router-link class="logobtn" :to="{ name: 'DiscoveryMovieView' }"><img src="https://user-images.githubusercontent.com/87971876/203657038-453caf98-d389-459a-851d-eb0e697480a7.png" alt="discovery"></router-link>
          <router-link class="logobtn" :to="{ name: 'FinderMovieView' }"><img src="https://user-images.githubusercontent.com/87971876/203657404-6b395133-ea66-4893-ae80-d5e59f92d39a.png" alt="logo"></router-link>
          <!-- <router-link :to="{ name: 'CreateReview' }">Review</router-link> | -->


          <router-link class="logobtn" :to="{ name: 'ProfileView', params: { username: username } }"><img src="https://user-images.githubusercontent.com/87971876/203657545-e8e536dd-da82-47ba-a703-94a8cc2cf9f4.png" alt="mypage"></router-link>
          
          <router-link class="logobtn" v-if="notLoggedIn" :to="{ name: 'SignUpView' }"><img src="https://user-images.githubusercontent.com/87971876/203659148-a11220fc-cb4b-487f-b4c2-ac56992bf3a0.png" alt="join"></router-link> 
          <router-link class="logobtn" v-if="notLoggedIn" :to="{ name: 'LogInView' } "><img src="https://user-images.githubusercontent.com/87971876/203659176-b2a548d9-0c77-48de-b532-562625a1b243.png" alt="login"> </router-link>
          <button class="logobtn" v-if="loggedIn" @click="logout"><img src="https://user-images.githubusercontent.com/87971876/203656219-c9f7f05b-406e-4b55-9080-f2e8e1d3670c.png" alt="logout"> </button>
          <!-- <router-link :to="{ name: 'CreateReview' }">Review</router-link> | -->
      </div>
    </nav>
    
    <div class="routerview">
      <router-view/>
    </div>
  </div>
</template>

<script>

// 비활성화 상태 로고
//login // https://user-images.githubusercontent.com/87971876/203659234-dd89b5d2-50c1-4e9c-90a5-14308971c965.png
//join // https://user-images.githubusercontent.com/87971876/203659278-306c3899-7844-4a0a-bbe2-d3b587b89e39.png
// mypage //https://user-images.githubusercontent.com/87971876/203659301-44012352-d3d0-4c2f-a48b-f8ad4a1b3eb9.png
//finder //https://user-images.githubusercontent.com/87971876/203659354-0e1e7b3b-d9c1-49d5-9b83-8cac6ac84d9d.png
//discovery // https://user-images.githubusercontent.com/87971876/203659428-5ccd4d15-4753-4896-b053-53c305b9647f.png
// movie // https://user-images.githubusercontent.com/87971876/203659428-5ccd4d15-4753-4896-b053-53c305b9647f.png

export default {
    name: "App",

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
.logo{
  width: 100%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-direction: row;
}
.routerview{
  width: 100%;
}
nav {
  display: flex;
  flex-direction: column;
  padding: 30px;
  width: 30em;
  justify-content: space-between;
  align-items: center;
  height: 100vh;
}

#category  a {
   background-color: transparent;
    width:50%;
    overflow: auto;
    border: none;
}
#category button{
  background-color: transparent;
  width:50%;
  overflow: auto;
  border: none;
}
.logobtn img{
  object-fit: cover;
  width: 100%;
}
#category button > img{
  object-fit: cover;
  width: 100%;
}
#category{
  width: 100%;
  padding: 0;
  height: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#category > a, #category button{
  padding-top: 40px;
}
nav a.router-link-exact-active {
  color: #42b983;
}
body a {
  text-decoration: none;
  color: black;
}
</style>
