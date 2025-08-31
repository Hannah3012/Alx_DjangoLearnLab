# Retrieve a Book Instance (Django Shell)

This step shows how to **retrieve and display the details** of the book we created earlier.

---

## Python Command with Expected Output

```python
>>> from bookshelf.models import Book
>>> obj = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
>>> {"id": obj.id, "title": obj.title, "author": obj.author, "publication_year": obj.publication_year}
{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}  
