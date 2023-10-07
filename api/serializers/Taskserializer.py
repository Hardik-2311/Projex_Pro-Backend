from rest_framework import serializers
from api.models.task import task
from .goalserializer import goalSerializer
class taskSerializer(serializers.ModelSerializer):

    project = serializers.PrimaryKeyRelatedField(read_only = True)
    creator = serializers.PrimaryKeyRelatedField(read_only = True)
    goal_set = goalSerializer(read_only = True, many = True)
    id = serializers.ReadOnlyField()
    time_stamp = serializers.ReadOnlyField()
    class Meta:
        model = task
        fields = [
            'id',
            'project',
            'title',
            'creator',
            'time_stamp',
            'finished_status',
            'goal_set',
        ]