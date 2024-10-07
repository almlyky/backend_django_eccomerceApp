import django_filters
import django_filters.fields
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    bigThen = django_filters.NumberFilter(field_name='pr_cost' or 0, lookup_expr='gt')
    lesThen = django_filters.NumberFilter(field_name='pr_cost', lookup_expr='lt')
    keyword = django_filters.CharFilter(field_name='pr_name_en', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['pr_name','keyword']