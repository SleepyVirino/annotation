from rest_framework import serializers
from .models import AnnotationModule, ToxicText, ToxicLabel, ToxicAnnotation


class AnnotationModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotationModule
        fields = '__all__'


class ToxicTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToxicText
        fields = '__all__'


class ToxicLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToxicLabel
        fields = '__all__'


class ToxicAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToxicAnnotation
        fields = '__all__'
