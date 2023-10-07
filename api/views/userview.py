from rest_framework import viewsets
from api.models import *
from api.serializers.userSerial import userSerializer
from rest_framework.permissions import IsAuthenticated
from api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()
