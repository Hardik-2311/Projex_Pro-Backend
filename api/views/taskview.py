from rest_framework import viewsets, status
from api.models import task, project
from rest_framework.response import Response
from api.serializers import taskSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsMemberAdminCreator 

class TaskViewSet(viewsets.ModelViewSet):

    queryset = task.objects.all()
    serializer_class = taskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsMemberAdminCreator]

    def create(self, request, *args, **kwargs):
        current_user = request.user
        project_id = request.data.get('id')
        current_project = project.objects.get(pk=project_id)

        if current_user.is_superuser or current_project.project_members.filter(username=current_user.username).exists() or current_project.creator == current_user:
            serializer = taskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(creator=current_user, project=current_project)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"error": "You don't have access to create a task in this project."}, status=status.HTTP_403_FORBIDDEN)
