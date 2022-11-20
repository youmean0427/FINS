import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate' // 인증받은 사용자의 토큰 상태를 유지하게 위해 사용하는 라이브러리 
// import common from './modules/common'
// import SecureLS from "secure-ls"; // npm install secure-ls
// import * as Cookies from 'js-cookie'; // npm install --save cookie js-cookie
// var ls = new SecureLS({ isCompression: false });

const API_URL = 'http://127.0.0.1:8000'

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
    BASE_POSTER_PATH : 'https://image.tmdb.org/t/p/original/',
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
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
          alert('비밀번호가 일치하지 않습니다!')
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
            context.state.now_user = name
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
    editProfile(state, payload){
      axios({
        method: 'put',
        url: `${API_URL}/accounts/user/`,
        data: {
          username: payload.username,
          email : payload.email,
          profile_img: payload.profile_img,
        },
        headers: {
          Authorization: `Token ${state.token}`
        }
      })
        .then((res) => {
          console.log('회원정보 수정 요청_____',res)
          alert('회원정보가 수정되었습니다')
        })
    },

  },
  modules: {
    // common,
  }
})
