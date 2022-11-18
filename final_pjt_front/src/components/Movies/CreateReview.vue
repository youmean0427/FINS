<template>
  <div>
      <h1>댓글 작성</h1>
        <form @submit.prevent="createReview">
            <label for="content">내용 ㅣ </label>
            <input type="text" id="content" v-model.trim="content">
            <input type="submit" id="sumbit">
        </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'CreateReview',
    data() {
        return{
            content: null,
        }
    },
    methods: {
        createReview(){
            const content = this.content
            if(!content) {
                alert('내용을 입력하세요')
                return
            }
            axios({
                method: 'post',
                url: `${API_URL}/api/v1/movies/1/createreview/`, // ------------------------로그인 기능 구현 후 바꿀 부분
                data: {
                    content : content,
                }
            })
            .then((res) => {
                console.log(res)
                this.$router.push({name: 'MovieView'})
            })
            .catch(() => {this.$router.push({name: 'MovieView'})})
        }
    }

}
</script>

<style>

</style>