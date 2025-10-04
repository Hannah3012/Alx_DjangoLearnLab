from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('', include('relationship_app.urls')),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
