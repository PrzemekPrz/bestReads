from django.contrib import admin
from .models import Book, Plan, BookPlan, Dayname
# Register your models here.
admin.site.register(Book)
admin.site.register(Plan)
admin.site.register(BookPlan)
admin.site.register(Dayname)