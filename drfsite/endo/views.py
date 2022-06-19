from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Endo
from .serializers import EndoSerializer


class EndoAPIList(generics.ListCreateAPIView):
    queryset = Endo.objects.all()
    serializer_class = EndoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class EndoAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Endo.objects.all()
    serializer_class = EndoSerializer
    permission_classes = (IsAuthenticated, )

