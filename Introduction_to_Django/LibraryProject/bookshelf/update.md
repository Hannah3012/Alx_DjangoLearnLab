# Update a Book Instance (Django Shell)

This step demonstrates how to **update the title** of the book we created earlier.

---

## Python Command with Expected Output

```python
>>> from bookshelf.models import Book
>>> book = Book.bookects.get(title="1984", author="George Orwell", publication_year=1949)
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> {"id": book.id, "title": book.title, "author": book.author, "publication_year": book.publication_year}
{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949} 
