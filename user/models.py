from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_superuser(self, username, nickname, email, phone, password,
                         **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'you must an assigned is_superuser=True'
            )
        if other_fields.get('is_staff') is not True:
            raise ValuError(
                'you must an assigned is_staff=True'
            )
        return self.create_user(username, nickname, email, phone, password,
                                **other_fields)

    def create_user(self, username, nickname, email, phone, password,
                    **other_fields):

        if not username:
            raise ValueError(
                _('you must provide username')
            )

        if not nickname:
            raise ValueError(
                _('you must provide nickname')
            )

        if not email:
            raise ValueError(
                _('you must provide nickname')
            )
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            nickname=nickname,
            email=email,
            phone=phone,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='user/', blank=True)
    username = models.CharField(_('username'), max_length=20, unique=True)
    nickname = models.CharField(_('Nickname'), max_length=50)
    first_name = models.CharField(_('First name'), max_length=25, blank=True)
    last_name = models.CharField(_('Last name'), max_length=25, blank=True)
    email = models.CharField(_('Email address'), max_length=50, unique=True)
    phone = models.CharField(_('Phone number'), max_length=15, unique=True)
    github = models.CharField(_('Github account'), max_length=150, blank=True)
    bio = models.CharField(_('Bio'), max_length=250, blank=True)
    date_join = models.DateTimeField(auto_now_add=timezone.now, editable=False)

    # TODO skills, Address_line, follow_tags, Fix Phone Number

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname', 'email', 'phone']

    def __str__(self):
        return self.username
