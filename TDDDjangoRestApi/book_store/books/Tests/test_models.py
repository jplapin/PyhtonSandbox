from django.test import TestCase
from ..models import Book


class BookTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Book.objects.create(
            title='The Hobbit', isbn='0618260307', author='J. R. R. Tolkien', num_pages=310, year_published=1937)
        Book.objects.create(
            title='Do Androids Dream of Electric Sheep?', isbn='9780345404473', author='Philip K. Dick', num_pages=210, year_published=1968)
   
    def test_get_author(self):
        book_hobbit = Book.objects.get(author='J. R. R. Tolkien')
        book_androids = Book.objects.get(author='Philip K. Dick')
        self.assertEqual(
            book_hobbit.get_author(), 'The author J. R. R. Tolkien wrote the book The Hobbit.')
        self.assertEqual(
            book_androids.get_author(), "The author Philip K. Dick wrote the book Do Androids Dream of Electric Sheep?.")
