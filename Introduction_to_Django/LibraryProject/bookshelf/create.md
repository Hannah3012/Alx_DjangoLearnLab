# Create a Book Instance (Django Shell)

This step shows how to **create a new `Book` record** in the database using the Django shell.  

---

## Python Command with Expected Output

```python
>>> from bookshelf.models import Book
>>> b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> b.pk  
1  





