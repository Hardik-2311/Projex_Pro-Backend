from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
import requests
from rest_framework import status
from dotenv import load_dotenv
from api.models import User
from rest_framework.response import Response

import os

load_dotenv()
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET_ID = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT")


@api_view(["GET"])
@authentication_classes([])  # Exclude authentication
@permission_classes([])  # Exclude permission checks
def login_direct(request):
    SITE = f"https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state=Success"
    return redirect(SITE)


# check if user is there or not
def auth(username, enrolment_number, year, email, is_Member):
    try:
        user = User.objects.get(username=username)
        print("Exists")
        return user
    except User.DoesNotExist:
        print("Not Exists")
        user = User(
            username=username,
            email=email,
            year=year,
            enrolment_no=enrolment_number,
            is_member=is_Member,
        )
        user.save()
        return user


@api_view(["GET"])
@authentication_classes([])  # Exclude authentication
@permission_classes([])  # Exclude permission checks
def check_login(request):
    if request.user.is_authenticated:
        return Response("LOGGED IN")
    else:
        return Response("NOT LOGGED IN")


@api_view(["GET"])
@authentication_classes([SessionAuthentication])  # Exclude authentication
@permission_classes([IsAuthenticated])  # Exclude permission checks
def oauth_login(request):
    code = request.GET.get("code")
    if not code:
        return Response("Missing authorization code", status=400)

    parameters = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET_ID,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }

    res = requests.post("https://channeli.in/open_auth/token/", data=parameters)

    if res.status_code == 200:
        data = res.json()
        access_token = data.get("access_token")

        if not access_token:
            return Response("Access token not received", status=400)

        header = {"Authorization": f"Bearer {access_token}"}
        data_res = requests.get(
            "https://channeli.in/open_auth/get_user_data/", headers=header
        )

        if data_res.status_code == 200:
            user_data = data_res.json()
            username = user_data["person"]["fullname"]
            enrolment_no = user_data["student"]["enrolmentNumber"]
            year = user_data["student"]["currentYear"]
            email = user_data["contactInformation"]["emailAddress"]
            is_Member = any(
                role["role"] == "Maintainer" for role in user_data["person"]["roles"]
            )

            user = auth(username, enrolment_no, year, email, is_Member)
            if user:
                login(request, user)
                request.session["username"]=username
                request.session["year"] = year
                request.session["email"] = email
                request.session["enrolment_no"] = enrolment_no
                request.session["is_Member"] = is_Member
                return redirect("http://127.0.0.1:3000/users/")

            else:
                return Response(
                    "Unable to create user", status=status.HTTP_INTERNAL_SERVER_ERROR
                )
        else:
            return Response("Unable to fetch user data from Channeli", status=400)
    else:
        return Response("OAuth token request failed", status=400)


# check credentials
@api_view(["POST"])
@authentication_classes([])  # Exclude authentication
@permission_classes([])  # Exclude permission checks
def login(request):
    name = request.data.get("name")
    password = request.data.get("password")
    user = authenticate(request, username=name, password=password)
    if user is not None:
        login(request, user)
        request.session["name"] = name
        return Response({"message": "LOGGED IN SUCCESSFULLY", "data": name})
    else:
        return Response({"message": "Check Your Credentials"}, status=400)


@api_view(["GET"])
@authentication_classes([])  # Exclude authentication
@permission_classes([])  # Exclude permission checks
def logout_direct(request):
    logout(request)
    return Response({"message": "LOGGED OUT SUCCESSFULLY"}, status=status.HTTP_200_OK)