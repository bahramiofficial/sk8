from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    USER = 'user'
    COCHE = 'coche'
    ADMIN = 'admin'
    LEVEL_TYPE = (
        (USER, "user"),
        (COCHE, "coche"),
        (ADMIN, "admin"),
    )

    mobile = models.CharField('mobile',max_length=11, unique=True)
    level = models.CharField('level', choices=LEVEL_TYPE ,default=USER,max_length=11)
    maker = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,default=None)

    username = models.CharField(
       "username",
        max_length=150,
        help_text=
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ,
        error_messages={
            "unique": "A user with that username already exists.",
        },
      blank = True, null = True, default = None
    )

    email = models.EmailField("email address", blank=True, null=True,default=None)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = [""]








    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'