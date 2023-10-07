from rest_framework import viewsets
from api.models import *
from api.serializers.userSerial import userSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from api.serializers import *
from rest_framework.response import Response


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_details(req):

    user_obj = req.user
    serialized = userSerial(user_obj)
    res_dict = serialized.data
    return Response(res_dict)
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.all()
