from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Corretor(models.Model):
    nome = models.CharField(max_length=200)
    celular = models.CharField(max_length=200)
    creci = models.CharField(max_length=200)
    dtanasc = models.DateField(blank=True, null=True)
    cidade = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Estadoconser(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.nome


class Nomecondominio(models.Model):
    nome = models.CharField(max_length=300)
    endereco = models.CharField(max_length=300, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("cond_edit", kwargs={"cond_pk": self.id})

    class Meta:
       ordering = ['nome']


class Padrao(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Tabelarossheideck(models.Model):
    idade_em_vida = models.IntegerField(db_column='idade_em_vida', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    a = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    b = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    c = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    d = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    e = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    f = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    g = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    h = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.idade_em_vida

    def __int__(self):
        return (self.id)

class Tipo(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
       ordering = ['nome']

class Vidautil(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    idadevidautil = models.IntegerField(db_column='idadeVidaUtil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
       ordering = ['nome']

    def __str__(self):
        return self.nome

BOOLEAN_CHOICES = (
        (None, 'Selecionar '),
        (True, 'Sim'),
        (False, 'Não'),
    )

class Proprietario(models.Model):
    nome = models.CharField('Nome', max_length=200)
    sobrenome = models.CharField('Sobrenome',  max_length=200, blank=True, null=True)
    celular = models.CharField('Celular',max_length=200)
    whatsApp = models.BooleanField('WhatsApp ?', default=False, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=20)
    email = models.EmailField('Email')
    cidade = models.CharField('Cidade', max_length=200)
    corretor = models.BooleanField('Corretor', default=False, blank=True, null=True)
    imobiliaria = models.BooleanField('Imobiliária', default=False, blank=True, null=True)
    dono = models.BooleanField('Proprietário', default=False, blank=True, null=True)

    class Meta:
       ordering = ['nome']

    def __str__(self):
        return "{} - {} - {} - {} ".format(self.nome, self.cpf, self.email, self.dono)

    def get_absolute_url_add(self):
        return reverse("proprietario_add", kwargs={"pk": self.id})

    def get_absolute_url(self):
        return reverse("proprietario_edit", kwargs={"pk": self.id})

status_choices = (
        ('1', 'Oferta'),
        ('2', 'Vendido')
    )

class Imovel(models.Model):
    valordevenda = models.DecimalField(db_column='Valor Pretendido', max_digits=10, decimal_places=2, blank=False, null=False, default=0, verbose_name='Valor de venda')  # Field name made lowercase.
    nomecondominio = models.ForeignKey(Nomecondominio, on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Condominio')
    idade = models.IntegerField(blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=200, blank=True)
    aconstruida = models.DecimalField(blank=False, null=False, default=0, max_digits=10, decimal_places=2,  verbose_name='Área Construída/Útil')
    atotal = models.DecimalField(blank=False, null=False, default=0, max_digits=10, decimal_places=2, verbose_name='Área Total')
    dtacadastro = models.DateField(db_column='dtaCadastro', blank=True, null=True, verbose_name='Data de cadastro')  # Field name made lowercase.
    status = models.CharField(max_length=1, choices=status_choices)
    padrao = models.ForeignKey(Padrao, on_delete=models.CASCADE, blank=True)
    estadoconser = models.ForeignKey(Estadoconser, on_delete=models.CASCADE, blank=True, verbose_name='Estado de Conservação')  # Field name made lowercase.
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, blank=True)
    vidautil = models.ForeignKey(Vidautil, on_delete=models.CASCADE, blank=True,  verbose_name='Vida Útil')  # Field name made lowercase.
    consultor = models.ForeignKey(Proprietario, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Consultor')


    class Meta:
        ordering = ['-dtacadastro']

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {}  ".format(self.padrao.nome, self.tipo.nome, self.nomecondominio.nome, self.estadoconser.nome, self.vidautil.nome, self.consultor.nome, self.consultor.corretor, self.consultor.whatsApp, self.corretor.celular)

    def __float__(self):
        return "{} - {} - {}".format(self.valordevenda, self.aconstruida, self.atotal)

    def metroquadrado(self):
        if self.aconstruida == 0:
            return self.valordevenda, self.aconstruida
        else:
            metro_quadrado = ((self.valordevenda) / (self.aconstruida))
            return round(float(metro_quadrado),2)

    def get_absolute_url(self):
        return reverse("editar", kwargs={"imovel_pk": self.id})


class Avaliacao(models.Model):
    data_avaliacao =models.DateField('Data Avaliação')
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, blank=True)
    valor_metro_quadrado = models.DecimalField('Valor m²', max_digits=20, decimal_places=2)
    valor_metro_quadrado_final=models.DecimalField('Valor Final m² ', max_digits=20, decimal_places=2)
    desconto_oferta = models.DecimalField('Valor m²', max_digits=20, decimal_places=2)
    valor_da_coluna = models.CharField('Coluna', max_length=1)
    idade_em_perc = models.DecimalField('Idade em % vida', max_digits=6,decimal_places=2)
    valor_avaliacao = models.DecimalField('Valor Avaliação', max_digits=10,decimal_places=2)
    ross_heideck = models.ForeignKey(Tabelarossheideck, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_avaliacao']

    def __str__(self):
        return "{} - {} - {} - {} ".format(self.imovel.tipo.nome, self.imovel.nomecondominio.nome, self.imovel.estadoconser.nome,  self.imovel.vidautil.nome,  self.imovel.proprietario.nome)

    def __float__(self):
        return "{} - {} - {}- {} - {} - {}- {} - {}- {}".format(self.imovel.aconstruida, self.valor_metro_quadrado, self.valor_metro_quadrado_final, self.imovel.valordevenda, self.imovel.aconstruida, self.imovel.atotal, self.desconto_oferta, self.idade_em_perc, self.valor_avaliacao)

    def get_absolute_url(self):
        return reverse("avaliacao_edit", kwargs={"avaliacao_pk": self.id})