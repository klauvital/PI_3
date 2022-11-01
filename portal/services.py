from django.contrib.auth.models import Group, Permission, User


def user_create(form):
    nome = form.cleaned_data.get('first_name')
    sobrenome = form.cleaned_data.get('last_name')
    email = form.cleaned_data.get('email')
    celular = form.CharField('celular', max_length=200)
    celularWhats = form.BooleanField('whatsApp', default=False, blank=True, null=True)
    cpf = form.CharField('cpf', max_length=20)
    cidade = form.CharField('cidade', max_length=200)
    corretor = form.BooleanField('corretor', default=False, blank=True, null=True)
    imobiliaria = form.BooleanField('imobiliária', default=False, blank=True, null=True)
    dono =form.BooleanField('proprietario', default=False, blank=True, null=True)
    user = User.objects.create(
        username=email,
        first_name=nome,
        last_name=sobrenome,
        email=email,
        celular =celular,
        celularWhats=celularWhats,
        cpf=cpf,
        cidade=cidade,
        corretor=corretor,
        imobiliaria=imobiliaria,
        dono=dono,
    )
    return user


def add_to_group_proprietario(form, user):
    # Adiciona o Proprietario no grupo 'proprietario'.
    group = Group.objects.get(name='proprietario')
    user.groups.add(group)

    # Adiciona a permissão add_imovel e update_imovel.
    add_permissions('proprietario', ['add_imovel', 'update_imovel', 'update_proprietario'])


def has_group(user, group_name):
    ''' Verifica se este usuário pertence a um grupo. '''
    if user:
        groups = user.groups.all().values_list('name', flat=True)
        return True if group_name in groups else False
    return False


def add_permissions(group_name, permissions):
    group = Group.objects.get(name=group_name)
    permissions = Permission.objects.filter(codename__in=permissions)
    # Remove todas as permissões.
    group.permissions.clear()
    # Adiciona novas permissões.
    for perm in permissions:
        group.permissions.add(perm)


