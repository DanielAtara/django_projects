from .models import rol,desarrolador,tasks
from rest_framework import viewsets,permissions
from .serializers import rolSerializer,desarroladorSerializer,tasksSerializer

class rolViewSet(viewsets.ModelViewSet):
    queryset = rol.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = rolSerializer
    
class desarroladorViewSet(viewsets.ModelViewSet):
    queryset = desarrolador.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = desarroladorSerializer
    
class tasksViewSet(viewsets.ModelViewSet):
    queryset = tasks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = tasksSerializer