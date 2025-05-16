
from django.utils.translation import gettext as _
from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_('Users must have a phone number'))

        user = self.model(
            phone_number=phone_number,
            full_name=full_name,
            **extra_fields
        )

        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError(_('Superuser must have is_admin=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        user = self.create_user(
            phone_number,
            full_name,
            password=password,
            **extra_fields
        )
        return user