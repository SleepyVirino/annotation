from django.core.paginator import Paginator
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdminOrReadOnly
from .models import (
    AnnotationModule,
    ToxicText, ToxicLabel,
    ToxicAnnotation, ToxicRisk
)
from .serializers import (
    AnnotationModuleSerializer,
    ToxicTextSerializer,
    ToxicLabelSerializer,
    ToxicRiskSerializer,
    ToxicAnnotationSerializer,
)


class AnnotationModuleViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = AnnotationModule.objects.all()
    serializer_class = AnnotationModuleSerializer


class ToxicTextViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ToxicText.objects.all()
    serializer_class = ToxicTextSerializer

    @action(detail=False, methods=['get'], url_path='unannotated')
    def get_unannotated_texts(self, request):
        user = request.user  # 获取当前请求用户

        # 获取查询参数中的 limit 值，默认为 10
        limit = int(request.query_params.get('limit', 10))

        # 获取用户已标注的 ToxicText IDs
        annotated_text_ids = ToxicAnnotation.objects.filter(user=user).values_list('text_id', flat=True)

        # 查询标注次数小于 5 且用户未标注过的 ToxicText
        unannotated_texts = ToxicText.objects.filter(times__lt=5).exclude(id__in=annotated_text_ids)

        # 使用 limit 限制返回的条数
        paginator = Paginator(unannotated_texts, limit)
        page = paginator.get_page(1)  # 默认取第一页

        # 序列化结果
        serializer = self.get_serializer(page.object_list, many=True)
        return Response(serializer.data)


class ToxicLabelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ToxicLabel.objects.all()
    serializer_class = ToxicLabelSerializer


class ToxicRiskViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ToxicRisk.objects.all()
    serializer_class = ToxicRiskSerializer


class ToxicAnnotationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ToxicAnnotation.objects.all()
    serializer_class = ToxicAnnotationSerializer
