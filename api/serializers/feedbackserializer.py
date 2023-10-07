from rest_framework import serializers
from api.models.feedback import feedback


class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = "__all__"
