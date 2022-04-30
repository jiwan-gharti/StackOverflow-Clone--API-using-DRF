from django.db.models import fields
from rest_framework import serializers
from .models import User, Profile

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input-type": "password"}, write_only=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "address",
            "gender",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = User(
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            gender=self.validated_data["gender"],
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must be match"})

        user.set_password(password)
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "address", "gender"]
