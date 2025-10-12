from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields.
    Includes custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['id']

    def validate_publication_year(self, value):
        """
        Field-level validation:
        - Ensure the publication_year is not greater than current year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class NestedBookSerializer(serializers.ModelSerializer):
    """
    A small serializer used for nested display inside AuthorSerializer.
    It omits the 'author' field to avoid circular nesting.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model:
    - name field
    - nested 'books' field which serializes related Book instances using NestedBookSerializer
    The 'books' field is read-only here (used for representation). If you want to allow
    creating books together with an author, you'd implement create/update methods.
    """
    books = NestedBookSerializer(source='books', many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        read_only_fields = ['id']
