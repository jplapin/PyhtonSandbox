import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Book
from ..serializers import BookSerializer


# initialize the APIClient app
client = Client()


class GetAllBooksTest(TestCase):
    """ Test module for GET all books API """

    def setUp(self):
        Book.objects.create(
            title='The Hobbit', isbn='0618260307', author='J. R. R. Tolkien', num_pages=310, year_published=1937)
        Book.objects.create(
            title='Do Androids Dream of Electric Sheep?', isbn='9780345404473', author='Philip K. Dick', num_pages=210, year_published=1968)
        Book.objects.create(
            title='Neuromancer', isbn='9780441569595', author='William Gibson', num_pages=271, year_published=1984)
        Book.objects.create(
            title='Dune', isbn='9789896372484', author='Frank Herbert', num_pages=412, year_published=1965)
        Book.objects.create(
            title='Nineteen Eighty-Four', isbn='9780451524935', author='George Orwell', num_pages=328, year_published=1949)

    def test_get_all_books(self):
        # get API response
        response = client.get(reverse('get_post_books'))
        # get data from db
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleBookTest(TestCase):
    """ Test module for GET single book API """

    def setUp(self):
        self.hobbit =  Book.objects.create(
            title='The Hobbit', isbn='0618260307', author='J. R. R. Tolkien', num_pages=310, year_published=1937)
        self.androids = Book.objects.create(
            title='Do Androids Dream of Electric Sheep?', isbn='9780345404473', author='Philip K. Dick', num_pages=210, year_published=1968)
        self.neuromancer = Book.objects.create(
            title='Neuromancer', isbn='9780441569595', author='William Gibson', num_pages=271, year_published=1984)
        self.dune = Book.objects.create(
            title='Dune', isbn='9789896372484', author='Frank Herbert', num_pages=412, year_published=1965)
        self.nieifour = Book.objects.create(
            title='Nineteen Eighty-Four', isbn='9780451524935', author='George Orwell', num_pages=328, year_published=1949)


    def test_get_valid_single_book(self):
        response = client.get(
            reverse('get_delete_update_book', kwargs={'pk': self.hobbit.pk}))
        book = Book.objects.get(pk=self.hobbit.pk)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_book(self):
        response = client.get(
            reverse('get_delete_update_book', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewBookTest(TestCase):
    """ Test module for inserting a new book """

    def setUp(self):
        self.valid_payload = {
            'title' : 'Nineteen Eighty-Four', 
            'isbn' : '9780451524935', 
            'author' : 'George Orwell', 
            'num_pages' : 328, 
            'year_published' : 1949
        }
        self.invalid_payload = {
            'title' : '',
            'isbn' : '9780451524935',
            'author' : 'George Orwell',
            'num_pages' : 328,
            'year_published' : 1949
        }

    def test_create_valid_book(self):
        response = client.post(
            reverse('get_post_books'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_book(self):
        response = client.post(
            reverse('get_post_books'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
