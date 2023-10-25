from rest_framework import generics,viewsets
from api.serializers import *
from api.models import *


# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = project.objects.all()
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]
#     def get_queryset(self):
#         user = self.request.user
#         return user.project_set.all()

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.serializer_class(instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             creator = request.user
#             members = serializer.validated_data.get('project_members', [])
#             project = serializer.save(creator=creator)
#             project.project_members.set(members)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data)
#         if serializer.is_valid():
#             members = serializer.validated_data.get('project_members', [])
#             instance.project_members.set(members)
#             instance.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectViewSet(viewsets.ModelViewSet):
     queryset = project.objects.all()
     serializer_class = ProjectSerializer
