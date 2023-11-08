from django import urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.projectview import ProjectViewSet
from api.views.userview import UserViewSet
from api.views.taskview import TaskDetailViewSet
from api.views.goalview import GoalDetail
from rest_framework import routers
from api.views.feedbackview import FeedbackDetailViewSet
from api.views.oauth import login_direct, logout

app_name = "ProjexPro"
router = routers.DefaultRouter()
router.register("task", TaskDetailViewSet)
router.register(
    "goal",
    GoalDetail
)
router.register("projects", ProjectViewSet)
router.register("feedback", FeedbackDetailViewSet)

# my_view2 = FeedbackDetailViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


# route2 = DefaultRouter()
# route2.register(r"user",UserViewSet, basename="user")
# urlpatterns = [
#     path('',include(route2.urls)),
#     path('projects/',ProjectViewSet.as_view({'get': 'list',
#     'post': 'create',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'}),),

#     path('login',login_direct),
#     path('task/',TaskDetailViewSet.as_view({'get': 'list',
#     'post': 'create',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'})),
#     path('goal/',GoalDetail.as_view({'get': 'list',
#     'post': 'create',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'})),
#     path('feedback/',my_view2),
#     path('logout',logout)

urlpatterns = [
    path("", include(router.urls)),
    path("user",UserViewSet.as_view({'get': 'list'}),name="user"),
    path("login", login_direct),
    path("logout", logout),
]
