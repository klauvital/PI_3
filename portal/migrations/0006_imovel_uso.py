# Generated by Django 4.1.2 on 2022-11-06 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_imovel_aquec_solar_imovel_banheiro_empre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='uso',
            field=models.CharField(blank=True, choices=[('1', 'Residencial'), ('2', 'Comercial'), ('3', 'Misto')], max_length=1, null=True, verbose_name='Estado Civil'),
        ),
    ]