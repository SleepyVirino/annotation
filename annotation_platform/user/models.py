from django.contrib.auth.models import AbstractUser
from django.db import models


# 创建自定义用户模型
class User(AbstractUser):
    # 基本个人信息字段
    age = models.IntegerField(null=True, blank=True, verbose_name="年龄")  # 年龄
    gender = models.CharField(
        max_length=10,
        choices=[('Male', '男'), ('Female', '女'), ('Other', '其他')],
        null=True,
        blank=True,
        verbose_name="性别"
    )  # 性别

    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name="电话号码")  # 电话号码
    wechat_number = models.CharField(max_length=20, null=True, blank=True,verbose_name="微信号码")
    education_information = models.TextField(null=True, blank=True)

    # 时间戳字段
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # 创建时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")  # 更新时间

    # 元数据（例如数据库表名和中文字段名）
    class Meta:
        db_table = 'user'  # 数据库中的表名
        verbose_name = '用户'  # 单数形式的用户名称
        verbose_name_plural = '用户'  # 复数形式的用户名称

    def __str__(self):
        return self.username  # 返回用户名
