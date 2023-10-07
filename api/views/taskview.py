from rest_framework import generics
from api.models.task import task
from api.serializers.Taskserializer import taskSerializer
from api.serializers.userSerial import userSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class taskCreateOrListViewSet(generics.ListCreateAPIView):
    serializer_class = taskSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return task.objects.filter(project__id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        project = project.objects.get(id=project_id)
        serializer.save(creator=self.request.user, project=project)

class taskDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = taskSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_url_kwarg = 'task_id'
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return task.objects.filter(project__id=project_id)

    def retrieve(self, request, *args, **kwargs):
        queryset = task.objects.all()
        task = generics.get_object_or_404(queryset, pk=self.kwargs['task_id'])
        serializer = taskSerializer(task)
        res_dict = serializer.data
        res_dict['creator'] = userSerializer(task.creator).data
        res_dict['project_creator'] = userSerializer(task.project.creator).data
        return Response(res_dict, status=status.HTTP_200_OK)
