from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    GET /api/books/  -> returns a JSON list of all books
    """
    queryset = Book.objects.all().order_by('-id') 
    serializer_class = BookSerializer

