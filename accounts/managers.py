from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_("user must have phone number"))
        if not full_name:
            raise ValueError(_("user must have full name"))
        user = self.model(phone_number=phone_number, full_name=full_name)
        user.set_password((password))
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(phone_number, full_name, password, **extra_fields)

