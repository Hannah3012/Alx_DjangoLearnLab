
# Delete a Book Instance (Django Shell)

This step demonstrates how to **delete the book** and verify its removal from the database.

---

## Python Command with Expected Output

```python
>>> from bookshelf.models import Book
>>> deleted, _ = Book.objects.filter(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949).delete()
>>> deleted
1  # ✅ One row deleted
>>> list(Book.objects.all().values("id","title","author","publication_year"))
[]  # ✅ Empty list confirms the book was removed
