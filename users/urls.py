from django.urls import re_path

from . import views

app_name = "users"
urlpatterns = [
    re_path("signup", views.signup),
    re_path("login", views.login),
    re_path("logout", views.logout),
    re_path("test_token", views.test_token),
]
