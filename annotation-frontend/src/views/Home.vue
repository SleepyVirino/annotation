<template>
    <div class="main-default">
        <h1>欢迎来到标注平台</h1>
        <p>在这里，您可以轻松地进行文本标注，帮助我们改进机器学习模型。</p>
        <p>请使用左侧菜单导航到不同的模块，开始您的标注之旅！</p>
        <el-card>
            <h2>平台介绍</h2>
            <p>本平台旨在为用户提供一个友好的标注环境，支持多种文本标注任务，包括毒性文本标注、情感分析等。</p>
            <p>我们鼓励用户积极参与，您的每一次标注都将为模型的训练提供宝贵的数据支持。</p>
        </el-card>
        <el-card>
            <h2>使用指南</h2>
            <ul>
                <li>1. 登录您的账户以访问标注功能。</li>
                <li>2. 选择左侧菜单中的“数据标注”以开始标注任务。</li>
                <li>3. 按照提示完成标注，并提交您的结果。</li>
                <li>4. 您可以随时查看您的标注统计信息。</li>
            </ul>
        </el-card>
    </div>
</template>

<script>
export default {
    name: 'HomeView',
}
</script>

<style scoped>
.main-default {
    padding: 20px;
}

h1 {
    color: #409eff;
}

.el-card {
    margin-top: 20px;
    padding: 15px;
}
</style>