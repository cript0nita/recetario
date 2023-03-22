from django import forms
from .models import Categoria, Receta


class RecestasForm(forms.ModelForm):
    """
    Formulario con definicion de tipos campos 
    """

    titulo = forms.CharField(
        label='Título',
        required=True,
        max_length=250,
        widget=forms.TextInput(
            attrs={ 'class': 'form-control' }
        )
    )

    dificultad = forms.ChoiceField(
        label='Dificultad',
        required=True,
        choices=(
            ('', '---------'),
            ('Baja', 'Dificultad baja'),
            ('Media', 'Dificultad media'),
            ('Alta', 'Dificultad alta'),
        ),
        widget=forms.Select(
            attrs={ 'class': 'form-select' }
        )
    )

    categoria = forms.ModelChoiceField(
        label='Categoria',
        required=True,
        queryset=Categoria.objects.all(),
        widget=forms.Select(
            attrs={ 'class': 'form-select' }
        )
    )

    descripcion = forms.CharField(
        label='Descripción',
        required=True,
        max_length=250,
        widget=forms.Textarea(
            attrs={ 'class': 'form-control', 'rows': 3 }
        )
    )

    class Meta:
        model = Receta
        fields = ('titulo','descripcion', 'dificultad', 'categoria')
