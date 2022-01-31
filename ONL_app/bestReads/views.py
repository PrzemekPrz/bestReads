from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Plan, Book, BookPlan
from .forms import BookAddForm, PlanAddForm, BookAddPlanForm, LoginForm, RegisterForm

# Create your views here.
class MainView(View):
    """
    Class displays the main page
    """
    def get(self, request):
        return render(request, 'bestReads/base.html')

class AppView(LoginRequiredMixin, View):
    """
    Class displays the main page of the app
    """
    def get(self, request):
        book_count = Book.objects.count()
        plan_count = Plan.objects.count()
        return render(request, 'bestReads/index.html', {"book_count": book_count, "plan_count": plan_count})

class BookAddView(View):
    """
    Class display add book view of the app
    """
    def get(self, request):
        form = BookAddForm
        return render(request, 'bestReads/add_book.html', {'form': form})

    def post(self, request):
        form = BookAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            author = form.cleaned_data['author']
            isbn = form.cleaned_data['isbn']
            number_pages = form.cleaned_data['number_pages']
            votes = form.cleaned_data['votes']
            Book.objects.create(name=name, description=description, author=author,
                                isbn=isbn, number_pages=number_pages, votes=votes)
            return redirect(f'/book/list/')
        else:
            return render(request, 'bestReads/add_book.html', {'form': form})

class PlanAddView(View):
    """
    Class display add plan view of the app
    """
    def get(self, request):
        form = PlanAddForm
        return render(request, 'bestReads/add_plan.html', {'form': form})

    def post(self, request):
        form = PlanAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            votes = form.cleaned_data['votes']
            Plan.objects.create(name=name, description=description, votes=votes)
            return redirect(f'/plan/list/')
        else:
            return render(request, 'bestReads/add_plan.html', {'form': form})


class BookAddPlanView(View):
    """
    Class display add book to plan view of the app
    """
    def get(self, request):
        form = BookAddPlanForm
        return render(request, 'bestReads/book_add_plan.html', {'form': form})

    def post(self, request):
        form = BookAddPlanForm(request.POST)
        if form.is_valid():
            plan = form.cleaned_data['plan']
            book = form.cleaned_data['book']
            day = form.cleaned_data['day']
            BookPlan.objects.create(plan=plan, book=book, day_name=day)
            return redirect(f'/book_plan/list')
        else:
            return render(request, 'bestReads/book_add_plan.html', {'form': form})

class BookView(View):
    """
    Class displays list of books in the app
    """
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'bestReads/books.html', {"books": books})


class PlanView(View):
    """
    Class displays list of plans in the app
    """
    def get(self, request):
        plans = Plan.objects.all()
        return render(request, 'bestReads/plans.html', {"plans": plans})


class BookPlanView(View):
    """
    Class displays plans with book in the app
    """
    def get(self, request):
        booksplans = BookPlan.objects.all()
        return render(request, 'bestReads/booksplans.html', {"booksplans": booksplans})


class LoginNewView(View):
    """
    Class displays login in the app
    """
    def get(self, request):
        form = LoginForm()
        return render(request, 'bestReads/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        form.is_valid()
        user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'bestReads/login.html', {'form': form, 'message': 'Błędny login lub hasło'})


class LogoutView(View):
    """
    Class displays logout in the app
    """
    def get(self, request):
        logout(request)
        return redirect('/')


class AddUserView(View):
    """
    Class displays add user in the app
    """
    def get(self, request):
        form = RegisterForm()
        return render(request, 'bestReads/add_user.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password1']
            name = form.cleaned_data['first_name']
            surname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            User.objects.create_user(username=login, email=email, password=password, first_name=name, last_name=surname)
            return render(request, 'bestReads/base.html', {'msg': "Dodano nowego użytkownika"})
        else:
            return render(request, 'bestReads/add_user.html', {'form': form})