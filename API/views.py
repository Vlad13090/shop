from rest_framework import generics
from API.serializers import ShoesSerializer
from main.models import Shoes


class ShoesAPIView(generics.ListCreateAPIView):  # Позволяет получить данные и добавить новые
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


# class ShoesAPIViewUpdate(generics.UpdateAPIView):  # Позволяет изменить данные
#     queryset = Shoes.objects.all()
#     serializer_class = ShoesSerializer


class ShoesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  # Позволяет читать, обновлять и удалять запись
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
