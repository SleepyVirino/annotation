<template>
  <div class="data-statistics-container">
    <h2>个人标注统计</h2>
    <el-card>
      <div class="stat-item">
        <div class="stat-label">已标注数量</div>
        <div class="stat-value">{{ annotationStats.total || 0 }}</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">毒性文本数</div>
        <div class="stat-value">{{ annotationStats.toxic || 0 }}</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">非毒性文本数</div>
        <div class="stat-value">{{ annotationStats.non_toxic || 0 }}</div>
      </div>
    </el-card>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'DataStatisticsView',
  computed: {
    ...mapState(['annotationStats']),
  },
  created() {
    this.fetchAnnotationStats();
  },
  methods: {
    async fetchAnnotationStats() {
      await this.$store.dispatch('fetchAnnotationStats');
    },
  },
};
</script>

<style scoped>
.data-statistics-container {
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
}
</style>
