from django.urls import include,path
from rest_framework import routers
from .views import ProductViewSet,ProductReviewViewSet

router = routers.DefaultRouter()
router.register('products',ProductViewSet)
router.register('reviews',ProductReviewViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('permission/',include("rest_framework.urls")),
]