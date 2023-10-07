from rest_framework import generics
from api.models.task import task
from api.serializers.Taskserializer import taskSerializer
from api.serializers.userSerial import userSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class TaskCreateOrListViewSet(generics.ListCreateAPIView):
    serializer_class = taskSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return task.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class TaskDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = taskSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_url_kwarg = 'task_id'
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_queryset(self):
        return task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = task.objects.all()
        task_instance = generics.get_object_or_404(queryset, pk=self.kwargs['task_id'])
        serializer = taskSerializer(task_instance)
        res_dict = serializer.data
        res_dict['creator'] = userSerializer(task_instance.creator).data
        return Response(res_dict, status=status.HTTP_200_OK)
