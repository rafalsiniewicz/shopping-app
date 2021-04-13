from django.urls import include, path
from authentication.views import MyObtainTokenPairView, RegisterView, DeleteUserView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UsersViewSet)
# router.register('login', views.MyObtainTokenPairView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('delete/<id>', DeleteUserView.as_view(), name='auth_delete'),
]