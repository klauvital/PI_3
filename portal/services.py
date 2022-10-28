from django.contrib.auth.models import Group, Permission


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
