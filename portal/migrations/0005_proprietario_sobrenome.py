# Generated by Django 4.1.2 on 2022-10-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_alter_proprietario_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='proprietario',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
