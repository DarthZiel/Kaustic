import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import App from './App.vue'
import router from './router/index'
import axios from 'axios'
import store from './store'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)
Vue.use(VueRouter)

Vue.prototype.axios = axios

Vue.use(VueResource)

new Vue({
  el: '#app',
  render: h => h(App),
  vuetify : new Vuetify(),
  router,
  store
})
 