from django import forms
from django.core import validators
from .models import Contact, PhoneNumber, Domicile

class ContactForm(forms.ModelForm):
    remove_group = forms.BooleanField(
        required=False,
        initial=False,
        label="Quitar grupo del contacto actual",
        widget=forms.CheckboxInput(attrs={
                'class': 'hidden',
                'tabindex': '0'
            }
        )
    )

    class Meta:
        model = Contact
        fields = [
            'name', 'last_name_p', 'last_name_m', 
            'email', 'discord_account', 'github_account', 'group'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Nombre(s)'}), 
            'last_name_p': forms.TextInput(attrs={'placeholder':'Apellido Paterno'}), 
            'last_name_m': forms.TextInput(attrs={'placeholder':'Apellido Materno'}), 
            'email': forms.EmailInput(attrs={'placeholder':'example@sos.com'}), 
            'discord_account': forms.URLInput(attrs={'placeholder':'https://'}), 
            'github_account': forms.URLInput(attrs={'placeholder':'https://'}),
            'group': forms.Select(attrs={'class': 'ui fluid dropdown'})
        }
        labels = {
            'name': 'Nombre completo (*)', 
            'last_name_p': 'Apellido Paterno', 
            'last_name_m': 'Apellido Materno', 
            'email': 'Correo electrónico (*)', 
            'discord_account': 'Perfil de Discord', 
            'github_account': 'Perfil de Github',
            'group': 'Grupo'
        }
        error_messages = {
            'name': {
                'required': 'El nombre es obligatorio',
                'max_length': 'El nombre no puede ser mayor de 50 caracteres'
            },
            'last_name_p': {
                'required': 'El apellido paterno es obligatorio',
                'max_length': 'El apellido paterno no puede ser mayor de 50 caracteres'
            },
            'last_name_m': {
                'required': 'El apellido materno es obligatorio',
                'max_length': 'El apellido materno no puede ser mayor de 50 caracteres'
            },
            'email': {
                'required': 'El correo electrónico es obligatorio',
                'invalid': 'Escribe un correo electrónico válido',
                'max_length': 'El correo electrónico no puede ser mayor de 50 caracteres'
            },
            'discord_account': {
                'invalid': 'Escribe una dirección URL de discord válida'
            },
            'github_account': {
                'invalid': 'Escribe una dirección URL de github válida'
            },
            'group': {
                'invalid_choice': 'Seleccione un grupo válido',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = "Selecciona un grupo"
        self.fields['group'].required = False

    def save(self, commit=True):
        contact = super().save(commit=False)

        if self.cleaned_data['remove_group']:
            contact.group = None

        if commit:
            contact.save()
            self.save_m2m()

        return contact


class DomicileForm(forms.ModelForm):
    class Meta:
        model = Domicile
        fields = '__all__'
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Calle Matusalen #XXX'}),
            'city': forms.TextInput(attrs={'placeholder': 'Ciudad ...'}),
            'province': forms.TextInput(attrs={'placeholder': 'Provincia ...'}),
            'country': forms.Select(attrs={'class': 'ui fluid dropdown'})
        }
        labels = {
            'address': 'Dirección', 
            'city': 'Ciudad', 
            'province': 'Provincia', 
            'country': 'País'
        }
        error_messages = {
            'address': {
                'required': 'La dirección es obligatorio',
                'max_length': 'La dirección no puede ser mayor de 100 caracteres'
            }, 
            'city': {
                'required': 'La ciudad es obligatorio',
                'max_length': 'La ciudad no puede ser mayor de 50 caracteres'
            }, 
            'province': {
                'max_length': 'La provincia no puede ser mayor de 50 caracteres'
            }, 
            'country': {
                'required': 'El país es obligatorio',
                'invalid_choice': 'Seleccione una opción válida'
            }
        }


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = '__all__'
        widgets = {
            'country_code': forms.TextInput(attrs={'placeholder': 'XX (LADA)'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'XXX XXX XXXX'})
        }
        labels = {
            'country_code': 'LADA', 
            'phone_number': 'Número de teléfono'
        }
        error_messages = {
            'country_code': {
                'max_length': 'La LADA no puede ser mayor de 5 caracteres'
            }, 
            'phone_number': {
                'required': 'El número de teléfono es obligatorio',
                'max_length': 'El número de teléfono no puede ser mayor de 15 caracteres'
            }
        }