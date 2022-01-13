from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [path('register/', views.registration_view, name="registration")]