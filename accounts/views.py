from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import User, Profile
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import uuid
from django.contrib.auth import authenticate, login
from accounts import serializers

# Create your views here.
class RegisterView(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        email = data.get("email")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user, auth_token=auth_token)
            profile_obj.save()
            send_mail_registration(email, auth_token)
            return Response(
                {"msg": "we have sent mail to your gamil account confirm it"}
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


# send mail function
def send_mail_registration(email, token):
    subject = "Verify your accounts "
    message = f"Hi click on  the link to verify your account http://127.0.0.1:8000/api/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(auth_token=token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(
                    request, "Your account is already verified.please login"
                )
            profile_obj.is_verified = True
            profile_obj.save()
            return redirect("/api/login/")
        else:
            return Response({"msg": "token doesnot match and check your mail"})
    except Exception as e:
        print(e)


class LoginView(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        email = data.get("email")
        password = data.get("password")
        print(email, password)
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return redirect("/profile/")
                return Response({"msg": "User Login "})

        return Response({"msg": "email and password didnot match"})


class ProfileView(viewsets.ViewSet):
    def create(self, request):
        return Response({"msg": "created"})
