# Generated by Django 4.1.2 on 2022-10-28 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_proprietario_alter_vidautil_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proprietario',
            options={'ordering': ['nome']},
        ),
    ]
