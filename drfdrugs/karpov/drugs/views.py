from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from drugs.models import Drugs
from drugs.serializers import DrugsSerializer

class DrugsViewSet(viewsets.ModelViewSet):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer
    parser_classes = (MultiPartParser, FormParser)



