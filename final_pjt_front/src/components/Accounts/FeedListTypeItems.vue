<template>
  <div class="vuegram-post">
    <div class="header level">
      <div class="level-left">
        <div class="image">
          <img class="imageimg" src="https://user-images.githubusercontent.com/87971876/203572590-35117aa5-e24e-4c08-9402-489b2c9888da.png" alt="프로필이미지"/>
        </div>
          <p>username</p>
        
      </div>
    </div>
    <div id="" @click="clickfeed(feed.id)" class="image-container" :style="{backgroundImage:'url('+poster+')'}"> </div>

    <div class="textarea">
      <div class="contenttitle">
        <p class="caption">{{feed.content}}</p>
        <span class="movieTitle">{{movieTitle}}</span>
      </div>
      <div>
        <p class="likes heartbtn"><img :src="heart" alt=""></p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
    name: 'FeedCardTypeItems',
    props:{
      feed : Object
    },
    data(){
      return{
        movieTitle:'',
        heart:'https://user-images.githubusercontent.com/87971876/203576382-75664732-87ee-4657-acad-fdad8d9c1c18.png'
      }
    },
    created(){
      if(this.feed){
        console.log(this.feed)
        this.getMovietitle(this.feed.movie_id)
      }
    },
    computed:{
      poster(){
        return this.feed.image_path
      },
      feedId(){
        return this.feed.id
      }
    },
    methods:{
      clickfeed(id){
        this.$emit('showFeed', id)
      },
      getMovietitle(id){
        this.$store.dispatch('getMovietitle', id)
        this.movieTitle = this.$store.state.likeMovieTitle
      }
    }
}
</script>

<style>
.vuegram-post {
  border: 1px solid rgb(90, 90, 90);
  border-radius: 10px;
  padding-top: 50px;
  margin-top:15px;
  width: 900px;
  min-height: 700px;
}
.level-left{
  padding-left:10px;
  padding-top:10px;
  display: flex;
  align-items: center;

}
.level-left p {
  padding-left:10px;
  padding-top:10px;
}
.vuegram-post ~ .vuegram-post {
  padding-top: 0;
}

.vuegram-post {
  padding: 5px 0;
}
  .header {
    /* height: 30px; */
    border-bottom: 1px solid #fff;
    /* margin: 7.5px 10px; */
    }
    .image{
      overflow: hidden;
      width:50px;
      margin: 0;
      height: 100%;
      border-radius: 50%;
  
    }
    .imageimg {
      object-fit: cover;
      width : 100%;
      height: 100%;
      padding:0;
    }

    .username {
      top: 3px;
      padding-left: 5px;
      font-size: 0.9rem;
      font-weight: bold;
    }

  .level {
    margin-bottom: 0.5rem !important;
  }

  .image-container {
    min-height: 330px;
    max-height: 800px;
    /* width : auto; */
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    top: inherit;
    height: 50vh
  }

  .content {
    margin: 7.5px 10px;
  }

  .far.fa-heart,
  .fas.fa-heart {
    cursor: pointer;
  }

  .fas.fa-heart {
    color: #f06595;
  }

  .likes {
    margin: 5px 0;
    margin-bottom: 5px !important;
    font-size: 0.85rem;
    font-weight: bold;
  }

  .caption {
    font-size: 1rem;
    font-weight: bold;
  }
    span {
      font-weight: bold;
    }
.vuegram-post:last-child {
  margin-bottom: 80px;
}
.heartbtn img{
    width: 30px;
  }
  .heartbtn{
    background-color: transparent;
    border: none;
  }
  .textarea{
    display: flex;
    flex-flow: row wrap;
    justify-content: space-between;
    padding:10px 10px 0px 10px;
  }
  .contenttitle{
    display: flex;
    flex-flow: column wrap;
    align-items: flex-start;
  }
  .movieTitle{
    color: rgb(145, 145, 145);
  }
   /* .hidden-title{
    z-index: 2;
    width: 100%;
    padding:1em;
    position: absolute;
    text-align : center;
    transform: translate(-50%, -50%);
    font-weight: bold;
    display:none;
    color:rgb(59, 59, 59);
    background: rgb(255,255,255);
    background: linear-gradient(90deg, rgba(255,255,255,0.8) 40%, rgb(121, 128, 121, 0.8) 100%);
    top : 50%;
    left: 50%;
    height: 100%;
   } */
  /* #movie-view-card{
    max-width: inherit;
    vertical-align : middle;
    transition: .5s ease;
    border-radius : 6px;
   }
   #movie-view-card:hover{
     transition: .5 ease;
     z-index: 1;
     
   }
   #movie-view-card:hover + .hidden-title{
    transition: .5 ease;
    display: block;
   } */

</style>