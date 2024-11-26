import django_filters
from .models import Turno, Adicional
from django.contrib.auth.models import User
from django_filters import DateFilter, ModelChoiceFilter

class RendicionFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name='ingreso', lookup_expr='gte')
    end_date = DateFilter(field_name='egreso', lookup_expr='lte')

    class Meta:
        model = Turno
        fields = ['ingreso', 'egreso']
