from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, MissionViewSet

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"missions", MissionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
