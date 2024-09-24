from rest_framework import generics

from .models import Cats
from .serializers import CatsSerializer




class CatsList(generics.ListCreateAPIView):
    serializer_class = CatsSerializer

    def get_queryset(self):
        queryset = Cats.objects.all()
        return queryset


class CatsDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CatsSerializer
    queryset = Cats.objects.all()
