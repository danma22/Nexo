import django_filters
from django import forms
from .models import Task, Status, Category

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Filtrar por titulo'}),
        label='Buscar por título'
    )
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'ui fluid dropdown'}),
        label='Buscar por estatus'
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'ui fluid dropdown'}),
        label='Buscar por categoría'
    )

    class Meta:
        model = Task
        fields = ['title', 'status', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['status'].empty_label = "Selecciona una categoría"
        self.form.fields['category'].empty_label = "Selecciona una categoría"