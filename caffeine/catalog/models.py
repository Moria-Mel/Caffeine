from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin


class QuestionsModel(models.Model):
    user_id = models.CharField(max_length=30, help_text='Username')
    question_1 = models.BooleanField(help_text='Do you have a caffeine addiction?')

    class Meta:
        pass

    def __str__(self):
        return self.user_id

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    last_login = False
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    questions = models.BooleanField(null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    class Meta:
        pass

    def __str__(self):
        return self.username


    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    summary = models.TextField(null=True)
    tags = models.TextField(null=True)
    template = models.TextField(default='base_article')

    class Meta:
        pass

    def create_dict(self):
        return {'title': self.title, 'tags': [i.capitalize() for i in self.tags.split()],
                'summary': self.summary}

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.article_id)])


