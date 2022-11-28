from django.contrib.auth.models import Group
from portal.services import add_permissions
from portal.models import Proprietario


def proprietario_avaliador_create(form, user):
    # Define username igual email.
    email = form.cleaned_data.pop('email')
    cidade = form.cleaned_data.pop('cidade')
    celular = form.cleaned_data.pop('celular')
    whatsApp = form.cleaned_data.pop('whatsApp')
    cpf = form.cleaned_data.pop('cpf')
    corretor = form.cleaned_data.pop('corretor')
    imobiliaria = form.cleaned_data.pop('imobiliaria')
    dono = form.cleaned_data.pop('dono')
    user.username = email

    user.save()


    # Adiciona ao grupo 'proprietario_avaliador'.
    group = Group.objects.get(name='proprietario_avaliador')
    user.groups.add(group)


    # Cria o Proprietario.
    #Proprietario.objects.create(user=user)
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
        dono=dono,

        )

       # Adiciona ao grupo.
    if corretor:
        group = Group.objects.get(name='corretor')
    elif imobiliaria:
        group = Group.objects.get(name='imobiliaria')
    elif dono:
        group = Group.objects.get(name='proprietario')
    user.groups.add(group)

    add_permissions('proprietario_avaliador', ['add_imovel'])
    add_permissions('proprietario', ['add_imovel'])
    add_permissions('corretor', ['add_imovel'])
    add_permissions('imobiliaria', ['add_imovel'])



