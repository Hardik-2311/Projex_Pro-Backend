from rest_framework import serializers
from api.models.goal import goal
class goalSerializer(serializers.ModelSerializer):
   class Meta:
      model=goal
      fields='__all__' 