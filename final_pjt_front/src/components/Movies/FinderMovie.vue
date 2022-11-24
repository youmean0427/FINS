<template>
    <div class="tinderbox">
      <Tinder class="tinderbox" key-name="id" :queue.sync="queue" :offset-y="10" @submit="onSubmit">
        <template slot-scope="scope">
          <div
            class="pic"
            :style="{
              'background-image': `url(${scope.data.id})`
            }"
          />
        </template>
        <img class="like-pointer lp2" slot="like" :src='require(`@/assets/Love.png`)' />
        <img class="like-pointer lp3" slot="like" :src='require(`@/assets/Love.png`)' />
        <img class="like-pointer" slot="like" :src='require(`@/assets/Love.png`)' />
        <img class="nope-pointer" slot="nope" src="https://user-images.githubusercontent.com/87971876/203677620-815c452a-e650-4980-843a-bdc7865bf159.png" />
        <img class="nope-pointer lp2" slot="nope" src="https://user-images.githubusercontent.com/87971876/203677620-815c452a-e650-4980-843a-bdc7865bf159.png" />
        <img class="nope-pointer lp3" slot="nope" src="https://user-images.githubusercontent.com/87971876/203677620-815c452a-e650-4980-843a-bdc7865bf159.png" />
        <img class="super-pointer" slot="super" src="https://user-images.githubusercontent.com/87971876/201873473-65515497-c38c-488c-8066-3fabc516f98b.png" />
      </Tinder>
    </div>
  </template>
  
  <script>
    import Tinder from "vue-tinder"
    // import source from "@/bing"
    
    export default {
      name: "FinderMovie",
      components: { Tinder },
      data: () => ({
        queue: [],
        offset: 0,
      }),
      beforeCreate(){
        this.$store.dispatch('getMovies')
        console.log(this.$store.state.movies.lengths,'~~~~~~~~~~~~~~~~~')
      },
      created() {
        this.mock()

      },
      computed:{
        source(){
          return this.$store.getters.tinderMovie
        }
      },
      methods: {
        mock(count = 5) {

          const list = [];
          for (let i = 0; i < count; i++) {

            // console.log(this.source) 영화 전체 url + movieList의 idx 담긴 리스트

            if (this.$store.getters.tinderMovie[this.offset].selected === false){

              list.push({ id: this.source[this.offset].url, idx : this.source[this.offset].idx })
      
            }
            this.offset++;
          }

          this.queue = this.queue.concat(list);
        },
        
        // FINDER LIKE
        onSubmit({ item, type }) {
          console.log(item, this.$store.state.tinderLike )

          if (type === 'like') {
            this.$store.dispatch('movieLike', item.idx)
          } else if (type === 'nope') {
            this.$store.dispatch('movieNope', item.idx)
          }
          if (this.queue.length < 3) {
            this.mock();
            console.log(item)
          }
        }
      }
    };
  </script>
  
  <style>
  
  /* Scroll 이슈 */
  
  /*
  html,
  body {
    height: 100%;
  }
  .tinderbox{

  }
  
  body {
    margin: 0;
    /* background-color: #20262e; */
    /*  overflow: hidden;
  } */
  
  #app .vue-tinder {
    position: relative;
    z-index: 1;
    left: 0;
    right: 0;
    /* Size Control */
    top: 50px;
    bottom: 46px;
    margin: auto;
    /* Size Control */
    /* 세로 크기 줄이기 */
    min-width: 17vw;
    max-width: 20vw;
    min-height: 70vh;
  }
  
  .nope-pointer,
  .like-pointer {
    position: absolute;
    z-index: 3;
    top:0;
    left: 0;
    padding-left:90px;
    padding-top: 140px;
    width: 370px;
    height: 370px;
    opacity: 0.9;
  }
  .lp3{
    width: 300px;
    height: auto;
    padding-left:220px;
    padding-top: 40px;
  }
  .lp2{
    width: 220px;
    height: auto;
    padding-left:50px;
    padding-top: 40px;
  }
  .nope-pointer {
    right: 10px;
  }
  
  .like-pointer {
    left: 10px;
    
  }
  
  .super-pointer {
    position: absolute;
    z-index: 1;
    bottom: 80px;
    left: 0;
    right: 0;

  }
  
  .pic {
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
  }
  </style>