import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import ToxicAnnotation from '../views/ToxicAnnotation.vue'
import Main from '../views/Main.vue'
import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import DataStatistics from '../views/DataStatistics.vue'

import store from '../store'

const routes = [
  {
    path: '/',
    redirect: '/main'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/annotation',
    name: 'ToxicAnnotation',
    component: ToxicAnnotation,
    meta: { requiresAuth: true }
  },
  {
    path: '/main',
    name: 'Main',
    component: Main,
    redirect: '/main/home',
    children: [
      {  path: 'profile', name: 'Profile', component: Profile},
      {  path: 'home', name: 'Home', component: Home},
      {  path: 'data-statistics', name: 'DataStatistics', component: DataStatistics}
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
// 路由守卫
router.beforeEach((to, from, next) => {
    const isAuthenticated = store.getters.isAuthenticated
    const isAdmin = store.getters.isAdmin


  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login')
    } else if (to.matched.some(record => record.meta.requiresAdmin) && !isAdmin) {
      next('/annotation')
    } else {
      next()
    }
  } else {
    next()
  }
})


export default router