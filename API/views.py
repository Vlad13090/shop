from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from API.serializers import ShoesSerializer
from main.models import Shoes, Category


class ShoesViewSet(viewsets.ModelViewSet):
    # queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Shoes.objects.all()[:3]
        else:
            return Shoes.objects.filter(pk=pk)

    @action(methods=["GET"], detail=True)  # Новый роут http://localhost:8000/api/shoes/1/categories/
    def categories(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        return Response({"categories": categories.name})
