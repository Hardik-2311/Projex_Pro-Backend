from .userSerial import userSerializer
from .Taskserializer import taskSerializer
from rest_framework import serializers
from api.models.project import project
class projectSerializer(serializers.ModelSerializer):

    creator = userSerializer(read_only = True)
    task_set = taskSerializer(read_only = True, many = True)
    id = serializers.ReadOnlyField()
    date_created = serializers.ReadOnlyField()
    class Meta:
        model = project
        fields = [
            'id',
            'creator',
            'date_created',
            'members',
            'name',
            'wiki',
            'finished_status',
            'task_set',
        ]