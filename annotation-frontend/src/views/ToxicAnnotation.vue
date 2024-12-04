<template>
  <div class="annotation-container">
    <!-- 模块说明和免责声明对话框 -->
    <el-dialog
      v-model="showInfo"
      title="模块说明"
      width="50%"
      :close-on-click-modal="false"
      :close-on-press-escape="false"
      :show-close="false"
    >
      <div class="module-info">
        <h3>模块说明</h3>
        <p>{{ moduleInfo.description }}</p>
        <h3>免责声明</h3>
        <p>{{ moduleInfo.disclaimer }}</p>
      </div>
      <template #footer>
        <el-button type="primary" @click="showInfo = false">我已了解</el-button>
      </template>
    </el-dialog>

    <!-- 标注区域 -->
    <el-card v-if="currentText" class="annotation-card">
      <!-- 文本内容展示 -->
      <div class="text-content">
        <h3>待标注文本：</h3>
        <p>{{ currentText.content }}</p>
      </div>

      <!-- 标注表单 -->
      <el-form
        :model="annotationForm"
        :rules="rules"
        ref="annotationForm"
        label-width="120px"
        @submit.prevent="submitAnnotation"
      >
        <!-- 毒性判断 -->
        <el-form-item label="是否有毒" prop="is_toxic">
          <el-switch
            v-model="annotationForm.is_toxic"
            active-text="是"
            inactive-text="否"
          />
        </el-form-item>

        <!-- 毒性文本相关字段 -->
        <template v-if="annotationForm.is_toxic">
          <!-- 毒性标签 -->
          <el-form-item label="毒性标签" prop="toxic_label">
            <el-select
              v-model="annotationForm.toxic_label"
              placeholder="请选择毒性标签"
            >
              <el-option
                v-for="label in availableLabels"
                :key="label.id"
                :label="label.name"
                :value="label.id"
              />
            </el-select>
          </el-form-item>

          <!-- 毒性原因 -->
          <el-form-item label="毒性原因" prop="toxic_reason">
            <el-input
              type="textarea"
              v-model="annotationForm.toxic_reason"
              :rows="3"
              placeholder="请详细说明该文本的毒性原因"
            />
          </el-form-item>
        </template>

        <!-- 提交按钮 -->
        <el-form-item>
          <el-button type="primary" native-type="submit" :loading="submitting">
            提交标注
          </el-button>
          <el-button @click="skipText" :disabled="submitting">跳过</el-button>
        </el-form-item>
      </el-form>
    </el-card>

    <!-- 无可用文本时显示 -->
    <el-empty
      v-else
      description="暂无可标注的文本"
      :image-size="200"
    >
      <template #description>
        <p>{{ noTextMessage || '暂无可标注的文本' }}</p>
      </template>
    </el-empty>

    <!-- 标注进度 -->
    <el-card v-if="annotationStats" class="stats-card">
      <template #header>
        <div class="stats-header">
          <span>标注进度</span>
        </div>
      </template>
      <el-row :gutter="20">
        <el-col :span="8">
          <div class="stat-item">
            <div class="stat-label">已标注数量</div>
            <div class="stat-value">{{ annotationStats.total || 0 }}</div>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="stat-item">
            <div class="stat-label">毒性文本数</div>
            <div class="stat-value">{{ annotationStats.toxic || 0 }}</div>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="stat-item">
            <div class="stat-label">非毒性文本数</div>
            <div class="stat-value">{{ annotationStats.non_toxic || 0 }}</div>
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'ToxicAnnotationView',
  data() {
    return {
      showInfo: true,
      moduleInfo: {
        description: '',
        disclaimer: ''
      },
      currentText: null,
      availableLabels: [],
      annotationForm: {
        is_toxic: false,
        toxic_label: null,
        toxic_reason: ''
      },
      submitting: false,
      annotationStats: null,
      noTextMessage: '',
      rules: {
        toxic_label: [
          { 
            required: true, 
            message: '请选择毒性标签', 
            trigger: 'change',
            validator: (rule, value, callback) => {
              if (this.annotationForm.is_toxic && !value) {
                callback(new Error('毒性文本必须选择标签'))
              } else {
                callback()
              }
            }
          }
        ],
        toxic_reason: [
          {
            required: true,
            message: '请输入毒性原因',
            trigger: 'blur',
            validator: (rule, value, callback) => {
              if (this.annotationForm.is_toxic && !value) {
                callback(new Error('毒性文本必须说明原因'))
              } else {
                callback()
              }
            }
          }
        ]
      }
    }
  },
  async created() {
    await this.getModuleInfo()
    await this.getNextText()
    await this.fetchAnnotationStats()
  },
  methods: {
    async getModuleInfo() {
      try {
        const response = await this.$axios.get('/annotation/module-info/')
        this.moduleInfo = response.data
      } catch (error) {
        this.$message.error('获取模块信息失败')
      }
    },
    
    async getNextText() {
      try {
        const response = await this.$axios.get('/annotation/get-text/')
        this.currentText = response.data.text
        this.availableLabels = response.data.available_labels
      } catch (error) {
        if (error.response?.status === 404) {
          this.noTextMessage = error.response.data.message
        } else {
          this.$message.error('获取文本失败')
        }
      }
    },

    async submitAnnotation() {
      try {
        await this.$refs.annotationForm.validate()
        this.submitting = true
        
        await this.$axios.post('/annotation/submit-annotation/', {
          text: this.currentText.id,
          is_toxic: this.annotationForm.is_toxic,
          toxic_reason: this.annotationForm.is_toxic ? this.annotationForm.toxic_reason : null,
          toxic_label: this.annotationForm.is_toxic ? this.annotationForm.toxic_label : null
        })

        this.$message.success('标注成功')
        this.resetForm()
        await Promise.all([
          this.getNextText(),
          this.fetchAnnotationStats()
        ])
      } catch (error) {
        if (error === false) {
          // 表单验证失败
          this.$message.error('请完善标注信息')
        } else {
          this.$message.error(error.response?.data?.error || '提交失败')
        }
      } finally {
        this.submitting = false
      }
    },

    async skipText() {
      await this.getNextText()
    },

    async fetchAnnotationStats() {
      try {
        const response = await this.$axios.get('/annotation/my-annotations/stats/')
        this.annotationStats = response.data
      } catch (error) {
        console.error('获取标注统计失败:', error)
      }
    },

    resetForm() {
      this.annotationForm = {
        is_toxic: false,
        toxic_label: null,
        toxic_reason: ''
      }
      if (this.$refs.annotationForm) {
        this.$refs.annotationForm.resetFields()
      }
    }
  }
}
</script>

<style scoped>
.annotation-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

.module-info {
  margin-bottom: 20px;
}

.module-info h3 {
  margin-top: 20px;
  margin-bottom: 10px;
  color: #303133;
}

.annotation-card {
  margin-bottom: 20px;
}

.text-content {
  margin-bottom: 20px;
  padding: 15px;
  background-color: #f5f7fa;
  border-radius: 4px;
}

.text-content h3 {
  margin-top: 0;
  margin-bottom: 10px;
  color: #303133;
}

.stats-card {
  margin-top: 20px;
}

.stats-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.stat-item {
  text-align: center;
  padding: 10px;
}

.stat-label {
  color: #909399;
  font-size: 14px;
  margin-bottom: 5px;
}

.stat-value {
  color: #303133;
  font-size: 24px;
  font-weight: bold;
}

.el-form-item:last-child {
  margin-bottom: 0;
  text-align: center;
}

.el-button {
  min-width: 120px;
  margin: 0 10px;
}
</style>
