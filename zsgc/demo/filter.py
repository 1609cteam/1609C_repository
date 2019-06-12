import django_filters
from .models import *


class BookFilters(django_filters.rest_framework.FilterSet):

    min_price = django_filters.NumberFilter(field_name='Book_price', lookup_expr='gt')
    max_price = django_filters.NumberFilter(field_name='Book_price', lookup_expr='lt')

    class Meta:
        model = Book
        fields = ('min_price', 'max_price')
