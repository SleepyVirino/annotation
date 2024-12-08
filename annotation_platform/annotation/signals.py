from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from .models import ToxicAnnotation, ToxicText


# 当 ToxicAnnotation 保存时触发
@receiver(post_save, sender=ToxicAnnotation)
def increment_annotation_count(sender, instance, created, **kwargs):
    """
    每次创建新的 ToxicAnnotation 时增加对应 ToxicText 的标注次数。
    """
    if created:  # 仅在新创建记录时触发
        ToxicText.objects.filter(id=instance.text_id).update(times=models.F('times') + 1)


# 当 ToxicAnnotation 删除时触发
@receiver(post_delete, sender=ToxicAnnotation)
def decrement_annotation_count(sender, instance, **kwargs):
    """
    每次删除一个 ToxicAnnotation 时减少对应 ToxicText 的标注次数。
    """
    ToxicText.objects.filter(id=instance.text_id).update(times=models.F('times') - 1)
