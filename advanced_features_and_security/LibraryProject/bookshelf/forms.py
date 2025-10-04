from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "summary", "cover"]  # limit fields explicitly

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Title is required.")
        if len(title) > 200:
            raise forms.ValidationError("Title is too long.")
        return title

    def clean_summary(self):
        summary = self.cleaned_data.get("summary", "")
        return summary

class BookSearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)

    def clean_q(self):
        q = self.cleaned_data.get("q", "").strip()
        return q
