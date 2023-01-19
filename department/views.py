from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DepartmentSerializer
from .models import Department

# Create your views here.
class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
