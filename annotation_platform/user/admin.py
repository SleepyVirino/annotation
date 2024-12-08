from django.contrib import admin
from .models import User
from annotation.models import ToxicAnnotation  # 导入标注模型


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 显示的字段
    list_display = ('username', 'email', 'phone_number', 'wechat_number', 'annotation_count', 'all_annotations')
    search_fields = ('username', 'email', 'phone_number', 'wechat_number')  # 搜索功能
    list_filter = ('gender',)  # 按性别筛选

    def annotation_count(self, obj):
        """
        用户的标注次数统计
        """
        return ToxicAnnotation.objects.filter(user=obj).count()

    annotation_count.short_description = '标注次数'

    def all_annotations(self, obj):
        """
        用户的全部标注记录
        """
        annotations = ToxicAnnotation.objects.filter(user=obj)
        if annotations.exists():
            return ", ".join(f"ID:{ann.id}, Text:{ann.text}" for ann in annotations[:10])  # 显示前10条记录ID
        return "无标注记录"

    all_annotations.short_description = '标注记录（部分展示）'
