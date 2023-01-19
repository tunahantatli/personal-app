from django.urls import path
from .views import DepartmentView, JobView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("departments",DepartmentView)
router.register("jobs",JobView)
urlpatterns = []
urlpatterns += router.urls