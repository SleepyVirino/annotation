import axios from 'axios'
import store from '../store'
import router from '../router'
import { ElMessage } from 'element-plus'

// 创建axios实例
const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL || '/api',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  },
  withCredentials: true  // 允许跨域请求携带cookie
})

// 请求拦截器
instance.interceptors.request.use(
  config => {
    // 开始加载
    store.commit('SET_LOADING', true)
    store.commit('CLEAR_ERROR')
    
    // 添加token到请求头
    const token = store.state.token
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    
    // 从cookie中获取CSRF token
    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1]
    
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken
    }
    
    return config
  },
  error => {
    store.commit('SET_LOADING', false)
    return Promise.reject(error)
  }
)

// 响应拦截器
instance.interceptors.response.use(
  response => {
    store.commit('SET_LOADING', false)
    return response
  },
  error => {
    store.commit('SET_LOADING', false)
    
    // 处理错误响应
    const status = error.response?.status
    const message = error.response?.data?.error || '请求失败'
    
    switch (status) {
      case 401:
        // 未授权，清除用户信息并跳转到登录页
        store.dispatch('logout')
        router.push('/login')
        ElMessage.error('登录已过期，请重新登录')
        break
      case 403:
        ElMessage.error('没有权限访问')
        break
      case 404:
        ElMessage.error('请求的资源不存在')
        break
      case 500:
        ElMessage.error('服务器错误')
        break
      default:
        ElMessage.error(message)
    }
    
    return Promise.reject(error)
  }
)

export default instance 