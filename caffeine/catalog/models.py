from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class QuestionsModel(models.Model):
    user_id = models.CharField(max_length=30, help_text='Username')
    question_1 = models.BooleanField(help_text='Do you have a caffeine addiction?')

    class Meta:
        pass

    def __str__(self):
        return self.user_id

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


class CustomUser(AbstractUser):
    last_login = None
    date_joined = None
    is_active = None
    is_staff = None
    first_name = None
    last_name = None
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    questions = models.BooleanField(null=True)

    class Meta:
        pass

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    summary = models.TextField()
    links = models.TextField(null=True)

    class Meta:
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.article_id)])


