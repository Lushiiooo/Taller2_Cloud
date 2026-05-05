from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'cantidad_disponible']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del libro',
                'required': True
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Autor del libro',
                'required': True
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del libro',
                'rows': 5
            }),
            'cantidad_disponible': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad disponible',
                'min': 0,
                'required': True
            }),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Usuario',
            'required': True,
            'autocomplete': 'username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'required': True,
            'autocomplete': 'current-password'
        })
    )
