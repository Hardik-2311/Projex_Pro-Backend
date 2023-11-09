from django import urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.projectview import ProjectViewSet
from api.views.userview import UserViewSet
from api.views.taskview import TaskDetailViewSet
from api.views.goalview import GoalDetail
from rest_framework import routers
from api.views.feedbackview import FeedbackDetailViewSet
from api.views.oauth import login_direct
from django.urls import path
from api.views.oauth import oauth_login,check_login,login,logout_direct
app_name = "ProjexPro"
router = routers.DefaultRouter()
router.register("users",UserViewSet)
router.register("task", TaskDetailViewSet)
router.register("goal", GoalDetail)
router.register("projects", ProjectViewSet)
router.register("feedback", FeedbackDetailViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("login/",login_direct,name="login_direct"),
    path('logout/', logout_direct, name='logout_direct'),
    path('check_login/', check_login, name='check_login'),
    
]
