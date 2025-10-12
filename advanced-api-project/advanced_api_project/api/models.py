from django.db import models

class Author(models.Model):
    """
    Author model:
    - name: stores the author's full name as a string.
    This model represents a book author. An Author can have many Books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - title: the book title (string).
    - publication_year: integer year the book was published.
    - author: ForeignKey to Author establishing a one-to-many relation
              (one Author -> many Books).
    Purpose: stores book metadata and links each book to an Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
