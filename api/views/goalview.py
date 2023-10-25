from rest_framework import generics, status,viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.models.goal import goal as Goal
from api.serializers.goalserializer import goalSerializer

# class GoalCreateOrList(generics.ListCreateAPIView):
#     serializer_class = goalSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser] 

#     def get_queryset(self):
#         return Goal.objects.all()

#     def perform_create(self, serializer):
      
#         serializer.save()

# class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = goalSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]
#     lookup_url_kwarg = 'goal_id'
#     http_method_names = ['get', 'head', 'patch', 'delete']

#     def get_queryset(self):
#         return Goal.objects.all()

#     def retrieve(self, request, *args, **kwargs):
#         queryset = Goal.objects.all()
#         goal = generics.get_object_or_404(queryset, pk=kwargs['goal_id'])
#         serializer = goalSerializer(goal)
#         output = serializer.data

#         return Response(output, status=status.HTTP_200_OK)

#     def partial_update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.serializer_class(instance, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return super().partial_update(request, *args, **kwargs)

#         return super().partial_update(request, *args, **kwargs)
class GoalDetail(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = goalSerializer