from rest_framework import routers
from .api import rolViewSet, desarroladorViewSet,tasksViewSet

router = routers.DefaultRouter()

router.register('api/rol', rolViewSet, 'rol')
router.register('api/desarrolador', desarroladorViewSet, 'desarrolador')
router.register('api/tasks', tasksViewSet, 'tasks')

urlpatterns = router.urls
