from django.shortcuts import render

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    Provides list, create, retrieve, update, partial_update, destroy
    """
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
