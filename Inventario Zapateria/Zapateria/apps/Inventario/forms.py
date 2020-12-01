from django import forms
from .models import *

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = [
            'color',
        ]

class TallaForm(forms.ModelForm):
    class Meta:
        model = Talla
        fields = [
            'talla',
        ]
class ZapatoForm(forms.ModelForm):
        class Meta:
            model = Zapato
            fields = [
                'codigoZapato',
                'modeloZapato',
                'descripcionZapato',
                'tipoZapato'
            ]

class ZapatoPorTallaPorColorForm(forms.ModelForm):
    class Meta:
        model = ZapatoPorTallaPorColor
        fields = [
            'cantidadZapatosPorTallaPorColor',
            'codigoZapatoFK',
            'colorFK',
            'tallaFK',
        ]