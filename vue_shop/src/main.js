import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import axios from 'axios'
import qs from 'qs'

// 程序主入口
Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs

// 设置一个请求拦截器 来设置token
axios.interceptors.request.use(
  config => {
    // 获取token，sessionStorage
    const tokenStr = window.sessionStorage.getItem('token')
    if (tokenStr) {
      config.headers.token = tokenStr
    }
    return config
  }
)

// 设置一个响应拦截器，来处理token是否有效
axios.interceptors.response.use(
  response => {
    if (response.data.status === 1006 || response.data.status === 1007) {
      window.sessionStorage.removeItem('token')
      // 跳转到登录页面
      router.replace(
        {
          path: '/login'
        }
      )
    }
    return response
  }
)
// axios.defaults.baseURL = 'http://localhost:5000'
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
