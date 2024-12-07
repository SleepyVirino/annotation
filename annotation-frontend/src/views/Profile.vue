<template>
    <div class="profile-container">
      <h2>个人资料</h2>
      <el-form :model="user" label-width="120px" @submit.prevent="updateUser">
        <el-form-item label="用户名">
          <el-input v-model="user.username" disabled />
        </el-form-item>
  
        <el-form-item label="邮箱">
          <el-input v-model="user.email" :disabled="true" />
        </el-form-item>
  
        <el-form-item label="年龄">
          <el-input v-model="user.age" />
        </el-form-item>
  
        <el-form-item label="性别">
          <el-select v-model="user.gender">
            <el-option label="男" value="Male"></el-option>
            <el-option label="女" value="Female"></el-option>
            <el-option label="其他" value="Other"></el-option>
          </el-select>
        </el-form-item>
  
        <el-form-item label="电话号码">
          <el-input v-model="user.phone_number" />
        </el-form-item>
  
        <el-form-item label="微信号码">
          <el-input v-model="user.wechat_number" />
        </el-form-item>
  
        <el-form-item label="教育信息">
          <el-input type="textarea" v-model="user.education_information" />
        </el-form-item>
  
        <!-- 非编辑字段 -->
        <el-form-item label="创建时间">
          <el-input v-model="user.created_at" disabled />
        </el-form-item>
  
        <el-form-item label="最后登录">
          <el-input v-model="user.last_login" disabled />
        </el-form-item>
  
        <el-form-item label="是否为管理员">
          <el-checkbox v-model="user.is_staff" disabled /> 
        </el-form-item>
  
        <el-button type="primary" @click="updateUser">更新</el-button>
      </el-form>
    </div>
  </template>

<script>
import store from '../store'


export default {
  name: 'ProfileView',


  methods: {
    async fetchUserProfile() {
      await store.dispatch('fetchUserProfile');
    },
    async updateUser() {
      await store.dispatch('updateUser', this.user)
      this.user = store.state.user;
    }
  },
  data() {
    this.fetchUserProfile();
    return {
      user: store.state.user
    }
  }
}
</script>

<style scoped>
/* .profile-container {
  padding: 20px;
} */
</style> 