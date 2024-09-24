from rest_framework import routers

from product.views import ProductViewSet


router = routers.SimpleRouter()
router.register("product", ProductViewSet, basename="Product")

urlpatterns = router.urls
