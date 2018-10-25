from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'author', 'num_pages',
                  'created_at', 'updated_at', 'year_published')
