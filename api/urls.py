from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import ProductsApi,ProductDetail
# from .views import ProductDetail


router = DefaultRouter()

router.register('product', ProductsApi)

urlpatterns = [
    path('',include(router.urls)),
    path('product/', ProductDetail.as_view()),
    path('product/<int:id>', ProductDetail.as_view())
]
