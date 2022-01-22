from django.shortcuts import render

from .models import CustomUser, Article
from django.views.generic.edit import FormView
from .forms import CustomUserRegistrationForm, Questionary1, Questionary2, Questionary3, Questionary4

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
    num = Article.objects.all().count()
    articles_list = [i.create_dict() for i in Article.objects.all()]
    return render(request, 'articles.html', {'num': num, 'articles_list': articles_list})


def questionary_view(request, data={'n': 1}):
    req = None
    form = Questionary1()
    if request.method == 'POST':
        req = request.POST
        if data['n'] == 1:
            data.update(req)
            data['n'] = 2
            form = Questionary2()
        elif data['n'] == 2:
            data.update(req)
            data['n'] = 3
            form = Questionary3()
        elif data['n'] == 3:
            data.update(req)
            data['n'] = 4
            form = Questionary4()
        elif data['n'] == 3:
            data.update(req)
            data['n'] = 4
            form = Questionary4()

    return render(request, 'questionary_base.html', context={'form': form, 'req': req, 'data': data})