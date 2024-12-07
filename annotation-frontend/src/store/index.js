import { createStore } from 'vuex'
import axios from '../utils/axios'

export default createStore({
  state: {
    user: JSON.parse(sessionStorage.getItem('user')) || null,
    token: sessionStorage.getItem('token') || null,
    isLoading: false,
    error: null,
    annotationStats: JSON.parse(sessionStorage.getItem('annotationStats')) || null
  },

  getters: {
    isAuthenticated: state => !!state.token,
    isAdmin: state => state.user?.is_staff || false,
    getUser: state => state.user,
    getError: state => state.error,
    isLoading: state => state.isLoading,
    getAnnotationStats: state => state.annotationStats
  },

  mutations: {
    SET_USER(state, user) {
      state.user = user
      if (user) {
        sessionStorage.setItem('user', JSON.stringify(user))
      } else {
        sessionStorage.removeItem('user')
      }
    },
    SET_TOKEN(state, token) {
      state.token = token
      if (token) {
        sessionStorage.setItem('token', token)
      } else {
        sessionStorage.removeItem('token')
      }
    },
    SET_LOADING(state, status) {
      state.isLoading = status
    },
    SET_ERROR(state, error) {
      state.error = error
    },
    CLEAR_ERROR(state) {
      state.error = null
    },
    SET_ANNOTATION_STATS(state, stats) {
      state.annotationStats = stats
      if (stats) {
        sessionStorage.setItem('annotationStats', JSON.stringify(stats))
      } else {
        sessionStorage.removeItem('annotationStats')
      } 
    }
  },

  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post('/user/login/', credentials)
        commit('SET_TOKEN', response.data.token)
        commit('SET_USER', response.data.user)
        return response.data
      } catch (error) {
        commit('SET_ERROR', error.response?.data?.error || '登录失败')
        throw error
      }
    },

    async register({ commit }, userData) {
      try {
        const response = await axios.post('/user/register/', userData)
        commit('SET_TOKEN', response.data.token)
        commit('SET_USER', response.data.user)
        return response.data
      } catch (error) {
        commit('SET_ERROR', error.response?.data?.error || '注册失败')
        throw error
      }
    },

    async fetchUserProfile({ commit }) {
      try {
        const response = await axios.get('/user/profile/', this.state.user)
        commit('SET_USER', response.data)
        return response.data
      } catch (error) {
        commit('SET_ERROR', error.response?.data?.error || '获取用户信息失败')
        throw error
      }
    },

    async updateUser({ commit }, userData) {
      try {
        const response = await axios.put('/user/profile/', userData)
        commit('SET_USER', response.data)
        return response.data
      } catch (error) {
        commit('SET_ERROR', error.response?.data?.error || '更新用户信息失败')
        throw error
      }
    },
    logout({ commit }) {
      commit('SET_TOKEN', null)
      commit('SET_USER', null)  
      commit('SET_ANNOTATION_STATS', null)
      sessionStorage.removeItem('token')
      sessionStorage.removeItem('user')
      sessionStorage.removeItem('annotationStats')
    },
    async fetchAnnotationStats({ commit }) {
      try {
        const response = await axios.get('/user/data-statistics/', this.state.user);
        commit('SET_ANNOTATION_STATS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.response?.data?.error || '获取标注统计失败')
        throw error
      }
    }
  }
}) 