<template>
  <div class="login-container">
    <el-card class="login-card">
      <h2>登录</h2>
      <el-form :model="loginForm" @submit.prevent="handleLogin" label-width="100px">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="loginForm.username" placeholder="请输入用户名"/>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="loginForm.password" placeholder="请输入密码"/>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit" class="submit-button">登录</el-button>
          <router-link to="/register">
            <el-button class="link-button">注册新账号</el-button>
          </router-link>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import store from '../store'

export default {
  name: 'LoginView',
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async handleLogin() {
      try {
        await store.dispatch('login', this.loginForm)
        this.$router.push('/main')
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style scoped>

</style>
