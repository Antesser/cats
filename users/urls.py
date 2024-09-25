from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

app_name = "users"
urlpatterns = [
    path("signup/", views.signup),
    path("get_token/", TokenObtainPairView.as_view()),
    path("login/", views.login),
    path("logout/", views.logout),
    path("test_token/", views.test_token),
]
