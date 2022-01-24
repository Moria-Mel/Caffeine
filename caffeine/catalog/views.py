from django.shortcuts import render

from .models import CustomUser, Article
from django.views.generic.edit import FormView
from .forms import CustomUserRegistrationForm, Questionary1, Questionary2, Questionary3, Questionary4, Articles_filter

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password



from django.views.generic import TemplateView


def index(request):
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
    form = Articles_filter()
    filters = None
    if request.method == 'POST':
        req = dict(request.POST)
        if 'filter_field' in req.keys():
            filters = req['filter_field']
            articles_list = [i for i in articles_list if set(i['tags']).intersection(set(filters))]
            num = len(articles_list)

    return render(request, 'articles.html', {'num': num, 'articles_list': articles_list,
                                             'form': form, 'filters': filters})


def questionary_view(request, data={'n': 1}):
    questionary_dict = {1: Questionary2(), 2: Questionary3(), 3: Questionary4(), 4: Questionary4()}
    req = None
    form = Questionary1()
    if request.method == 'POST':
        req = request.POST
        try:
            data.update(req)
            form = questionary_dict[data['n']]
            data['n'] += 1
        except KeyError:
            form = Questionary1

    return render(request, 'questionary_base.html', context={'form': form, 'req': req, 'data': data})


def article_view(request, id):
    try:
        template = Article.objects.filter(article_id=id)[0].template
    except KeyError:
        template = 'article_error'
    return render(request, f'articles/{template}.html')
