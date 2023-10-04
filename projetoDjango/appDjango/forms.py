from django import forms
from .models import Estoque

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['nome', 'descricao', 'quantidade']
        labels = {
            'nome': 'Nom',
            'descricao': 'Descrição',
            'quantidade': 'Quantidade',
        }
    
       