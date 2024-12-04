from rest_framework.routers import DefaultRouter
from .views import (
    AnnotationModuleViewSet,
    ToxicTextViewSet,
    ToxicLabelViewSet,
    ToxicAnnotationViewSet,
)

app_name = 'annotation'

router = DefaultRouter()
router.register(r'annotation-modules', AnnotationModuleViewSet)
router.register(r'toxic-texts', ToxicTextViewSet)
router.register(r'toxic-labels', ToxicLabelViewSet)
router.register(r'toxic-annotations', ToxicAnnotationViewSet)

urlpatterns = router.urls
