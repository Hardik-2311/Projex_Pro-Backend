from django import urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.projectview import ProjectViewSet
from api.views.userview import UserViewSet
from api.views.taskview import TaskCreateOrListViewSet,TaskDetailViewSet
from api.views.goalview import GoalCreateOrList,GoalDetail
from api.views.feedbackview import FeedbackCreateOrListViewSet,FeedbackDetailViewSet
from api.views.oauth import login_direct,logout
app_name = "ProjexPro"

my_view = FeedbackCreateOrListViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
my_view2 = FeedbackDetailViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
route1 = DefaultRouter()
route1.register(r"projects", ProjectViewSet, basename="project")

route2 = DefaultRouter()
route2.register(r"user",UserViewSet, basename="user")
urlpatterns = [
    path('',include(route2.urls)),
    path('',include(route1.urls)),
    path('login',login_direct),
    path('task/',TaskCreateOrListViewSet.as_view()),
    path('task/<int:task_id>/',TaskDetailViewSet.as_view()),
    path('goal/',GoalCreateOrList.as_view()),
    path('goal/<int:goal_id>/',GoalDetail.as_view()),
    path('feedback/',my_view),
    path('feedback/<int:feedback_id>/',my_view2),
    path('logout',logout)

]