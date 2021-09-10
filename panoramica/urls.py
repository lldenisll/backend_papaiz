from django.urls import path
from rest_framework import routers
from .views import PanoramicaView
from .models import Panoramica

router = routers.DefaultRouter()
router.register('panoramica',PanoramicaView,basename='Panoramica')


urlpatterns=router.urls