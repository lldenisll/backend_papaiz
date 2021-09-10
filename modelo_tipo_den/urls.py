from django.urls import path
from rest_framework import routers
from .views import TesteView
from .models import Teste

router = routers.DefaultRouter()
router.register('teste-denticao',TesteView,basename='Teste')


urlpatterns=router.urls