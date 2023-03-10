from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')

# carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')


urlpatterns = router.urls 
