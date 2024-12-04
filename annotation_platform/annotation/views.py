from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdminOrReadOnly
from .models import (
    AnnotationModule,
    ToxicText, ToxicLabel,
    ToxicAnnotation
)
from .serializers import (
    AnnotationModuleSerializer,
    ToxicTextSerializer,
    ToxicLabelSerializer,
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


class ToxicLabelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ToxicLabel.objects.all()
    serializer_class = ToxicLabelSerializer


class ToxicAnnotationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ToxicAnnotation.objects.all()
    serializer_class = ToxicAnnotationSerializer
