from django import forms
from portal.models import Imovel, Nomecondominio, Estadoconser, Padrao, Tipo, Proprietario


status_choices = (
        ('1', 'Oferta'),
        ('2', 'Vendido')
    )

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dtacadastro'].widget.attrs.update({'class': 'mask-date'})
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ImovelFormFilter(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude=('valordevenda', 'dtacadastro', 'corretor', 'vidautil', 'status')

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        exclude = ()

        widgets = {
             'nome': forms.TextInput(attrs={'class': 'form-control'})

        }

class PadraoForm(forms.ModelForm):
    class Meta:
        model = Padrao
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})

        }

class EstadoconserForm(forms.ModelForm):
    class Meta:
        model = Estadoconser
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),

        }

class NomecondominioForm(forms.ModelForm):
    class Meta:
        model = Nomecondominio
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProprietarioForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})

        }
