<template>
  <div class="register-container">
    <el-card class="register-card">
      <h2>注册</h2>
      <el-form 
        :model="registerForm" 
        :rules="rules"
        ref="registerForm"
        label-width="100px"
        @submit.prevent="handleRegister"
      >
        <!-- 基本信息 -->
        <el-form-item label="用户名" prop="username">
          <el-input v-model="registerForm.username" placeholder="请输入用户名" />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="registerForm.password" placeholder="请输入密码" />
        </el-form-item>
        <el-form-item label="确认密码" prop="confirmPassword">
          <el-input type="password" v-model="registerForm.confirmPassword" placeholder="请再次输入密码" />
        </el-form-item>

        <!-- 个人信息 -->
        <el-form-item label="年龄" prop="age">
          <el-input-number v-model="registerForm.age" :min="1" :max="120" />
        </el-form-item>
        
        <el-form-item label="性别" prop="gender">
          <el-select v-model="registerForm.gender" placeholder="请选择性别">
            <el-option label="男" value="Male" />
            <el-option label="女" value="Female" />
            <el-option label="其他" value="Other" />
          </el-select>
        </el-form-item>

        <el-form-item label="地址" prop="address">
          <el-input v-model="registerForm.address" placeholder="请输入地址" />
        </el-form-item>

        <el-form-item label="电话号码" prop="phone_number">
          <el-input v-model="registerForm.phone_number" placeholder="请输入电话号码" />
        </el-form-item>

        <el-form-item label="微信号码" prop="wechat_number">
          <el-input v-model="registerForm.wechat_number" placeholder="请输入微信号码" />
        </el-form-item>

        <el-form-item label="教育信息" prop="education_information">
          <el-input type="textarea" v-model="registerForm.education_information" placeholder="请输入教育信息" />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" native-type="submit" class="submit-button">注册</el-button>
          <router-link to="/login">
            <el-button class="link-button">返回登录</el-button>
          </router-link>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'RegisterView',
  data() {
    return {
      registerForm: {
        username: '',
        password: '',
        confirmPassword: '',
        age: null,
        gender: '',
        address: '',
        phone_number: '',
        wechat_number: '',
        education_information: ''
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, message: '密码长度不能小于6位', trigger: 'blur' }
        ],
        confirmPassword: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          { validator: this.validatePass2, trigger: 'blur' }
        ],
        phone_number: [
          { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号码', trigger: 'blur' }
        ],
        wechat_number: [
          { max: 20, message: '微信号码不能超过20个字符', trigger: 'blur' }
        ],
        education_information: [
          { max: 200, message: '教育信息不能超过200个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    validatePass2(rule, value, callback) {
      if (value !== this.registerForm.password) {
        callback(new Error('两次输入的密码不一致'))
      } else {
        callback()
      }
    },
    async handleRegister() {
      try {
        await this.$refs.registerForm.validate()
        
        // 构造注册数据，移除确认密码字段
        const registerData = { ...this.registerForm }
        delete registerData.confirmPassword
        
        await this.$store.dispatch('register', registerData)
        this.$message.success('注册成功，请登录')
        this.$router.push('/login')
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
  background-color: #f5f7fa;
}

.register-card {
  width: 500px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #303133;
}

.el-form-item {
  margin-bottom: 20px;
}

.el-input, .el-select {
  border-radius: 5px;
}

.submit-button {
  width: 120px;
  margin-right: 10px;
}

.link-button {
  width: 120px;
  background-color: #f0f0f0;
  color: #409eff;
}

.el-button:hover.link-button {
  background-color: #e0e0e0;
}

.el-button:hover.submit-button {
  background-color: #409eff;
  color: white;
}

.el-form-item:last-child {
  margin-bottom: 0;
  text-align: center;
}
</style>