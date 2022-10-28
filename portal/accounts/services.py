from django.contrib.auth.models import Group
from portal.services import add_permissions
from portal.models import Proprietario


def proprietario_avaliador_create(form, user):
    # Define username igual email.
    email = form.cleaned_data.pop('email')
    celular = form.cleaned_data.pop('celular')
    cpf = form.cleaned_data.pop('cpf')
    cidade = form.cleaned_data.pop('cidade')
    user.username = email

    user.save()

    # Adiciona ao grupo 'proprietario_avaliador'.
    group = Group.objects.get(name='proprietario_avaliador')
    user.groups.add(group)

    # Cria o Proprietario.
    Proprietario.objects.create(
        nome=user.first_name,
        sobrenome=user.last_name,
        email=user.username,
        cpf=cpf,
        cidade=cidade,
        celular=celular
    )

    #adiciona a permissão can_add_imovel
    add_permissions('proprietario_avaliador', ['add_imovel'])



