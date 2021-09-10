from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Panoramica
from rest_framework.viewsets import ModelViewSet
from .serializer import PanoramicaSerializer


class PanoramicaView(ModelViewSet):
    queryset = Panoramica.objects.all()          
    serializer_class = PanoramicaSerializer