from django.contrib.auth.base_user import BaseUserManager
#from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):

        if not email:
            raise ValueError('Email must be set')
        if not username:
            raise ValueError('Username must be set')
        #email = self.normalize_email(email)
        user = self.model(email=email, username=username **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)