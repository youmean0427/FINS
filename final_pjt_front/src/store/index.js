import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import _ from 'lodash'
import createPersistedState from 'vuex-persistedstate' // 인증받은 사용자의 토큰 상태를 유지하게 위해 사용하는 라이브러리 


const API_URL = 'http://127.0.0.1:8000'

// tinder
const SERVER_URL = 'http://127.0.0.1:8080/'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies : [],
    token: null,
    BASE_POSTER_PATH : 'https://image.tmdb.org/t/p/original/',

    // Tinder
    genres: [],
    tinderMovie : [],

    // search
    searchMovieList : [],
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
    LOGOUT(state){
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
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
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
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          console.log('회원가입 요청_____',res)
          context.commit('SAVE_TOKEN', res.data.key)
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
    },
    logout(context){
      context.commit('LOGOUT')
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
    submitGenres({commit}, genreItems) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}movies/genres/`,
        data: genreItems.genres,
        headers: genreItems.token
      })
      .then(() => {
        commit('SUBMIT_GENRES')
      })
      .catch(err => console.log(err))
    },

  },
  modules: {
  }
})
