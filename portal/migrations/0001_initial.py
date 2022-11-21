# Generated by Django 4.1.2 on 2022-11-21 00:16

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
                ('whatsApp', models.BooleanField(blank=True, default=False, null=True, verbose_name='WhatsApp ?')),
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
            name='Pesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, db_column='data', null=True, verbose_name='Data Pesquisa')),
                ('uso', models.CharField(blank=True, choices=[('1', 'Residencial'), ('2', 'Comercial'), ('3', 'Misto')], max_length=1, null=True, verbose_name='Uso')),
                ('idade', models.IntegerField(blank=True)),
                ('aconstruida', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Área Construída/Útil')),
                ('atotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Área Total')),
                ('bairro', models.CharField(blank=True, default='----', max_length=100, null=True)),
                ('cidade', models.CharField(default='Ribeirão Preto', max_length=200)),
                ('estado', models.CharField(default='SP', max_length=2)),
                ('estadoconser', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.estadoconser', verbose_name='Estado de Conservação')),
                ('nomecondominio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.nomecondominio', verbose_name='Condominio')),
                ('padrao', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.padrao')),
                ('tipo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.tipo')),
                ('user_consultor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Usuário', to='portal.proprietario')),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtacadastro', models.DateField(blank=True, db_column='dtaCadastro', null=True, verbose_name='Data de cadastro')),
                ('uso', models.CharField(blank=True, choices=[('1', 'Residencial'), ('2', 'Comercial'), ('3', 'Misto')], max_length=1, null=True, verbose_name='Estado Civil')),
                ('idade', models.IntegerField(blank=True)),
                ('logradouro', models.CharField(blank=True, db_column='Logradouro', max_length=200, null=True)),
                ('complemento', models.CharField(blank=True, db_column='Complemento', max_length=200, null=True)),
                ('numero', models.CharField(blank=True, db_column='Número', max_length=20, null=True)),
                ('sem_numero', models.BooleanField(blank=True, default=False, null=True, verbose_name='S/N')),
                ('bairro', models.CharField(default='----', max_length=100)),
                ('cidade', models.CharField(default='Ribeirão Preto', max_length=200)),
                ('estado', models.CharField(default='SP', max_length=2)),
                ('numero_dormitorios', models.IntegerField(db_column='Nº dormitórios', default=0)),
                ('numero_banheiros', models.IntegerField(db_column='Nº total banheiros', default='0')),
                ('lavabo', models.BooleanField(blank=True, default=False, null=True, verbose_name='Lavabo')),
                ('aquec_solar', models.BooleanField(blank=True, default=False, null=True, verbose_name='Aquecimento Solar')),
                ('suites', models.IntegerField(db_column='Nº Suítes', default=0)),
                ('churrasqueira', models.BooleanField(blank=True, default=False, null=True, verbose_name='Churrasqueira')),
                ('quarto_empreg', models.BooleanField(blank=True, default=False, null=True, verbose_name='Quarto empregada')),
                ('banheiro_empre', models.BooleanField(blank=True, default=False, null=True, verbose_name='Banheiro empregada')),
                ('vestiario', models.BooleanField(blank=True, default=False, null=True, verbose_name='Vestiário')),
                ('piscina', models.BooleanField(blank=True, default=False, null=True, verbose_name='Piscina')),
                ('pisc_aquec', models.BooleanField(blank=True, default=False, null=True, verbose_name='Piscina aquecida')),
                ('aconstruida', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Área Construída/Útil')),
                ('atotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Área Total')),
                ('status', models.CharField(choices=[('1', 'Oferta'), ('2', 'Vendido')], max_length=1)),
                ('valordevenda', models.DecimalField(db_column='Valor Pretendido', decimal_places=2, default=0, max_digits=10, verbose_name='Valor de venda')),
                ('consultor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Consultor', to='portal.proprietario')),
                ('estadoconser', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.estadoconser', verbose_name='Estado de Conservação')),
                ('nomecondominio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.nomecondominio', verbose_name='Condominio')),
                ('padrao', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portal.padrao')),
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
