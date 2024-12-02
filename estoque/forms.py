from django import forms
from . models import Produto

class Produto_form(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
