from rest_framework import serializers
from api.models.project import project
class ProjectSerializer(serializers.ModelSerializer):
   class Meta:
      model=project
      fields='__all__'     
