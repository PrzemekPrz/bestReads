from django import forms
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from .models import Book, Plan, BookPlan, Dayname, Votes

class BookAddForm(forms.Form):
    name = forms.CharField(label='Nazwa')
    description = forms.CharField(label='Opis')
    author = forms.CharField(label='Autor')
    isbn = forms.IntegerField(label='Isbn')
    number_pages = forms.IntegerField(label='Strony')
    votes = forms.ModelChoiceField(queryset=Votes.objects.all(), label='ocena')

class PlanAddForm(forms.Form):
    name = forms.CharField(label='Nazwa')
    description = forms.CharField(label='Opis')
    votes = forms.ModelChoiceField(queryset=Votes.objects.all(), label='ocena')

class BookAddPlanForm(forms.Form):
    plan = forms.ModelChoiceField(queryset=Plan.objects.all(), label='Nazwa planu')
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label='Nazwa ksiązki')
    day = forms.ModelChoiceField(queryset=Dayname.objects.all(), label='Dzień')


class LoginForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

def login_not_taken(login):
    if User.objects.filter(username=login):
        raise ValidationError('Podany login jest zajęty')

class RegisterForm(forms.Form):
    login = forms.CharField(label='Login', validators=[login_not_taken])
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz Hasło', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Imie')
    last_name = forms.CharField(label='Nazwisko')
    email = forms.CharField(label='E-mail')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Podane hasla nie są takie same')
        return cleaned_data


