from .views import CatsList, CatsDetail
from django.urls import path

urlpatterns = [
    path("all_cats/", CatsList.as_view()),
    path("cat/<int:pk>/", CatsDetail.as_view()),
    
]