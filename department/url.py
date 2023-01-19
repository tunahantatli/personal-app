from django.urls import path
from .views import DepartmentView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("department",DepartmentView)

urlpatterns = []
urlpatterns += router.urls