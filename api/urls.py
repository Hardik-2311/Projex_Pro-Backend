from django import urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.projectview import ProjectViewSet
from api.views.userview import UserViewSet
from api.views.oauth import login_direct
app_name = "ProjexPro"

r1 = DefaultRouter()
r1.register(r"projects", ProjectViewSet, basename="project")

r2 = DefaultRouter()
r2.register(r"user",UserViewSet, basename="user")
urlpatterns = [
    path('',include(r2.urls)),
    path('',include(r1.urls)),
    path('login',login_direct),
    
]