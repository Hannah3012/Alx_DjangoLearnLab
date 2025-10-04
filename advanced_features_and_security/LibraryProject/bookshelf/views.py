from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.db import connection
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm, BookSearchForm
from .forms import ExampleForm

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})

def book_list(request):
    form = BookSearchForm(request.GET)
    books_qs = Book.objects.all().order_by("title")
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            books_qs = books_qs.filter(title__icontains=q) 
    paginator = Paginator(books_qs, 20)
    page = request.GET.get("page", 1)
    books = paginator.get_page(page)
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})

@require_http_methods(["GET", "POST"])
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("bookshelf:book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})

@require_http_methods(["GET", "POST"])
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookshelf:book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form})

@require_POST
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return redirect("bookshelf:book_list")

def raw_books_example(user_input):
    sql = "SELECT id, title FROM bookshelf_book WHERE title LIKE %s"
    pattern = f"%{user_input}%"
    with connection.cursor() as cursor:
        cursor.execute(sql, [pattern])  
    return rows
