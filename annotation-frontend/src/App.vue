<template>
  <div id="app">
    <loading-overlay/>
    <el-config-provider :locale="zhCn">
      <router-view/>
    </el-config-provider>
  </div>
</template>

<script>
import {ElConfigProvider} from 'element-plus'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import LoadingOverlay from './components/LoadingOverlay.vue'

export default {
  name: 'App',
  components: {
    LoadingOverlay,
    ElConfigProvider
  },
  data() {
    return {
      zhCn
    }
  },
  created() {
    // 如果有token，获取用户信息
    // if (this.$store.getters.isAuthenticated) {
    //   this.$store.dispatch('fetchUserProfile')
    // }
  }
}
</script>

<style>
#app {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
  'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.el-message {
  z-index: 9999 !important;
}
</style>
