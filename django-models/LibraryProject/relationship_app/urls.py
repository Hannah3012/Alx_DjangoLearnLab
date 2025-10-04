from django.urls import path, include
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('', include('relationship_app.urls')),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
]
