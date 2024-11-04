from django.urls import path
from rest_framework.routers import SimpleRouter

from store.apps import StoreConfig
from store.views import ProductViewSet, LinkListAPIView, LinkCreateAPIView, LinkDestroyAPIView, LinkUpdateAPIView, \
    LinkRetrieveAPIView

app_name = StoreConfig.name

router = SimpleRouter()
router.register("product", ProductViewSet, basename="product")

urlpatterns = [
    path("link/", LinkListAPIView.as_view(), name="link_list"),
    path("link/create/", LinkCreateAPIView.as_view(), name="link_create"),
    path("link/<int:pk>/", LinkRetrieveAPIView.as_view(), name="link_retrieve"),
    path("link/<int:pk>/update/", LinkUpdateAPIView.as_view(), name="link_update"),
    path("link/<int:pk>/delete/", LinkDestroyAPIView.as_view(), name="link_delete"),
] + router.urls
