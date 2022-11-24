<template>
  <div id="app"  style="margin-top: 2%;">

    <!-- nav component로 만들까유?  -->

   
    <img src="@/assets/Line_000.png" alt="" style="margin-left: 2.5%">
    <nav class="nav">
       
       <router-link :to="{ name: 'MovieView' }"><img  class="logo wave-one nav_component" src="@/assets/Fins.png" @click='mov_color' style="margin-left: 2.5%" alt="로고"></router-link>


      <div id="category">
          
          
          <router-link v-show="mov_color_black" class="logobtn nav_component" :to="{ name: 'MovieView' }"><img src="https://user-images.githubusercontent.com/87971876/203657294-a2dfa5fd-d787-4e95-9553-b79a2da62d77.png" @click='mov_color' alt="movive" ></router-link>
          <router-link v-show="mov_color_gray" class="logobtn nav_component" :to="{ name: 'MovieView' }"><img src="@/assets/movie_gray.png" @click='mov_color' alt="movive" ></router-link>
    
          <router-link  v-show="dis_color_gray"  class="logobtn nav_component" :to="{ name: 'DiscoveryMovieView' }"><img src="https://user-images.githubusercontent.com/87971876/203659428-5ccd4d15-4753-4896-b053-53c305b9647f.png"  @click='dis_color' alt="discovery" ></router-link>
        
          <router-link v-show="dis_color_black"  class="logobtn nav_component" :to="{ name: 'DiscoveryMovieView' }"><img src="https://user-images.githubusercontent.com/87971876/203657038-453caf98-d389-459a-851d-eb0e697480a7.png"   @click='dis_color' alt="discovery" ></router-link>
      
          
          <router-link v-show="fin_color_gray"  class="logobtn nav_component" :to="{ name: 'FinderMovieView' }" ><img src="https://user-images.githubusercontent.com/87971876/203659354-0e1e7b3b-d9c1-49d5-9b83-8cac6ac84d9d.png" @click='fin_color'  alt="logo"></router-link>
          
          <router-link v-show="fin_color_black"  class="logobtn nav_component" :to="{ name: 'FinderMovieView' }"><img src="https://user-images.githubusercontent.com/87971876/203657404-6b395133-ea66-4893-ae80-d5e59f92d39a.png" @click='fin_color'  alt="logo"></router-link>
          <!-- <router-link :to="{ name: 'CreateReview' }">Review</router-link> | -->


          <router-link v-show="myp_color_gray"   class="logobtn nav_component" :to="{ name: 'ProfileView', params: { username: username } }"><img src="https://user-images.githubusercontent.com/87971876/203659301-44012352-d3d0-4c2f-a48b-f8ad4a1b3eb9.png" @click='myp_color' alt="mypage"></router-link>
          <router-link v-show="myp_color_black"  class="logobtn nav_component" :to="{ name: 'ProfileView', params: { username: username } }"><img src="https://user-images.githubusercontent.com/87971876/203657545-e8e536dd-da82-47ba-a703-94a8cc2cf9f4.png" @click='myp_color'  alt="mypage"></router-link>


          <router-link v-show="join_color_gray" class="logobtn nav_component" v-if="notLoggedIn" :to="{ name: 'SignUpView' }"><img src="https://user-images.githubusercontent.com/87971876/203659278-306c3899-7844-4a0a-bbe2-d3b587b89e39.png" @click='join_color' alt="join"></router-link> 
          <router-link v-show="join_color_black" class="logobtn nav_component" v-if="notLoggedIn" :to="{ name: 'SignUpView' }"><img src="https://user-images.githubusercontent.com/87971876/203659148-a11220fc-cb4b-487f-b4c2-ac56992bf3a0.png" @click='join_color' alt="join"></router-link> 


          <router-link v-show="login_color_gray" class="logobtn nav_component" v-if="notLoggedIn" :to="{ name: 'LogInView' } "><img src="https://user-images.githubusercontent.com/87971876/203659234-dd89b5d2-50c1-4e9c-90a5-14308971c965.png" @click='login_color' alt="login"> </router-link>
          <router-link v-show="login_color_black" class="logobtn nav_component" v-if="notLoggedIn" :to="{ name: 'LogInView' } "><img src="https://user-images.githubusercontent.com/87971876/203659176-b2a548d9-0c77-48de-b532-562625a1b243.png" @click='login_color' alt="login"> </router-link>


          <button class="logobtn nav_component" v-if="loggedIn" @click="logout"><img src="https://user-images.githubusercontent.com/87971876/203656219-c9f7f05b-406e-4b55-9080-f2e8e1d3670c.png" alt="logout"> </button>
          <!-- <router-link :to="{ name: 'CreateReview' }">Review</router-link> | -->
      </div>
    </nav>
    
    <div class="routerview">
      <router-view/>
    </div>
  </div>
</template>

<script>

