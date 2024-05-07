from rest_framework import routers
from .api import Projectviewset

router=routers.DefaultRouter()

router.register('api/projects', Projectviewset, 'projects')

urlpatterns = router.urls