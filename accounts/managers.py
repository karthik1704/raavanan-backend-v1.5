from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, **kwargs):
        if not email:
            raise ValueError("User must have email address.")

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None, **kwargs):
        user = self.create_user(
            email,
            phone,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomerManager(models.Manager):
    def create_user(self, email, phone, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required !")

        email = email.lower()
        user = self.model(email=email, phone=phone)
        if not password:
            user.set_unusable_password()

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_customer=True)
        return queryset


class SellerManager(models.Manager):
    def create_user(self, email, phone, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required !")

        email = email.lower()
        user = self.model(email=email, phone=phone)
        if not password:
            user.set_unusable_password()

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_seller=True)
        return queryset


class StaffManager(models.Manager):
    def create_user(self, email, phone, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required !")

        email = email.lower()
        user = self.model(email=email, phone=phone)
        if not password:
            user.set_unusable_password()

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_staff=True)
        return queryset
