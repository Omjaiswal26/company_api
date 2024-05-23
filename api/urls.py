from django.contrib import admin 
from django.urls import path , include
from .views import CompanyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',viewset=CompanyViewSet)

urlpatterns = [
    path('' , include(router.urls))
]
