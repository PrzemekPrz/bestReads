from bestReads.models import Book, Plan, BookPlan, Votes, Dayname
import pytest

@pytest.fixture
def votes():
    return Votes.objects.create(
        votes='***'
    )


@pytest.fixture
def book(votes):
    return Book.objects.create(
        name='Potop',
        description='Książka o kmicicu',
        author='Henryk Sienkiewicz',
        isbn='123456789',
        number_pages=936,
        votes=votes
    )

@pytest.fixture
def plan(votes):
    return Plan.objects.create(
        name='Intensywny Plan',
        description='Example Text',
        votes=votes
    )

@pytest.fixture
def day_name():
    return Dayname.objects.create(
        day_name='Poniedziałek'
    )



