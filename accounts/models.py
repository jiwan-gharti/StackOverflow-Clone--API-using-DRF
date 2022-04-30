from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.utils import timezone

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    object = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default="default.jpg",
        null=True,
        upload_to="profile_images",
        verbose_name="Avatar",
    )
    bio = models.TextField(null=True, verbose_name="biography")
    auth_token = models.UUIDField(max_length=100, null=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        ordering = ["date_joined"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.email
