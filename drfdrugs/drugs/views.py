from django.shortcuts import render
from rest_framework import generics

from .models import Drugs
from .serializers import DrugsSerializer


# Create your views here.
class DrugsAPIView(generics.ListAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer
