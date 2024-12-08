<template>
  <div v-if="isLoading" class="loading-overlay">
    <el-loading
      :fullscreen="true"
      text="加载中..."
    />
  </div>
</template>

<script>
import store from '../store'

export default {
  name: 'LoadingOverlay',
  computed: {
    isLoading() {
      return store.state.isLoading
    }
  }
}
</script>

<style scoped>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255, 255, 255, 0.7);
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style> 