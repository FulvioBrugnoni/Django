from django import forms
from .models import Questionario





class Inserimento(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = [
                    'nome','cognome','q1','q2'
        ]
        widget = {
                'nome': forms.TextInput(attrs={'cols':1200}),
                'cognome': forms.TextInput(attrs={'class':'form-control'}),
                'q1': forms.TextInput(attrs={'class':'form-control'}),
        }
