from rest_framework import serializers
from .userSerial import userSerializer
from api.models.feedback import feedback
class feedbackSerializer(serializers.ModelSerializer):

    commentor = userSerializer(read_only = True)
    id = serializers.ReadOnlyField()
    is_edited = serializers.ReadOnlyField()

    class Meta:
        model = feedback
        fields = [
            'id',
            'commentor',
            'content',
            'timestamp',
            'is_edited',
        ]