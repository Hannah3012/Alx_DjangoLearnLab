# Update a Book Instance (Django Shell)

This step demonstrates how to **update the title** of the book we created earlier.

---

## Python Command with Expected Output

```python
>>> from bookshelf.models import Book
>>> obj = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
>>> obj.title = "Nineteen Eighty-Four"
>>> obj.save()
>>> {"id": obj.id, "title": obj.title, "author": obj.author, "publication_year": obj.publication_year}
{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949} 
