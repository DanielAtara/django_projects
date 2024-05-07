from .models import projects
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class Projectviewset(viewsets.ModelViewSet):
    queryset = projects.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
