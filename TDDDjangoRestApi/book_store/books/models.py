from django.db import models


class Book(models.Model):
    """
    Book Model
    Defines the attributes of a book
    """
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    num_pages = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    year_published = models.IntegerField()

    def get_author(self):
        return 'The author ' +self.author + ' wrote the book ' + self.title + '.'

    def __repr__(self):
        return 'The book '+self.title + ' is added.'
