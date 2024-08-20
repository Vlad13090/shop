from rest_framework import generics, viewsets
from API.serializers import ShoesSerializer
from main.models import Shoes


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
