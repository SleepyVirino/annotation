<template>
  <div class="main-container">
    <el-container>
      <!-- 侧边栏 -->
      <el-aside class="sidebar">
        <el-menu default-active="/main/person" class="menu" router>
          <el-sub-menu index="/main/person">
            <template v-slot:title>
              <el-icon><HomeFilled /></el-icon>
              <span>个人中心</span>
            </template>
            <el-menu-item index="/main/person/profile">
              <el-icon><User /></el-icon>
              <span>个人资料</span>
            </el-menu-item>
            <el-menu-item index="/main/person/data-statistics">
              <el-icon><DataAnalysis /></el-icon>
              <span>数据统计</span>
            </el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="/main/annotation">
            <template v-slot:title>
              <el-icon><Edit /></el-icon>
              <span>数据标注</span>
            </template>
            <el-menu-item index="/main/annotation/toxic-annotation">
              <el-icon><Failed /></el-icon>
              <span>毒性文本标注</span>
            </el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-aside>
      <!-- 内容区域 -->
      <el-container class="main">
        <!-- 顶部导航栏 -->
        <el-header class="header">
          <div class="header-content">
            <router-link :to="{ name: 'Home' }" class="home-link">首页</router-link>
            <div>
              <el-button 
                v-if="isLoggedIn" 
                type="primary" 
                size="small" 
                @click="logout">
                退出登录
              </el-button>
              <el-button 
                v-else 
                type="primary" 
                size="small" 
                @click="login">
                登录
              </el-button>
            </div>
          </div>
        </el-header>
        <!-- 主内容 -->
        <el-main class="main-content">
          <router-view/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import store from '../store'
import { User, HomeFilled, DataAnalysis, Edit, Failed } from '@element-plus/icons-vue'

export default {
  name: 'MainView',
  components: {
    User,
    HomeFilled,
    DataAnalysis,
    Edit,
    Failed
  },
  data() {
    return {
      isLoggedIn: false // 用于跟踪登录状态
    };
  },
  methods: {
    checkLoginStatus() {
      const token = store.state.token; // 检查 sessionStorage 中的 token
      this.isLoggedIn = !!token; // 如果 token 存在，则表示已登录
    },
    login() {
      this.$router.push({ name: 'Login' }); // 跳转到登录页面
    },
    logout() {
      store.dispatch('logout');
      this.isLoggedIn = false;
      this.$router.push({ name: 'Home' }); // 返回到登录页面
    }
  },
  mounted() {
    this.checkLoginStatus(); // 检查登录状态
  }
};
</script>

<style scoped>

</style>

