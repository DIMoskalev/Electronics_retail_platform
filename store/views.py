from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from store.models import Link, Product
from store.permissions import IsActive
from store.serializers import LinkSerializer, ProductSerializer


class LinkCreateAPIView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActive]


class LinkRetrieveAPIView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActive]


class LinkListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'city', 'street', 'house_number', 'level']


class LinkUpdateAPIView(UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_update(self, serializer):
        if "debt" in serializer.validated_data:
            serializer.validated_data.pop("debt")
            raise Exception("Невозможно изменить поле задолженности")
        super().perform_update(serializer)


class LinkDestroyAPIView(DestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]
