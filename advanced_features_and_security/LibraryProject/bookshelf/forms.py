from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=True, label="Search Books")
