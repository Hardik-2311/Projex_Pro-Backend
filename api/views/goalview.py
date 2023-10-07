from rest_framework import viewsets
from api.models import goal
from api.serializers import goalSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdminToCreateGoal

class GoalViewSet(viewsets.ModelViewSet):

    queryset = goal.objects.all()
    serializer_class = goalSerializer
    permission_classes = [IsAuthenticated, IsAdminToCreateGoal]
