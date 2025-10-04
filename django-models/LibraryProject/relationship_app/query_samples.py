import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def create_sample_data():
    author, _ = Author.objects.get_or_create(name="Jane Austen")
    b1, _ = Book.objects.get_or_create(title="Pride and Prejudice", author=author)
    b2, _ = Book.objects.get_or_create(title="Emma", author=author)

    lib, _ = Library.objects.get_or_create(name="Central Library")
    lib.books.add(b1, b2)

    librarian, _ = Librarian.objects.get_or_create(name="John Smith", library=lib)
    return author, lib, librarian


def queries(author, library, librarian):
    print("=== Query: All books by author ===")
    books_by_author = Book.objects.filter(author=author)
    for book in books_by_author:
        print("-", book.title)

    print("\n=== Query: All books in library ===")
    library_name = "Central Library"
    selected_library = Library.objects.get(name=library_name)
    for b in selected_library.books.all():
        print("-", b.title)

    print("\n=== Query: Librarian for the library ===")
    print("Librarian:", Librarian.objects.get(library=library).name)


if __name__ == '__main__':
    author, library, librarian = create_sample_data()
    queries(author, library, librarian)
