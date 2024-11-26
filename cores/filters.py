import django_filters
from .models import Cores
from django_filters import DateFilter, CharFilter

class CoresFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name='ingreso', lookup_expr='gte')
    end_date = DateFilter(field_name='egreso', lookup_expr='lte')
    efectivo = CharFilter(field_name='efectivo__efectivo_nombre', lookup_expr='icontains')

    class Meta:
        model = Cores
        fields = '__all__'
        exclude = ['efectivo', 'ingreso', 'egreso']
