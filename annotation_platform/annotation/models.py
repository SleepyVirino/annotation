from django.db import models
from user.models import User


class AnnotationModule(models.Model):
    name = models.CharField(max_length=20, verbose_name="模块名称")
    description = models.TextField(verbose_name="模块描述")
    disclaimer = models.TextField(verbose_name="模块声明")
    need_times = models.IntegerField(default=5, verbose_name="标注次数")

    class Meta:
        db_table = 'annotation_module'
        verbose_name = "标注模块"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ToxicText(models.Model):
    content = models.TextField(verbose_name='文本内容')
    times = models.IntegerField(default=0, verbose_name="标注次数")
    module = models.ForeignKey(AnnotationModule, on_delete=models.CASCADE, verbose_name="标注模块")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'toxic_text'
        verbose_name = '待标注文本'
        verbose_name_plural = '待标注文本'

    def __str__(self):
        return self.content[0:20]


class ToxicLabel(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签名称')

    class Meta:
        db_table = 'toxic_label'
        verbose_name = '毒性标签'
        verbose_name_plural = '毒性标签'

    def __str__(self):
        return self.name


class ToxicRisk(models.Model):
    risk = models.CharField(
        max_length=10,
        choices=[('low', '低风险'), ('medium', '中风险'), ('high', '高风险')],
        null=True,
        blank=True,
        verbose_name="风险等级"
    )

    class Meta:
        db_table = 'toxic_risk'
        verbose_name = "毒性风险"
        verbose_name_plural = "毒性风险"

    def __str__(self):
        return self.risk


class ToxicAnnotation(models.Model):
    text = models.ForeignKey(ToxicText, on_delete=models.CASCADE, verbose_name='标注文本')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='标注用户')
    is_toxic = models.BooleanField(verbose_name='是否有毒')
    toxic_label = models.ForeignKey(ToxicLabel, null=True, blank=True, on_delete=models.SET_NULL,
                                    verbose_name='毒性标签')
    toxic_risk = models.ForeignKey(ToxicRisk, null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name="毒性风险")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'toxic_annotation'
        unique_together = ('text', 'user')
        verbose_name = '标注记录'
        verbose_name_plural = '标注记录'

    def __str__(self):
        return str(self.text)
