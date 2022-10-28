# Generated by Django 4.1.2 on 2022-10-28 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_imovel_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='vidautil',
            options={'ordering': ['nome']},
        ),
        migrations.AddField(
            model_name='imovel',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.proprietario', verbose_name='Proprietario'),
        ),
    ]
