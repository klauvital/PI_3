# Generated by Django 4.1.2 on 2022-11-21 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_remove_pesquisa_user_consultor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pesquisa',
            options={'ordering': ['-data_pesquisa']},
        ),
        migrations.RenameField(
            model_name='pesquisa',
            old_name='data',
            new_name='data_pesquisa',
        ),
        migrations.RenameField(
            model_name='pesquisa',
            old_name='user_consultor_id',
            new_name='user_consultor',
        ),
    ]
