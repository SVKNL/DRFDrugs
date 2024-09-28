from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from drugs.models import Drugs
from drugs.serializers import DrugsSerializer


# Create your views here.
class DrugsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer
    parser_classes = (MultiPartParser, FormParser)


class DrugsUpdateAPIView(generics.UpdateAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer
    parser_classes = (MultiPartParser, FormParser)


class DrugsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer
    parser_classes = (MultiPartParser, FormParser)
