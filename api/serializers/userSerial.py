from rest_framework import serializers
from api.models.user import *

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'