from django.urls import include, path
from rest_framework import routers
from . import views
from authentication import views as auth_views

router = routers.DefaultRouter()
router.register('shopping-lists', views.ShoppingListViewSet)
router.register('items', views.ItemsInListViewSet)
router.register('users', auth_views.UsersViewSet)
# router.register('login', auth_views.MyObtainTokenPairView)


urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('authentication.urls'))
]