from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Article, QuestionsModel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']
    list_filter = []  # Спорное решение


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)
admin.site.register(QuestionsModel)
