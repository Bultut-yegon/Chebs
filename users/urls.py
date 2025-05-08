from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

# app_name = "users"
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.custom_login, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]