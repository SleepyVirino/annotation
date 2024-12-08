import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

// 使用懒加载
const LoginView = () => import('../views/Login.vue')
const RegisterView = () => import('../views/Register.vue')
const ToxicAnnotationView = () => import('../views/ToxicAnnotation.vue')
const MainView = () => import('../views/Main.vue')
const HomeView = () => import('../views/Home.vue')
const ProfileView = () => import('../views/Profile.vue')
const DataStatisticsView = () => import('../views/DataStatistics.vue')

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

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      return next('/login')
    } else {
      return next()
    }
  } else {
    return next()
  }
})

export default router
