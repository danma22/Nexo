from django import forms
from django.core import validators
from .models import Task

class TaskForm(forms.ModelForm):
    remove_category = forms.BooleanField(
        required=False,
        initial=False,
        label="Quitar categoría de la tarea actual",
        widget=forms.CheckboxInput(attrs={
                'class': 'hidden',
                'tabindex': '0'
            }
        )
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titulo'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'category': forms.Select(attrs={'class': 'ui fluid dropdown'})
        }
        labels = {
            'title': 'Título (*)',
            'description': 'Descripción (*)',
            'category': 'Categoría'
        }
        error_messages = {
            'title': {
                'required': 'El título es obligatorio',
                'max_length': 'El título no puede ser mayor de 50 caracteres'
            },
            'description': {
                'required': 'La descripción es obligatoria'
            },
            'category': {
                'invalid_choice': 'Seleccione una categoría válida',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Selecciona una categoría"
        self.fields['category'].required = False

    def save(self, commit=True):
        task = super().save(commit=False)

        if self.cleaned_data['remove_category']:
            task.category = None
        
        if commit:
            task.save()
            self.save_m2m()

        return task