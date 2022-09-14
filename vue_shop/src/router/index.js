import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '../components/myLogin.vue'
import home from '../components/myHome.vue'
import welcome from '../components/myWelcome.vue'
import user from '../components/user/myUser.vue'
import menu from '../components/power/myMenu.vue'
import role from '../components/power/myRole.vue'
import cate from '../components/goods/myCate.vue'
import attribute from '../components/goods/myAttribute.vue'
import goods from '../components/goods/myGoods.vue'
import add from '../components/goods/myAdd.vue'
import order from '../components/order/myOrder.vue'
import data from '../components/data/myData.vue'
import '../assets/css/global.css'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    component: login
  },
  {
    path: '/home',
    component: home,
    redirect: '/welcome',
    children: [
      {
        path: '/welcome',
        component: welcome
      },
      {
        path: '/user_list',
        component: user
      },
      {
        path: '/role_list',
        component: menu
      },
      {
        path: '/author_list',
        component: role
      },
      {
        path: '/product_list',
        component: cate
      },
      {
        path: '/group_list',
        component: attribute
      },
      {
        path: '/goods_list',
        component: goods
      },
      {
        path: '/add_goods',
        component: add
      },
      {
        path: '/order_list',
        component: order
      },
      {
        path: '/data_list',
        component: data
      },
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router

router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next()
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('login')
  next()
})
