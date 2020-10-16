from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'animal', AnimalViewSet, basename = 'user')
router.register(r'animal_type', Animal_TypeViewSet, basename = 'user')
router.register(r'animal_place', Animal_PlaceViewSet, basename = 'user')
router.register(r'staff', StaffViewSet, basename = 'user')

urlpatterns = router.urls

