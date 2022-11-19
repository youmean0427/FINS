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
    path: '/finder',
    name: 'FinderMovieView',
    component : FinderMovieView,
  },
  {
    path: '/discovery/:genre',
    name: 'GenreMovieListView',
    component : GenreMovieListView,
  },  
  {
    path: '/movies/:id',
    name: 'MovieDetailView',
    component : MovieDetailView,
  },
  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
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
