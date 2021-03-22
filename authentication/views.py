from django.http import Http404
from rest_framework import generics, permissions
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, DeleteSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import viewsets

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DeleteSerializer
    lookup_field = 'username'