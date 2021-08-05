from rest_framework.routers import DefaultRouter

from apps.api.v1.views import BMIViewSet

router = DefaultRouter()

app_name = 'bmi'

router.register('', BMIViewSet, basename='bmi')

urlpatterns = router.urls
