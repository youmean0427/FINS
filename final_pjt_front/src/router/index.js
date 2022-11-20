import Vue from 'vue'
import VueRouter from 'vue-router'

import LogInView from '../views/accounts/LogInView.vue'
import ProfileView from '../views/accounts/ProfileView.vue'
import SignUpView from '../views/accounts/SignUpView.vue'

import DiscoveryMovieView from '../views/movies/DiscoveryMovieView.vue'
import FinderMovieView from '../views/movies/FinderMovieView.vue'
import GenreMovieListView from '../views/movies/GenreMovieListView.vue'
import MovieView from '../views/movies/MovieView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'
import KeywordMovieView from '../views/movies/KeywordMovieView.vue'




Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView
    
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  
  
  {
    path: '/discovery',
    name: 'DiscoveryMovieView',
    component : DiscoveryMovieView,
  },
  
  {
    path: '/discovery/:id',
    name: 'GenreMovieListView',
    component : GenreMovieListView,
  },  

  {
    path: '/discovery/:keyword',
    name: 'search',
    component: () => import(/* webpackChunkName: "about" */ '@/views/movies/SearchView.vue')
  },

  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/finder',
    name: 'FinderMovieView',
    
    component : FinderMovieView,
  },
  {
    path: '/movies/:id',
    name: 'MovieDetailView',
    component : MovieDetailView,
  },
  {
    path: '/movies/keyword/:id',
    name: 'KeywordMovieView',
    component : KeywordMovieView,
  },
  // {
  //   path: '/movies/:id/createreview',
  //   name: 'CreateReview',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../components/Movies/CreateReview.vue')
  // },





]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
