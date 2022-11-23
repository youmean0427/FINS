<template>
  <div class="vuegram-post">
    <div class="header level">
      <div class="level-left">
        <figure class="image">
          <img class="imageimg" src="https://user-images.githubusercontent.com/87971876/203341350-7975d794-b740-4247-a30c-76542d13b71a.png" alt="프로필이미지"/>
        </figure>
        <span class="username">{{movieTitle}}</span>
      </div>
    </div>
    <div class="image-container" :style="{backgroundImage:'url('+poster+')'}"> </div>

    <div class="content">
      <p class="likes">{{feed.id}} likes</p>
      <p class="caption"><span>{{feed.id}}</span> {{feed.content}}</p>
    </div>
  </div>
</template>

<script>
      // <div class="heart">
      //   <!-- <i class="far fa-heart fa-lg"
      //     :class="{'fas': this.post.hasBeenLiked}"
      //     @click="like">
      //   </i> -->
      // </div>
export default {
    name: 'FeedCardTypeItems',
    props:{
      feed : Object
    },
    data(){
      return{
        movieTitle:''
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
  padding-top: 50px;
}
.level-left{
  display: flex;
  align-items: center;

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
      padding-right: 50px;
  
    }
    .imageimg {
      object-fit: cover;
      border-radius: 99px;
      width : -webkit-fill-available;
  
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
    height: 330px;
    /* width : auto; */
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    
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
    font-size: 0.85rem;
  }
    span {
      font-weight: bold;
    }
.vuegram-post:last-child {
  margin-bottom: 80px;
}

</style>