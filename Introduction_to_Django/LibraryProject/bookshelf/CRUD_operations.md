# Django Shell CRUD — Book Model

This file demonstrates all CRUD operations for the `Book` model using the Django shell.  
Each operation includes the Python command and the expected output inline.

---

## Prerequisites

1. Your app (e.g., `bookshelf`) is added to `INSTALLED_APPS` in `settings.py`.
2. `models.py` defines a `Book` model:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} — {self.author} ({self.publication_year})"

3. Run migrations

# 1. Create a Book Instance
>>> from bookshelf.models import Book
>>> b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> b.pk  
1  # ✅ ID of the new record (value may differ if other rows exist)

# 2. Retrieve the Book Instance
>>> obj = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
>>> {"id": obj.id, "title": obj.title, "author": obj.author, "publication_year": obj.publication_year}
{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}  # ✅ Values of the retrieved book

# 3. Update the Book Title
>>> obj = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
>>> obj.title = "Nineteen Eighty-Four"
>>> obj.save()
>>> {"id": obj.id, "title": obj.title, "author": obj.author, "publication_year": obj.publication_year}
{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}  # ✅ Title updated successfully

# 4. Delete the Book Instance
>>> deleted, _ = Book.objects.filter(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949).delete()
>>> deleted
1  # ✅ One row deleted
>>> list(Book.objects.all().values("id","title","author","publication_year"))
[]  # ✅ Empty list confirms the book was removed
