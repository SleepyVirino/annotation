import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/Login.vue'
import RegisterView from '../views/Register.vue'
import ToxicAnnotationView from '../views/ToxicAnnotation.vue'
import MainView from '../views/Main.vue'
import HomeView from '../views/Home.vue'
import ProfileView from '../views/Profile.vue'
import DataStatisticsView from '../views/DataStatistics.vue'

import store from '../store'

const routes = [
  {
    path: '/',  
    name: 'Root',
    redirect: '/main/home'
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView
  },
  {
    path: '/main',
    name: 'Main',
    component: MainView,
    redirect: '/main/home',
    children: [
      { path: 'home', name: 'Home', component: HomeView }, // 相对路径
      {  
        path: 'person', // 相对路径
        name: 'Person', 
        meta: { requiresAuth: true },
        children: [
          { path: 'profile', name: 'Profile', component: ProfileView }, // 相对路径
          { path: 'data-statistics', name: 'DataStatistics', component: DataStatisticsView } // 相对路径
        ]
      },
      {  
        path: 'annotation', // 相对路径
        name: 'Annotation', 
        meta: { requiresAuth: true },
        children: [
          { path: 'toxic-annotation', name: 'ToxicAnnotation', component: ToxicAnnotationView } // 相对路径
        ]
      }
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