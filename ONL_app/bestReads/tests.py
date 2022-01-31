from django.test import TestCase, Client
import pytest
from .models import Book, Plan, BookPlan

# Create your tests here.

@pytest.mark.django_db
def test_main_page():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_add(client, votes):
    response = client.post(f'/book_add', {'name': 'Potop',
                                           'description': 'Książka o kmicicu',
                                           'author': 'Henryk Sienkiewicz',
                                           'isbn': '9780870520044',
                                           'number_pages': '936',
                                           'votes': votes.id})
    assert response.status_code == 302
    book = Book.objects.get(name='Potop')
    assert book.description == 'Książka o kmicicu'
    assert book.author == 'Henryk Sienkiewicz'
    assert book.isbn == '9780870520044'
    assert book.number_pages == 936
    assert book.votes == votes


@pytest.mark.django_db
def test_plan_add(client, votes):
    response = client.post(f'/plan_add', {'name': 'Intensywny plan',
                                           'description': 'Chce przeczytać dwie ksiązki w poniedziałek',
                                           'votes': votes.id})
    assert response.status_code == 302
    plan = Plan.objects.get(name='Intensywny plan')
    assert plan.description == 'Chce przeczytać dwie ksiązki w poniedziałek'
    assert plan.votes == votes


@pytest.mark.django_db
def test_book_add_plan(client, book, plan, day_name):
    response = client.post(f'/book_add_plan', {'book': book.id,
                                           'day': day_name.id,
                                           'plan': plan.id})
    print(response.content)
    assert response.status_code == 302
    bookplan = BookPlan.objects.get(book_id=book.id)
    assert bookplan.day_name_id == day_name.id
    assert bookplan.plan_id == plan.id
