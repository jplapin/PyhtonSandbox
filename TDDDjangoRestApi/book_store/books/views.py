from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # get details of a single book
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    # delete a single book
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single book
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_books(request):
    # get all book
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    # insert a new record for a book
    if request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'isbn': request.data.get('isbn'),
            'author': request.data.get('author'),
            'num_pages': int(request.data.get('num_pages')),
            'year_published': int(request.data.get('year_published')),
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
