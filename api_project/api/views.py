from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    Supports:
      - GET /books_all/       → List all books
      - GET /books_all/<id>/  → Retrieve a specific book
      - POST /books_all/      → Create a new book
      - PUT /books_all/<id>/  → Update an existing book
      - DELETE /books_all/<id>/ → Delete a book
    """
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