// 비활성화 상태 로고 (회색)
//login // https://user-images.githubusercontent.com/87971876/203659234-dd89b5d2-50c1-4e9c-90a5-14308971c965.png
//join // https://user-images.githubusercontent.com/87971876/203659278-306c3899-7844-4a0a-bbe2-d3b587b89e39.png
// mypage //https://user-images.githubusercontent.com/87971876/203659301-44012352-d3d0-4c2f-a48b-f8ad4a1b3eb9.png
//finder //https://user-images.githubusercontent.com/87971876/203659354-0e1e7b3b-d9c1-49d5-9b83-8cac6ac84d9d.png
//discovery // https://user-images.githubusercontent.com/87971876/203659428-5ccd4d15-4753-4896-b053-53c305b9647f.png
// movie // https://user-images.githubusercontent.com/87971876/203659428-5ccd4d15-4753-4896-b053-53c305b9647f.png

// 활성화 상태 로고 (검은색)

// movie // "https://user-images.githubusercontent.com/87971876/203657294-a2dfa5fd-d787-4e95-9553-b79a2da62d77.png
// discovery // https://user-images.githubusercontent.com/87971876/203657038-453caf98-d389-459a-851d-eb0e697480a7.png
// finder // https://user-images.githubusercontent.com/87971876/203657404-6b395133-ea66-4893-ae80-d5e59f92d39a.png
// mypage // https://user-images.githubusercontent.com/87971876/203657545-e8e536dd-da82-47ba-a703-94a8cc2cf9f4.png

// join // https://user-images.githubusercontent.com/87971876/203659148-a11220fc-cb4b-487f-b4c2-ac56992bf3a0.png
// login // https://user-images.githubusercontent.com/87971876/203659176-b2a548d9-0c77-48de-b532-562625a1b243.png
// logout // https://user-images.githubusercontent.com/87971876/203656219-c9f7f05b-406e-4b55-9080-f2e8e1d3670c.png

export default {
    name: "App",

    data() {
      return{ 
        mov_color_black : true,
        mov_color_gray : false,

        fin_color_black : false,
        fin_color_gray : true,

        myp_color_black : false,
        myp_color_gray : true,

        dis_color_black : false,
        dis_color_gray : true,

        join_color_black : false,
        join_color_gray : true,

        login_color_black : false,
        login_color_gray : true,

        logout_color_black : false,
        logout_color_gray : true,
      }
    },

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

    mov_color() {
      this.dis_color_black = false
      this.dis_color_gray = true

      this.mov_color_black = true
      this.mov_color_gray = false

      this.fin_color_black = false
      this.fin_color_gray = true

      this.myp_color_black = false
      this.myp_color_gray = true

      this.join_color_black = false
      this.join_color_gray = true

      this.login_color_black = false
      this.login_color_gray = true

      this.logout_color_black= false
      this.logout_color_gray = true
    },

    dis_color() {
      this.dis_color_black = true
      this.dis_color_gray = false

      this.mov_color_black = false
      this.mov_color_gray = true

      this.fin_color_black = false
      this.fin_color_gray = true

      this.myp_color_black = false
      this.myp_color_gray = true

      this.join_color_black = false
      this.join_color_gray = true

      this.login_color_black = false
      this.login_color_gray = true

      this.logout_color_black= false
      this.logout_color_gray = true
    },

    fin_color() {
      this.dis_color_black = false
      this.dis_color_gray = true

      this.mov_color_black = false
      this.mov_color_gray = true

      this.fin_color_black = true
      this.fin_color_gray = false

      this.myp_color_black = false
      this.myp_color_gray = true

      this.join_color_black = false
      this.join_color_gray = true

      this.login_color_black = false
      this.login_color_gray = true

      this.logout_color_black= false
      this.logout_color_gray = true
    },

    
    join_color() {
      this.dis_color_black = false
      this.dis_color_gray = true

      this.mov_color_black = false
      this.mov_color_gray = true

      this.fin_color_black = false
      this.fin_color_gray = true

      this.myp_color_black = false
      this.myp_color_gray = true

      this.join_color_black = true
      this.join_color_gray = false

      this.login_color_black = false
      this.login_color_gray = true

      this.logout_color_black= false
      this.logout_color_gray = true
    },


    myp_color() {
      this.dis_color_black = false
      this.dis_color_gray = true

      this.mov_color_black = false
      this.mov_color_gray = true

      this.fin_color_black = false
      this.fin_color_gray = true

      this.myp_color_black = true
      this.myp_color_gray = false

      this.join_color_black = false
      this.join_color_gray = true

      this.login_color_black = false
      this.login_color_gray = true

      this.logout_color_black= false
      this.logout_color_gray = true
    },

      login_color() {
      this.dis_color_black = false
      this.dis_color_gray = true

      this.mov_color_black = false
      this.mov_color_gray = true

      this.fin_color_black = false
      this.fin_color_gray = true

      this.myp_color_black = false
      this.myp_color_gray = true

      this.join_color_black = false
      this.join_color_gray = true

      this.login_color_black = true
      this.login_color_gray = false

      this.logout_color_black= false
      this.logout_color_gray = true
    },
   },
   watch: {
    $route() {
      window.scrollTo(0, 0);
    },
  },
  }
</script>

<style>
.logo{
  width: 90%;
}

.name_1{
  width: 20%;
  
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
  position: sticky;
  top: 0;
  display: flex;
  flex-direction: column;
  padding: 0px;
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

.nav_component:hover{
transform: scale(1.1);
transition: 0.5s ease;
}






/*  물결 test */

</style>
