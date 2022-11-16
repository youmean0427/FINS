import Vue from 'vue'
import App from './App.vue'
import store from './store'
import "@/fontAwesome.js"  // font awesome js파일 추가

Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
