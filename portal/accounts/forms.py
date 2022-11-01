from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProprietarioAvaliadorForm(UserCreationForm):


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
        label='Imobiliaria',
        required=False,
    )

    corretor = forms.BooleanField(
        label='Corretor',
        required=False,
    )

    proprietario = forms.BooleanField(
        label='Proprietário',
        required=False,
    )

    password1 = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmação da Senha')   # noqa E501

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'celular', 'whatsApp' ,'cpf', 'cidade','imobiliaria', 'corretor', 'proprietario', 'password1', 'password2')






