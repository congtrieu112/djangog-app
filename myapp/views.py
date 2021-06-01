from rest_framework import permissions
from myapp.models import ProductHistory
from django.shortcuts import render
from rest_framework.permissions import AllowAny

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ProductSerializer, RegisterSerializer
from rest_framework import generics

class TestAPIView(APIView):

    def get(self, request):
        return Response('ok')

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ProducView(generics.CreateAPIView):
    queryset = ProductHistory.objects.all()
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = ProductSerializer

class ListProducView(generics.ListAPIView):
    queryset = ProductHistory.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductHistory.objects.all()
    serializer_class = ProductSerializer