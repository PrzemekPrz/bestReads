from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    number_pages = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.ForeignKey('Votes', default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.ForeignKey('Votes', default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Dayname(models.Model):
    day_name = models.CharField(max_length=16)

    def __str__(self):
        return self.day_name

class BookPlan(models.Model):
    day_name = models.ForeignKey('Dayname', on_delete=models.CASCADE)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)


class Page(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Votes(models.Model):
    votes = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.votes
