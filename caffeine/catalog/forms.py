from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'password')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class Questionary(forms.Form):
    numb = 0
    comment = ''

    def get_data(self):
        data = self.cleaned_data
        return data


class Questionary1(Questionary):
    gender = forms.ChoiceField(choices=(('M', 'Мужчина'), ('F', 'Женщина')), label='Пол')
    age = forms.IntegerField(min_value=5, max_value=100, label='Возраст')
    job = forms.ChoiceField(choices=(('Sc', 'Школьник'), ('St', 'Студент'),
                                         ('T', 'Преподаватель'), ('O', 'Другое')), label='Род деятельности')

    numb = 1
    comment = 'Укажите свои данные'


class Questionary2(Questionary):
    default_choice = [('0', 'Почти никогда'), ('1', 'Единожды в месяц или реже'),
                                                ('2', 'Несколько раз в месяц'), ('3', ' 2 - 3 раза в неделю'),
                                                ('4', 'Ежедневно'), ('5', 'Несколько раз в день')]
    instant_coffee = forms.ChoiceField(choices=default_choice,
                                       label='Растворимый кофе')
    grain_coffee = forms.ChoiceField(choices=default_choice, label='Зерновой кофе')
    tea = forms.ChoiceField(choices=default_choice, label='Чай')
    energy_drinks = forms.ChoiceField(choices=default_choice, label='Энергетические напитки')
    pills = forms.ChoiceField(choices=default_choice, label='Кофеиносодержащие БАДы или медецинские препараты')

    numb = 2
    comment = 'Какие из этих источников кофеина и с какой передичностью Вы используете?'


class Questionary3(Questionary):
    default_choice = [('0', 'Никогда'), ('1', 'Иногда'), ('2', 'Часто'), ('3', 'Каждый день')]

    addiction1 = forms.ChoiceField(label='Употребляете ли вы кофеин, чтобы лучше справиться с учебными или рабочими задачами?',
                                   choices=default_choice)
    addiction2 = forms.ChoiceField(label='Употребляете ли вы кофеин, чтобы проснуться утром?',
                                   choices=default_choice)
