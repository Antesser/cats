from rest_framework import generics

from users.permissions import IsOwnerOrReadOnly

from .models import Cats
from .serializers import CatsSerializer

from rest_framework import permissions


class CatsList(generics.ListCreateAPIView):
    serializer_class = CatsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_queryset(self):
        queryset = Cats.objects.filter(owner=self.request.user)
        return queryset


class CatsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatsSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly
    ]
    queryset = Cats.objects.all()
