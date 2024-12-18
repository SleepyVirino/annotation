import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from './utils/axios'


const app = createApp(App)

// 将axios实例添加到全局属性
app.config.globalProperties.$axios = axios

app.use(store)
   .use(router)
   .use(ElementPlus)
   .mount('#app')
