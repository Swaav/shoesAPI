from rest_framework import viewsets
from apishoe import models, serializers


class Manufacturer_View(viewsets.ModelViewSet):

    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.Manufacturer_Serializer


class ShoeType_View(viewsets.ModelViewSet):

    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeType_Serializer


class ShoeColor_View(viewsets.ModelViewSet):

    queryset = models.ShoeColor.objects.all()
    serializer_class = serializers.ShoeColor_Serializer


class Shoe_View(viewsets.ModelViewSet):

    queryset = models.Shoe.objects.all()
    serializer_class = serializers.Shoe_Serializer