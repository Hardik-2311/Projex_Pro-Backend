from rest_framework import viewsets
from api.models.task import task
from api.serializers.Taskserializer import taskSerializer


# class TaskCreateOrListViewSet(generics.ListCreateAPIView):
#     serializer_class = taskSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]

#     def get_queryset(self):
#         return task.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)

# class TaskDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = taskSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]
#     lookup_url_kwarg = 'task_id'
#     http_method_names = ['get', 'post', 'head', 'patch', 'delete']

#     def get_queryset(self):
#         return task.objects.all()

#     def retrieve(self, request, *args, **kwargs):
#         queryset = task.objects.all()
#         task_instance = generics.get_object_or_404(queryset, pk=self.kwargs['task_id'])
#         serializer = taskSerializer(task_instance)
#         res_dict = serializer.data
#         res_dict['creator'] = userSerializer(task_instance.creator).data
#         return Response(res_dict, status=status.HTTP_200_OK)
class TaskDetailViewSet(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = taskSerializer