from django.shortcuts import render

from .models import CustomUser, Article
from django.views.generic.edit import FormView
from .forms import CustomUserRegistrationForm, Questionary1, Questionary2, Questionary3

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password



from django.views.generic import TemplateView


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_users = CustomUser.objects.all().count()
    num_articles = Article.objects.all().count()

    return render(
        request,

        'index.html',
        context={'num_users': num_users, 'num_articles': num_articles},
    )


def registration_view(request):
    form = CustomUserRegistrationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = make_password(form.cleaned_data.get('password'))
        email = form.cleaned_data.get('email')
        user = CustomUser(username=username, password=password, email=email)
        user.save()
        return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form

})


def statistic_view(request):
    return render(request, 'statistic.html')


def articles_view(request):
    return render(request, 'articles.html')


def questionary_view(request, data={}):
    form = Questionary1()
    req = None
    if request.method == 'POST':
        req = request.POST
        if form.numb == 1:
            data.update(req)
            form = Questionary2()
        elif form.numb == 2:
            data.update(req)
            form = Questionary3()
        elif form.numb == 3:
            data.update(req)

    return render(request, 'questionary_base.html', context={'form': form, 'req': req, 'data': data})