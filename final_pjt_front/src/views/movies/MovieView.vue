<template>
  <div style="margin-top: 30px">
    <div class="wrapper"> 
        <div v-if="loggedIn">
       <b-button style="background:none; color:gray; border:none;" class="btn11" @click="toggleOnOff">{{this.button_name}}</b-button>
       </div>
    </div> 
    <br>
    <div v-show="!isActive"><InfiniteMovieList/></div>

    <!-- button toggle -->
    <div v-if="loggedIn">
    <div v-show="isActive" ><UserMovieList/></div>
    </div>
  </div>
</template>

<script>
import InfiniteMovieList from '@/views/movies/InfiniteMovieList'
import UserMovieList from '@/components/Movies/UserMovieList'
export default {
    name : 'MovieView',
    data() {
        return {
        isActive: false,
        button_name : '당신을 위한 추천영화'
        }
    },
    components:{
        InfiniteMovieList,
        UserMovieList,
    },
    methods:{
        toggleOnOff: function() {
            this.isActive = !this.isActive;
            if (this.isActive === true) {
            this.button_name = '전체 영화'
            } else {
                this.button_name ='당신을 위한 추천영화'
            }

        }

       
    },
    computed: {
        loggedIn(){
            return this.$store.getters.isLogin
    }
    },
    mounted: {
      
    }

}
</script>

<style>

.wrapper { height: 100%; margin: 0 auto; background: #ddd; } 
.btn11 { color: #fff; border: 3px solid #fff; padding: 12px 30px; font-size: 22px; border-radius: 10px; position: absolute;  transform: translate(-50%, -50%); overflow: hidden; transition: all 1s ; 
} 

.btn11:before { content: ""; position: absolute; width: 300px; height: 300px; border-radius: 100px; background-color: black; top: 30px; left: 50%; transform: translate(-50%); animation: wave 5s infinite linear; transition: all 1s; opacity: 0.4; } 
.btn11:hover:before { top: 0px; } 

span { position: relative; }

@keyframes wave {
  0% { transform: translate(-50%) rotate(-180deg); }
  100% { transform: translate(-50%) rotate(360deg); } 
} 

/* 텍스트 안에 물결 */

</style>