<template>
  <div class="data-statistics-container">
    <h2>个人标注统计</h2>
    <el-card>
      <div class="stat-item">
        <div class="stat-label">已标注数量</div>
        <div class="stat-value" v-if="annotationStats">{{ annotationStats.total || 0 }}</div>
        <div class="stat-value" v-else>0</div>
      </div>
    </el-card>
  </div>
</template>

<script>
import store from '../store'

export default {
  name: 'DataStatisticsView',
  data() {
    return {
        annotationStats: store.state.annotationStats
    }
  },
  async created() {
    await this.fetchAnnotationStats()
  },

  methods: {
    async fetchAnnotationStats() {
      await store.dispatch('fetchAnnotationStats');
      this.annotationStats = store.state.annotationStats;
    },
  },
};
</script>

<style scoped>
/* .data-statistics-container {
  padding: 20px;
}
.stat-item {
  margin-bottom: 10px;
}
.stat-label {
  font-weight: bold;
}
.stat-value {
  color: #409eff;
} */
</style>
