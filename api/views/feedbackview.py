from rest_framework import viewsets
from api.models import feedback
from api.serializers.feedbackserializer import feedbackSerializer
from api.permissions import IsAdminToPerformFeedbackActions
from rest_framework.response import Response
from rest_framework import status, generics,viewsets

class FeedbackDetailViewSet(viewsets.ModelViewSet):
    queryset = feedback.objects.all()
    serializer_class = feedbackSerializer
# class FeedbackCreateOrListViewSet(viewsets.ModelViewSet):
#     serializer_class = feedbackSerializer
#     permission_classes = [IsAdminToPerformFeedbackActions]

#     def get_queryset(self):
#         return feedback.objects.all()

#     def perform_create(self, serializer):
#         serializer.save()


# class FeedbackDetailViewSet(viewsets.ModelViewSet):
#     serializer_class = feedbackSerializer
#     permission_classes = [IsAdminToPerformFeedbackActions]
#     lookup_url_kwarg = "feedback_id"

#     def get_queryset(self):
#         return feedback.objects.all()

#     def retrieve(self, request, *args, **kwargs):
#         queryset = feedback.objects.all()
#         goal = generics.get_object_or_404(queryset, pk=kwargs["feedback_id"])
#         serializer = feedbackSerializer(goal)
#         output = serializer.data

#         return Response(output, status=status.HTTP_200_OK)

#     def partial_update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)

#         if serializer.is_valid():
#             if instance.content != serializer.validated_data["content"]:
#                 serializer.validated_data["is_edited"] = True

#             self.perform_update(serializer)
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
