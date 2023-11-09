from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from api.models.user import User
from api.serializers.userSerial import userSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        year = request.data.get("year")
        email = request.data.get("email")
        enrolment_no = request.data.get("enrolment_no")
        is_Member = request.data.get("is_Member")

        # Check if the user already exists or create a new one
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "username": username,
                "year": year,
                "email": email,
                "enrolment_no": enrolment_no,
                "is_Member": is_Member,
            }
        )

        # Perform login for the user
        if created or not request.user.is_authenticated:
            login(request, user)

        # Serialize the user and return the response
        serializer = userSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
