from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProprietarioAvaliadorForm(UserCreationForm):
    required_css_class = 'required'


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

    celular = forms.CharField(
        label='Celular',
    )

    whatsApp = forms.BooleanField(
        label='WhatsApp',
        required=False,
    )

    cpf = forms.CharField(
        label='CPF',

    )
    cidade = forms.CharField(
        label='Cidade',
    )

    imobiliaria = forms.BooleanField(
        label='Imobiliária',
        required=False,
        initial=None,
    )

    corretor = forms.BooleanField(
        label='Corretor',
        required=False,
        initial=None,
    )

    dono = forms.BooleanField(
        label='Proprietário',
        required=False,
        initial=None,
    )

    password1 = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmação da Senha')   # noqa E501

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'celular', 'whatsApp', 'cpf', 'cidade', 'imobiliaria', 'corretor', 'dono', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['celular'].widget.attrs.update({'class': 'mask-cel'})


