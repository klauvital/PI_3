from django import forms
from portal.models import Imovel, Nomecondominio, Estadoconser, Padrao, Tipo, Proprietario, Vidautil
from portal.services import has_group
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render


class CustomUserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome',
        max_length=150,
    )
    last_name = forms.CharField(
        label='Sobrenome',
        max_length=150,
    )
    email = forms.EmailField(
        label='E-mail',
    )

    class Meta:
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs['instance']:
            user_instance = kwargs['instance'].user

        if user:
            self.fields['first_name'].initial = user_instance.first_name
            self.fields['last_name'].initial = user_instance.last_name
            self.fields['email'].initial = user_instance.email

            if not has_group(user, 'proprietario_avaliador'):
                self.fields['first_name'].widget.attrs['readonly'] = True
                self.fields['last_name'].widget.attrs['readonly'] = True


status_choices = (
        ('1', 'Oferta'),
        ('2', 'Vendido')
    )


class ImovelForm(forms.ModelForm):
    required_css_class = 'required'

    dtacadastro = forms.DateField(
        label='Data Cadastro',
        required=False,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = Imovel
        fields = '__all__'

    def __init__(self, user=User, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = user.username
        queryset = Proprietario.objects.filter(email=user)
        self.fields['consultor'].queryset = queryset


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

class ProprietarioAddForm(CustomUserForm):
    required_css_class = 'required'

    class Meta:
        model = Proprietario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'}) # noqa E501


class ProprietarioUpdateForm(CustomUserForm):
    required_css_class = 'required'

    class Meta:
        model = Proprietario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'}) # noqa E501

    def save(self, commit=True):
        instance = super().save(commit=False)

        user = instance.user

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']

        if commit:
            user.username = email
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            instance.save()
        return instance






