from rest_framework import routers

from network.views import NetworkElementViewSet

router = routers.SimpleRouter()
router.register("network_element", NetworkElementViewSet, basename="Network Element")

urlpatterns = router.urls
