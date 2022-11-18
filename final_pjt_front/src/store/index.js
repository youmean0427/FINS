import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies : [],
    BASE_POSTER_PATH : 'https://image.tmdb.org/t/p/original/',
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state,movies){
      state.movies = movies
    }
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

    }
  },
  modules: {
  }
})
