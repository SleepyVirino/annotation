<template>

  <div class="main-container">
    <el-container>
      <el-aside>
        <el-menu default-active="/main/person" class="sidebar" router>
          <el-sub-menu index="/main/person">
            <template v-slot:title>
              <span>个人中心</span>
            </template>
            <el-menu-item index="/main/person/profile">
              <span>个人资料</span>
            </el-menu-item>
            <el-menu-item index="/main/person/data-statistics">
              <span>数据统计</span>
            </el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="/main/annotation">
            <template v-slot:title>
              <span>数据标注</span>
            </template>
            <el-menu-item index="/main/annotation/toxic-annotation">
              <span>毒性文本标注</span>
            </el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-header>
          <router-link :to="{ name: 'Home' }">首页</router-link>
          <el-button v-if="isLoggedIn" type="primary" @click="logout">退出登录</el-button>
          <el-button v-else type="primary" @click="login">登录</el-button>
        </el-header>

        <el-main>
          <router-view/>
      </el-main>

      </el-container>

    </el-container>


  </div>
</template>

<script>
import store from '../store'

export default {
  name: 'MainView',
  data() {
    return {
      isLoggedIn: false // 用于跟踪登录状态
    };
  },
  methods: {
    // 页面加载时检查登录状态
    checkLoginStatus() {
      const token = store.state.token; // 检查 sessionStorage 中的 token
      this.isLoggedIn = !!token; // 如果 token 存在，则表示已登录
    },
    navigateTo(module) {
      this.$router.push({ name: module });
    },
    login() {
      this.$router.push({ name: 'Login' }); // 跳转到登录页面
    },
    logout() {
      // 清除 sessionStorage 并重置状态
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
/* .main-container {
  padding: 20px;
  background-color: #f0f2f5;
}

.sidebar {
  background-color: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.sidebar .el-menu-item {
  font-size: 1em;
  padding: 0.625em 1.25em;
  transition: background-color 0.3s;
}

.sidebar .el-menu-item:hover {
  background-color: #e6f7ff;
}

.sidebar .el-sub-menu {
  margin-bottom: 10px;
}
.el-header {
  display: flex;
  justify-content: flex-end;
  padding: 1em;
  background-color: #ffffff;
  border-bottom: 1px solid #e0e0e0;
}

.el-button {
  margin-left: 10px;
} */

</style>