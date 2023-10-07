from rest_framework import serializers
from api.models.user import User
class userSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(read_only = True)
    full_name = serializers.ReadOnlyField()
    display_picture = serializers.ReadOnlyField()
    enrolment_number = serializers.ReadOnlyField()
    online_status = serializers.ReadOnlyField()
    email = serializers.EmailField(read_only = True)
    class Meta:
        model = User
        fields = [
            'user_id',
            'full_name', 
            'display_picture', 
            'enrolment_number', 
            'user_type',
            'online_status',
            'is_disabled',
            'email',
        ]