import Vue from 'vue'
import VueRouter from 'vue-router'

import LogInView from '../views/accounts/LogInView.vue'
import SignUpView from '../views/accounts/SignUpView.vue'

import DiscoveryMovieView from '../views/movies/DiscoveryMovieView.vue'
import FinderMovieView from '../views/movies/FinderMovieView.vue'
import GenreMovieListView from '../views/movies/GenreMovieListView.vue'
import MovieView from '../views/movies/MovieView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'
import store from '../store/index';

const requireAuth = () => (to, from, next) => {
  if (store.state.token) {
    return next();
  }
  next('/login');
};

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
    component: () => import('../views/accounts/ProfileView.vue'),
    beforeEnter : requireAuth()
  },
  {
    path: '/profile/edit',
    name : 'ProfileEditView',
    component: () => import('../views/accounts/ProfileEditView.vue')
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
  {
    path: '*',
    redirect: { name: 'MovieView' }
  },





]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
