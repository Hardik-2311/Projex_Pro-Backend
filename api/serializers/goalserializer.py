from .userSerial import userSerializer
from rest_framework import serializers
from api.models.goal import goal
from api.models.user import User
class goalSerializer(serializers.ModelSerializer):

    assignees = serializers.PrimaryKeyRelatedField(allow_empty = True, many = True, queryset = User.objects.all())
    creator = userSerializer(read_only = True)
    list = serializers.PrimaryKeyRelatedField(read_only = True)
    id = serializers.ReadOnlyField()
    due_date = serializers.DateField(format = '%d-%m-%Y')
    class Meta:
        model = goal
        fields = [
            'id',
            'list',
            'title',
            'desc',
            'creator',
            'assignees',
            'finished_status',
            'due_date',
        ]