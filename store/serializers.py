from rest_framework.serializers import ModelSerializer

from store.models import Link, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class LinkSerializer(ModelSerializer):

    class Meta:
        model = Link
        fields = "__all__"
