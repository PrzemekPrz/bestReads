"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bestReads.views import (
MainView, AppView, BookAddView,
PlanAddView, BookView, PlanView,
BookPlanView, BookAddPlanView,
LoginNewView, LogoutView, AddUserView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('index/', AppView.as_view()),
    path('book_add', BookAddView.as_view(), name='book-add'),
    path('plan_add', PlanAddView.as_view(), name='plan-add'),
    path('book_add_plan', BookAddPlanView.as_view(), name='book-add-plan'),
    path('book/list/', BookView.as_view(), name="books"),
    path('plan/list/', PlanView.as_view(), name="plans"),
    path('book_plan/list/', BookPlanView.as_view(), name="book-plan"),
    path('login_new/', LoginNewView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('add_user/', AddUserView.as_view()),

]
