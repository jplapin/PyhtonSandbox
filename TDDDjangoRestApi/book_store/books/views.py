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
        return Response({})
    # delete a single book
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single book
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_books(request):
    # get all books
    if request.method == 'GET':
        return Response({})
    # insert a new record for a book
    elif request.method == 'POST':
        return Response({})
