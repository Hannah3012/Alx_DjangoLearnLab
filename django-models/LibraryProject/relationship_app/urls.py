from django.urls import path
from . import views
from . import views_role

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Auth
    path("register/", views.register_view, name="register"),
    path("login/", views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Role-based access
    path("admin-view/", views_role.admin_view, name="admin_view"),
    path("librarian-view/", views_role.librarian_view, name="librarian_view"),
    path("member-view/", views_role.member_view, name="member_view"),
]

