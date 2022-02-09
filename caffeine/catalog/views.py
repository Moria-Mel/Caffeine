from django.shortcuts import render

from .models import CustomUser, Article, QuestionsModel
from django.views.generic.edit import FormView
from .forms import CustomUserRegistrationForm, Questionary1, Questionary2, Questionary3, Questionary4, Articles_filter

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
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
    questionaries = QuestionsModel.objects.all()

    def get_stat(column, value):
        if column == 'gender':
            return len(questionaries.filter(gender=value))
        elif column == 'job':
            return len(questionaries.filter(job=value))
        elif column == 'age':
            pass
        elif column == 'symptoms':
            res = ''.join([i.symptoms for i in questionaries])
            res = {int(i): res.count(i) for i in '123456'}
            return res

    stat_data = [('male', get_stat('gender', 'M')), ('female', get_stat('gender', 'F')), ('Sc', get_stat('job', 'Sc')),
                 ('St',  get_stat('job', 'St')), ('T',  get_stat('job', 'T')), ('O',  get_stat('job', 'O'))]

    stat1 = get_stat('symptoms', 0)
    stat_data += [('symp' + str(i), stat1[i]) for i in stat1.keys()]
    
    return render(request, 'statistic.html', context={'stat_data': stat_data})


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


@login_required
def questionary_view(request, data={'n': 1}):
    questionary_dict = {1: Questionary2(), 2: Questionary3(), 3: Questionary4(), 4: Questionary4()}
    req = None
    form = Questionary1()
    if request.method == 'POST':
        req = request.POST
        if data['n'] == 5:
            # user_id=request.user in QuestionsModel
            questionary = QuestionsModel(gender=data['gender'][0],
                                         age=int(data['age'][0]),
                                         job=data['job'][0], instant_coffee=int(data['instant_coffee'][0]),
                                         grain_coffee=int(data['grain_coffee'][0]), tea=int(data['tea'][0]),
                                         energy_drinks=int(data['energy_drinks'][0]), pills=int(data['pills'][0]),
                                         addiction1=int(data['addiction1'][0]),
                                         addiction2=int(data['addiction2'][0]),
                                         addiction3=int(data['addiction3'][0]),
                                         symptoms=''.join([str(i) for i in data['symptoms']]))
            questionary.save()
            data = {}
            data['n'] = 1
        else:
            try:
                data.update(req)
                form = questionary_dict[data['n']]
                data['n'] += 1
            except KeyError:
                form = Questionary1()

    return render(request, 'questionary_base.html', context={'form': form, 'req': req, 'data': data})


def article_view(request, id):
    try:
        template = Article.objects.filter(article_id=id)[0].template
    except KeyError:
        template = 'article_error'
    return render(request, f'articles/{template}.html')
