from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Teste
from rest_framework.viewsets import ModelViewSet
from .serializer import TesteSerializer


class TesteView(ModelViewSet):
    queryset = Teste.objects.all()          
    serializer_class = TesteSerializer