from django import forms
from .models import Producto, Usuario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'foto', 'marca', 'prunit', 'existencias']