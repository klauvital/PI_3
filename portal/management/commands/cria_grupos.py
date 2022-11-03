from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


def create_groups():
    groups = (
        'proprietario_avaliador',
        'proprietario',
        'corretor',
        'imobiliaria',

    )
    aux_list = [Group(name=group) for group in groups]
    Group.objects.bulk_create(aux_list)


class Command(BaseCommand):
    help = 'Cria Grupos.'

    def handle(self, *args, **options):
        Group.objects.all().delete()
        create_groups()
