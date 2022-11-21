import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import _ from 'lodash'
import createPersistedState from 'vuex-persistedstate' // 인증받은 사용자의 토큰 상태를 유지하게 위해 사용하는 라이브러리 
// import common from './modules/common'
// import SecureLS from "secure-ls"; // npm install secure-ls
// import * as Cookies from 'js-cookie'; // npm install --save cookie js-cookie
// var ls = new SecureLS({ isCompression: false });

const API_URL = 'http://127.0.0.1:8000'

// // tinder
// const SERVER_URL = 'http://127.0.0.1:8080/'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      // key: 'key',
      // paths:['LogIn'], // 해당 모듈의 state값만 localstorage에 저장
      // storage: {
        // getItem: (key) => JSON.parse(Cookies.get(key)),
        // setItem: (key, value) => Cookies.set(key, JSON.stringify(value), {expires: 3, secure: true}),
        // removeItem: (key) => Cookies.remove(key)

        // getItem: (key) => ls.get(key),
        // setItem: (key, value) => ls.set(key,value),
        // removeItem: (key) => ls.remove(key)
      // }
  })],
  state: {
    movies : [],
    token: null,
    now_user : '',
    now_user_pk: '',
    BASE_POSTER_PATH : 'https://image.tmdb.org/t/p/original/',

    // Tinder
    genres: [],
    tinderMovie : [],

    // Search
    searchMovieList : [],

    // Like Check
    likeCheck : false,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },

    // Tinder

    randomMovie(state) {
      // lodash를 사용해서 랜덤한 번호를 추출
      // 영화 요청 9번 했을 때 180개의 영화가 담겨있음 
      const randomNumber = _.sample(_.range(0, 180))
      state.randomMovie = state.movieList[randomNumber]
      return state.randomMovie
    },


    

    tinderMovie(state){
      for (var i = 0; i < 100; i++){
        const randomNumber = _.sample(_.range(0, 180))
        state.tinderMovie[i] = {
          url : state.BASE_POSTER_PATH + state.movieList[randomNumber].poster_path,
          idx : randomNumber,
          selected : false,
        }
      }
      return state.tinderMovie
    },

    // Search

    searchMovieListLen(state){
      return state.searchMovieList.length
    },
   

  },


  mutations: {
    GET_MOVIES(state,movies){
      return state.movies = movies
    },


    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'MovieView' })
    },
    DELETE_TOKEN(state){
      state.token = null
    },
    GET_RANDOM_MOVIES(state, res) {
      state.randomMovies = res
    },

    SEARCH_MOVIE(state, m){
      state.searchMovieList = m
      console.log('검색한 영화리스트 담기 완료')
      console.log(state.searchMovieList)
      console.log('======================')
    },
    
  },




  actions: {
    getMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          // console.log(res, context) // 받은 데이터 state에 저장
          // console.log(res.data)// 받은 데이터 state에 저장
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })

    },

    signUp(context,payload){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          email : payload.email,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          console.log('회원가입 요청_____',res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) =>{
          console.log(err.response.data)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err)=>{
          console.log('왜 로그인이 안되죠?', err)
          alert('비밀번호가 일치하지 않습니다!')``
        })
    },
    logout(context){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log('로그아웃 되었습니다..', res)
          context.commit('DELETE_TOKEN')
        })
    },

    // search

    search_movie(context, movies){
      context.commit('SEARCH_MOVIE', movies)
    },

    // Tinder
    getRandomMovies(context) {
      const randomNumber = _.sample(_.range(0, 5))
      context.state.randomMovie = context.state.movieList[randomNumber]
      context.commit('GET_RANDOM_MOVIES',context.state.randomMovie)
    },
    movieLike({commit}, genres) {
      commit('MOVIE_LIKE', genres)
    },
    movieNope({commit}, genres) {
      commit('MOVIE_NOPE', genres)
    },
    // submitGenres({commit}, genreItems) {
    //   axios({
    //     method: 'POST',
    //     url: `${SERVER_URL}movies/genres/`,
    //     data: genreItems.genres,
    //     headers: genreItems.token
    //   })
    //   .then(() => {
    //     commit('SUBMIT_GENRES')
    //   })
    //   .catch(err => console.log(err))
    // },
    // 요청한 사용자의 이름을 반환해주는 메서드
    request_user(context){
      if(context.state.token){
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${context.state.token}`
          }
        })
          .then((res) => {
            console.log('res.data.username======',res.data.username)
            const name = res.data.username
            const name_id = res.data.id
            context.state.now_user = name
            context.state.now_user_id = name_id
          })
          .catch((err) => {
            console.log('-==--------이름을 받아올 수 없엉')
            console.log(err)
            return null
          })
      }
    },
    isMyPage(context, profile_username){
      let is_sameuser = false
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log(res, context) // 받은 데이터 state에 저장
          // console.log(res.data)// 받은 데이터 state에 저장
          if(res.data.username === profile_username){
            is_sameuser = true
          }
        })
        .catch((err) => {
          console.log(err)
        })
        return is_sameuser
    },
    editProfile(context, payload){

      axios({
        method: 'put',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
        data: {
          username: payload.username,
          email : payload.email,
          profile_img: payload.profile_img,
        },

      })
        .then((res) => {
          console.log('회원정보 수정 요청_____',res)
          alert('회원정보가 수정되었습니다')
          context.state.now_user = payload.username
          router.push({name:'ProfileView', params: { username: payload.username}})
        })
        .error((err) =>{
          console.log('회원정보 수정에 실패했습니다.')
          alert('로그인이 만료되었습니다')
          console.log(err.message)
        })
    },
    changePwd(context, payload){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
        data:{
          new_password1 : payload.new_password1,
          new_password2 : payload.new_password2
        }
      })
      .then(() => {
        console.log('비밀번호 변경 성공')
        router.push({name:'ProfileView', params: { username: context.state.now_user}})
      })
      .catch((err) => console.log('비밀번호 변경 실패...',err ))
    },

    // --------------------- like ----------------------------
    like_movie(context, movieId){
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/like/${movieId}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          if (res.data.status == '좋아하는상태'){
            context.state.likeCheck  = true
          }else{
            context.state.likeCheck  = false
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },

    // review_delete
    delete_review(context, reviewId){
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/movies/review/${reviewId}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },

      // review_edit
      edit_review(context, payload){
        console.log(payload)
        axios({
          method: 'put',
          url: `${API_URL}/api/v1/movies/review/${payload.reviewId}/`,
          data: {
            content: payload.inputData
          },
          headers: {
            Authorization: `Token ${context.state.token}`
          },
          
        })
          .then(() => {
            window.location.reload() 
            
          })
          .catch((err) => {
            console.log(err)
         
          })
      }

  },
  modules: {
    // common,
  }
})
