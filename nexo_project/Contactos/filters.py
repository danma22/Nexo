import django_filters
from django import forms
from .models import Contact, Group

class ContactFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre(s)'}),
        label='Buscar por nombre completo'
    )

    last_name_p = django_filters.CharFilter(
        field_name='last_name_p',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Apellido paterno'}),
        label='Buscar por apellido paterno'
    )

    last_name_m = django_filters.CharFilter(
        field_name='last_name_m',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Apellido materno'}),
        label='Buscar por apellido materno'
    )

    group = django_filters.ModelChoiceFilter(
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={'class': 'ui fluid dropdown'}),
        label='Buscar por grupo'
    )

    class Meta:
        model = Contact
        fields = ['name', 'last_name_p', 'last_name_m', 'group']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['group'].empty_label = "Selecciona un grupo"