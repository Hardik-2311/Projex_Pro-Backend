from rest_framework import viewsets
from api.models import feedback
from api.serializers import feedbackSerializer
from api.permissions import IsAdminToPerformFeedbackActions
from rest_framework.response import Response
from rest_framework import status
class FeedbackCreateOrListViewSet(viewsets.ModelViewSet):
    serializer_class = feedbackSerializer
    permission_classes = [IsAdminToPerformFeedbackActions]

    def get_queryset(self):
        return feedback.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class FeedbackDetailViewSet(viewsets.ModelViewSet):
    serializer_class = feedbackSerializer
    permission_classes = [IsAdminToPerformFeedbackActions]
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return feedback.objects.all()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            if instance.content != serializer.validated_data['content']:
                serializer.validated_data['is_edited'] = True

            self.perform_update(serializer)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
