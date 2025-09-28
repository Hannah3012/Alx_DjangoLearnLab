from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET)
    books = Book.objects.none()
    if form.is_valid():
        query = form.cleaned_data['query']
        # safe ORM filter; prevents SQL injection
        books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})
