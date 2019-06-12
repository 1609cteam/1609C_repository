from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filter import BookFilters


class Page(PageNumberPagination):
    page_size = 2


class BookTypeViewSet(ModelViewSet):

    pagination_class = Page

    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializers


class BookViewSet(ModelViewSet):
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    filter_class = BookFilters
    search_fields = ('book_name',)
    ordering_fields = ('book_price',)

    queryset = Book.objects.all()
    serializer_class = BookSerializers
