from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    # logic for creating book
    return render(request, "create_book.html")

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # logic for editing
    return render(request, "edit_book.html", {"book": book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return render(request, "book_deleted.html")
