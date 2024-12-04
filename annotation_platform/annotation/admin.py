from django.contrib import admin
from .models import (
    AnnotationModule,
    ToxicText, ToxicLabel,
    ToxicRisk, ToxicAnnotation
)

admin.site.register(ToxicLabel)
admin.site.register(ToxicRisk)


@admin.register(AnnotationModule)
class AnnotationModuleAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(ToxicAnnotation)
class ToxicAnnotationAdmin(admin.ModelAdmin):
    search_fields = ['text', 'user']
    list_filter = ['is_toxic', 'toxic_label', 'toxic_risk']


@admin.register(ToxicText)
class ToxicTextAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_filter = ["module",'times']
