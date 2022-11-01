# Generated by Django 4.1.2 on 2022-10-30 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=200)),
                ('creci', models.CharField(max_length=200)),
                ('dtanasc', models.DateField(blank=True, null=True)),
                ('cidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estadoconser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nomecondominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('endereco', models.CharField(blank=True, max_length=300, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('uf', models.CharField(blank=True, db_column='UF', max_length=2, null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Padrao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('sobrenome', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sobrenome')),
                ('celular', models.CharField(max_length=200, verbose_name='Celular')),
                ('CelularWhats', models.BooleanField(blank=True, default=False, null=True, verbose_name='WhatsApp ?')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('corretor', models.BooleanField(blank=True, default=False, null=True, verbose_name='Corretor')),
                ('imobiliaria', models.BooleanField(blank=True, default=False, null=True, verbose_name='Imobiliária')),
                ('dono', models.BooleanField(blank=True, default=False, null=True, verbose_name='Proprietário')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Tabelarossheideck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade_em_vida', models.IntegerField(blank=True, db_column='idade_em_vida', null=True)),
                ('a', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('b', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('c', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('d', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('e', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('f', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('g', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('h', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Vidautil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('idadevidautil', models.IntegerField(blank=True, db_column='idadeVidaUtil', null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valordevenda', models.DecimalField(db_column='valorDeVenda', decimal_places=2, default=0, max_digits=10, verbose_name='Valor de venda')),
                ('idade', models.IntegerField(blank=True)),
                ('bairro', models.CharField(blank=True, max_length=100)),
                ('cidade', models.CharField(blank=True, max_length=200)),
                ('aconstruida', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Área Construída/Útil')),
                ('atotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Área Total')),
                ('dtacadastro', models.DateField(blank=True, db_column='dtaCadastro', null=True, verbose_name='Data de cadastro')),
                ('status', models.CharField(choices=[('1', 'Oferta'), ('2', 'Vendido')], max_length=1)),
                ('corretor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.corretor')),
                ('estadoconser', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.estadoconser', verbose_name='Estado de Conservação')),
                ('nomecondominio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.nomecondominio', verbose_name='Condominio')),
                ('padrao', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.padrao')),
                ('proprietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.proprietario', verbose_name='Proprietario')),
                ('tipo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.tipo')),
                ('vidautil', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.vidautil', verbose_name='Vida Útil')),
            ],
            options={
                'ordering': ['-dtacadastro'],
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliacao', models.DateField(verbose_name='Data Avaliação')),
                ('valor_metro_quadrado', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor m²')),
                ('valor_metro_quadrado_final', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor Final m² ')),
                ('desconto_oferta', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor m²')),
                ('valor_da_coluna', models.CharField(max_length=1, verbose_name='Coluna')),
                ('idade_em_perc', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Idade em % vida')),
                ('valor_avaliacao', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Avaliação')),
                ('imovel', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.imovel')),
                ('ross_heideck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.tabelarossheideck')),
            ],
            options={
                'ordering': ['-data_avaliacao'],
            },
        ),
    ]
