from rest_framework.decorators import api_view
from django.shortcuts import redirect
import os
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.response import Response
import requests
from django.contrib.auth import authenticate,logout,login
# models
from api.models import *

# serializers
from api.serializers import *

load_dotenv()
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET_ID = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT")


@api_view(["GET"])
def login_direct(request):
    SITE = f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state="Success/'
    return redirect(SITE)


# check if user is there or not
def auth(username, enrolment_number, name, year, email, is_Member):
    try:
        user = User.objects.get(username=username)
        print("Exists")
        return user

    except User.DoesNotExist:
        print("Not Exists")
        User.objects.create(
            username=username,
            name=name,
            email=email,
            year=year,
            enrolment_no=enrolment_number,
            is_Member=is_Member,
        )
        user = User.objects.get(username=username)
        return user


@api_view(["GET"])
def check_login(request):
    if "sessionid" in request.COOKIES:
        return Response("LOGGED IN")
    else:
        return Response("NOT LOGGED IN")


@api_view(["GET"])
def oauth_login(req):
    parameters = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET_ID,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        "code": req.GET.get("code", None),
    }

    res = requests.post("https://channeli.in/open_auth/token/", data=parameters)

    if res.status_code == 200:
        data = res.json()
        header = {"Authorization": "Bearer " + data["access_token"]}

        data_res = requests.get(
            "https://channeli.in/open_auth/get_user_data/", headers=header
        )

        user = data_res.json()

        # get the data from the response
        username = user["username"]
        name = user["person"]["fullName"]
        year = user["student"]["currentYear"]
        email = user["contactInformation"]["emailAddress"]
        enrolment_no = user["student"]["enrolmentNumber"]

        is_Member = False
        # check if the user has maintainer role or not
        for i in user["person"]["roles"]:
            if i["role"] == "Maintainer":
                is_Member = True
                break
        if is_Member == True:
            try:
                user = auth(username, enrolment_no, name, year, email, is_Member)
                print(user)
            except:
                return Response("unable to create user")
            try:
                req.session["username"] = username
                req.session["name"] = name
                req.session["year"] = year
                req.session["email"] = email
                req.session["enrolment_no"] = enrolment_no
                req.session["is_Member"] = is_Member
                login(req, user)
                return Response("LOGGED IN")
            except:
                return Response("Not logged in successfully")
        else:
            return Response("not img fella")


# check credentials
@api_view(['POST'])
def login(request):
   username=request.data['username']
   password=request.data['password']
   user=authenticate(request,username=username,password=password)
   if user is not None:
      login(request,user)
      request.session['username']=username
      return Response({"message":"LOGGED IN SUCCESSFULLY"})
   else:
    return Response({"message":"Check Your Credentials"})
   
@api_view(['GET'])
def logout(request):
   logout(request)
   return Response({"message":"LOGGED OUT SUCCESSFULLY"}, status=status.HTTP_200_OK)