from rest_framework.serializers import HyperlinkedModelSerializer

from apishoe import models


class Manufacturer_Serializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer

        fields = ['name', 'website']


class ShoeType_Serializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeType

        fields = ['style']


class ShoeColor_Serializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeColor

        fields = ['color_style']


class Shoe_Serializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Shoe

        fields = ['size', 'brand', 'manufacturer', 'color', 'material', 'shoe_type', 'fasten_type']