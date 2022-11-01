from django.contrib.auth.models import Group
from portal.services import add_permissions
from portal.models import Proprietario
from django.contrib.auth.models import User


def proprietario_avaliador_create(form, user):
    # Define username igual email.
    email = form.cleaned_data.pop('email')
    cidade = form.cleaned_data.pop('cidade')
    celular = form.cleaned_data.pop('celular')
    whatsApp = form.cleaned_data.pop('whatsApp')
    cpf = form.cleaned_data.pop('cpf')
    corretor = form.cleaned_data.pop('corretor')
    imobiliaria = form.cleaned_data.pop('imobiliaria')
    proprietario = form.cleaned_data.pop('proprietario')
    user.username = email

    user.save()

    # Adiciona ao grupo 'proprietario_avaliador'.
    group = Group.objects.get(name='proprietario_avaliador')
    user.groups.add(group)


    # Cria o Proprietario.
    #proprietario = Proprietario.objects.filter(email=user.email)
    #if not proprietario:
    Proprietario.objects.create(
        nome=user.first_name,
        sobrenome=user.last_name,
        email=email,
        cpf=cpf,
        cidade=cidade,
        celular=celular,
        whatsApp=whatsApp,
        corretor=corretor,
        imobiliaria=imobiliaria,
        dono=proprietario,
        )

    # Como é o Proprietario_Avaliador,
    # adiciona a permissão can_add_imovel.
    add_permissions('proprietario_avaliador', ['add_imovel'])

    # Adiciona ao grupo 'proprietario'.
    group = Group.objects.get(name='proprietario')
    user.groups.add(group)






