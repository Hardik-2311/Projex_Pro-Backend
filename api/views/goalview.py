from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from api.permissions import IsSessionAuthenticated
from api.models.goal import goal
from api.serializers.goalserializer import goalSerializer


class GoalDetail(viewsets.ModelViewSet):
    queryset = goal.objects.all()
    serializer_class = goalSerializer
    permission_classes = [IsSessionAuthenticated]
    lookup_url_kwarg = "id"
    http_method_names = ["get", "put", "patch", "delete", "post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        goal = self.get_object()
        serializer = self.get_serializer(goal)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        goal = self.get_object()
        serializer = self.get_serializer(goal, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        goal = self.get_object()
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
