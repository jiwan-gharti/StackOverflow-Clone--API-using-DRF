from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("accounts", views.RegisterView, basename="register_account")
router.register("login", views.LoginView, basename="login")
router.register("profile/", views.ProfileView, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
    path("verify/<str:token>/", views.verify, name="verify"),
    path("login/", views.LoginView, name="login"),
    path("profile/", views.ProfileView.as_view, name="profile"),
]
