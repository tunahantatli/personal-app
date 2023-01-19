from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DepartmentSerializer, JobSerializer, StaffSerializer
from .models import Department, Job
from .permissions import IsStafforReadOnly

# Create your views here.
class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsStafforReadOnly,)

    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.request.user.is_staff:
            return StaffSerializer

        return serializer

class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(user=self.request.user)
