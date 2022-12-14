import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from portal.forms import ImovelForm, PadraoForm, NomecondominioForm, EstadoconserForm, TipoForm, ImovelFormFilter, ProprietarioForm, PesquisaForm
from portal.models import Imovel, Padrao, Nomecondominio, Estadoconser, Tipo, Tabelarossheideck, Vidautil, Proprietario, Pesquisa
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.http import request



from .services import (
    add_to_group_proprietario,
    user_create
)

def index(request):
    return render(request, 'portal/index.html')

def home(request):

    return render(request, 'portal/home.html')


def pesquisa_ref_imovel(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    pesquisa = Pesquisa.objects.all()

    Pesquisa.objects.create(
        data=datetime.date.today(),
        uso=imovel.uso,
        idade=int(imovel.idade),
        aconstruida=float(imovel.aconstruida),
        atotal=imovel.atotal,
        bairro=imovel.bairro,
        cidade=imovel.cidade,
        estado=imovel.estado,
        estadoconser_id=imovel.estadoconser.id,
        nomecondominio_id=imovel.nomecondominio.id,
        padrao_id=imovel.padrao.id,
        tipo_id=imovel.tipo.id,
        user_consultor_id=imovel.consultor.id,
        status=imovel.status,
        valor_venda= imovel.valordevenda,
        valor_avaliacao=0.00,
    )


    return redirect('pesquisa_list')



class PesquisaCreateView(LRM, CreateView):
    model = Pesquisa
    form_class = PesquisaForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user.username})
        return kwargs


class PesquisaDetailView(LRM, DetailView):
    model = Pesquisa


class PesquisaListView(LRM, ListView):
    model = Pesquisa

    def get_queryset(self):
        user = self.request.user.username
        queryset = Pesquisa.objects.filter(user_consultor__email=user)  # noqa E501
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labels'] = (
            'Data',
            'Uso',
            'Status',
            'Idade',
            'Conserva????o',
            'Padr??o',
            'Tipo',
            'AC',
            'AT',
            'Condominio',
            'Bairro',
            'Cidade',
            'Estado',
            'Consultor',

        )

        return context


def referenciais(request):
    if request.method == "POST":
        uso = request.POST.get('uso')
        tipo = request.POST.get('tipo')
        conservacao = request.POST.get('estadoConserv')
        padrao = request.POST.get('padrao')
        idade = int(request.POST.get('idade'))
        aT = request.POST.get('atotal')
        aC = int(request.POST.get('aconstruida'))
        condominio = request.POST.get('condominio')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        # Quando precisar dos valores de Estadoconser

        busca = Q(
            Q(nomecondominio__nome=condominio)
            | Q(bairro=bairro)
            & Q(padrao__nome=padrao)
            & Q(tipo__nome=tipo)
        )
        dados = (uso, tipo, conservacao, padrao, idade, aT, aC,
                 condominio, bairro, cidade, estado)


        Listimovel = Imovel.objects.filter(busca)

        if Listimovel.count() != 0:
            metro_quadr = 0
            cont = 0
            media_m2 = 0
            gordura = 0
            valorAvaliacao = 0
            vidautil = 0
            valor_tabela = 0
            desconto_oferta = 0
            metro_quadrado_inicial = 0
            metro_quadrado_final = 0
            idade_em_perc = 0
            frase = ''
            inversao = False
            lista = []
            for i in Listimovel:
                dicionario = {}
                metro_quadr = 0
                metro_quadr = i.metroquadrado()
                metro_quadrado_final = 0
                if i.status == '1':
                    desconto_oferta = round((metro_quadr * 0.05),2)
                    metro_quadr = metro_quadr - desconto_oferta

                if idade == i.idade:
                    cont += 1
                    media_m2 += metro_quadr / cont
                else:
                    ec = i.estadoconser.codigo
                    vidautil = (idade - i.idade)
                    vidautil = round(vidautil * 100 / i.vidautil.idadevidautil)
                    idade_em_perc = vidautil

                    if vidautil < 0:
                       vidautil= vidautil * -1
                       inversao = True

                    if vidautil == 0:
                       vidautil= vidautil+2

                    if vidautil % 2 !=0:
                       vidautil=vidautil+1

                    lst = [field.name for field in Tabelarossheideck._meta.get_fields()]

                    # ec vem da lista de colunas da Tabelarossheideck

                    # Dicion??rio vazio
                    lorem = {}

                    # Transforma o objeto Tabelarossheideck numa lista de dicion??rios.
                    objeto_rossheideck = Tabelarossheideck.objects.filter(idade_em_vida=vidautil).values()
                    primeiro_registro = objeto_rossheideck[0]

                    # valor da coluna correspondente
                    # primeiro_registro[ec] ?? como se fosse um dicion??rio
                    # com chave e valor, mas no lugar da chave
                    # usamos uma vari??vel, porque a letra vem de ec.
                    valor_da_coluna = primeiro_registro[ec]
                    valor_tabela = round(metro_quadr * float(valor_da_coluna)/100,2)

                    metro_quadrado_inicial = i.metroquadrado()

                    if inversao == True:
                        metro_quadrado_final = metro_quadrado_inicial - desconto_oferta + valor_tabela

                    else:
                        metro_quadrado_final = metro_quadrado_inicial - valor_tabela - desconto_oferta

                    cont += 1
                    media_m2 += metro_quadrado_final
                    dicionario['id'] = i.id
                    dicionario['uso'] = i.uso
                    dicionario['tipo'] = i.tipo.nome
                    dicionario['padrao'] = i.padrao.nome
                    dicionario['condominio'] = i.nomecondominio.nome
                    dicionario['bairro'] = i.bairro
                    dicionario['ac'] = i.aconstruida
                    dicionario['ec'] = i.estadoconser.nome
                    dicionario['idade'] = i.idade
                    dicionario['estatus'] = i.get_status_display
                    dicionario['valor'] = i.valordevenda
                    dicionario['metro_quadrado'] = i.metroquadrado()
                    dicionario['metro_quadrado_final'] = round(metro_quadrado_final,2)
                    dicionario['desconto_oferta'] = desconto_oferta
                    dicionario['valor_da_coluna'] = valor_da_coluna
                    dicionario['idade_em_perc'] = idade_em_perc
                    dicionario['valor_tabela'] = valor_tabela
                    lista.append(dicionario)

            media_m2 = media_m2 / cont
            valorAvaliacao = media_m2 * aC
            media_m2 = "R$ {:,.2f}".format(media_m2).replace(",", "X").replace(".", ",").replace("X", ".")
            valorAvaliacao = "R$ {:,.2f}".format(valorAvaliacao).replace(",", "X").replace(".", ",").replace("X", ".")

            context = {
               'lista': lista,
               'referenciais': Listimovel,
               'dados': dados,
               'valor': valorAvaliacao,
               'media_metro2': media_m2,
               'area_construida': aC,
            }
            return render(request, 'portal/referenciais.html', context=context)
        else:
            frase = "N??o existe referenciais para os dados acima"

            context = {
                'dados': dados,
                'frase': frase,
            }
            return render(request, 'portal/referenciais_nulo.html', context=context)





def pesquisa_imovel(request, pk):
    pesquisa = get_object_or_404(Pesquisa, pk=pk)

    if pesquisa:
        uso = pesquisa.uso
        idade = int(pesquisa.idade)
        conservacao = pesquisa.estadoconser
        padrao = pesquisa.padrao
        tipo = pesquisa.tipo
        aC = float(pesquisa.aconstruida)
        atotal = pesquisa.atotal
        condominio = pesquisa.nomecondominio
        bairro = pesquisa.bairro
        cidade = pesquisa.cidade
        estado = pesquisa.estado



        busca = Q(
            Q(nomecondominio__nome=condominio)
            | Q(bairro=bairro)
            & Q(padrao__nome=padrao)
            & Q(tipo__nome=tipo)
        )
        Listimovel = Imovel.objects.filter(busca)


        if Listimovel.count() != 0:
            metro_quadr = float(0)
            cont = 0
            media_m2 = float(0)
            gordura = 0
            valorAvaliacao = 0
            vidautil = 0
            valor_tabela = 0
            valor_da_coluna = 0
            desconto_oferta = float(0)
            metro_quadrado_inicial = float(0)
            metro_quadrado_final = float(0)
            idade_em_perc = 0
            valor_desc_oferta = 0
            frase = ''
            inversao = False
            lista = []

            for i in Listimovel:
                dicionario = {}
                metro_quadr = float(0)
                metro_quadr = i.metroquadrado()
                metro_quadrado_final = float(0)
                valor_desc_oferta = float(0)
                idade_em_perc = 0
                valor_desc_idade = 0

                #se for status oferta , desc 5%
                if i.status == '1':
                    desconto_oferta = round((metro_quadr * 0.05), 2)
                    valor_desc_oferta = ( metro_quadr - desconto_oferta)

                else:
                    desconto_oferta = 0
                    valor_desc_oferta = metro_quadr - desconto_oferta


                if idade == i.idade:
                    cont += 1
                    metro_quadrado_final = valor_desc_oferta
                    valor_da_coluna = 0
                    valor_tabela = 0
                    vidautil = vidautil + 2
                    vidautil = round(vidautil * 100 / i.vidautil.idadevidautil)

                else:
                    ec = i.estadoconser.codigo
                    vidautil = (idade - i.idade)
                    vidautil = round(vidautil * 100 / i.vidautil.idadevidautil)

                    if vidautil % 2 != 0:
                        vidautil = vidautil - 1
                        idade_em_perc = vidautil

                    if vidautil == 0:
                        vidautil = vidautil + 2
                        idade_em_perc = vidautil

                    if vidautil < 0:
                        idade_em_perc = vidautil
                        vidautil = vidautil * -1
                        inversao = True


                    lst = [field.name for field in Tabelarossheideck._meta.get_fields()]

                    # ec vem da lista de colunas da Tabelarossheideck

                    # Dicion??rio vazio
                    lorem = {}

                    # Transforma o objeto Tabelarossheideck numa lista de dicion??rios.
                    objeto_rossheideck = Tabelarossheideck.objects.filter(idade_em_vida=vidautil).values()
                    primeiro_registro = objeto_rossheideck[0]

                    # valor da coluna correspondente
                    # primeiro_registro[ec] ?? como se fosse um dicion??rio
                    # com chave e valor, mas no lugar da chave
                    # usamos uma vari??vel, porque a letra vem de ec.
                    valor_da_coluna = primeiro_registro[ec]

                    valor_tabela = round(valor_desc_oferta/(100 - float(valor_da_coluna)), 2) * 100
                    valor_desc_idade = (round(valor_tabela - valor_desc_oferta),2)

                    metro_quadrado_inicial = (i.metroquadrado())

                    if inversao == True:
                        metro_quadrado_final = (valor_tabela)

                    else:
                        metro_quadrado_final = (valor_desc_oferta)

                    cont += 1
                media_m2 += metro_quadrado_final
                dicionario['id'] = i.id
                dicionario['uso'] = i.get_uso_display
                dicionario['tipo'] = i.tipo
                dicionario['padrao'] = i.padrao
                dicionario['condominio'] = i.nomecondominio
                dicionario['bairro'] = i.bairro
                dicionario['ac'] = i.aconstruida
                dicionario['ec'] = i.estadoconser
                dicionario['idade'] = i.idade
                dicionario['estatus'] = i.get_status_display
                dicionario['valor_venda'] = i.valordevenda
                dicionario['metro_quadrado'] = i.metroquadrado()
                dicionario['metro_quadrado_final'] = round(metro_quadrado_final, 2)
                dicionario['desconto_oferta'] = desconto_oferta
                dicionario['valor_da_coluna'] = valor_da_coluna
                dicionario['idade_em_perc'] = idade_em_perc
                dicionario['valor_tabela'] = valor_desc_idade
                lista.append(dicionario)

            media_m2 = media_m2 / cont
            valorAvaliacao = media_m2 * float(aC)
            pesquisa.valor_avaliacao = valorAvaliacao
            pesquisa.save()
            media_m2 = "R$ {:,.2f}".format(media_m2).replace(",", "X").replace(".", ",").replace("X", ".")
            valorAvaliacao = "R$ {:,.2f}".format(valorAvaliacao).replace(",", "X").replace(".", ",").replace(
                "X", ".")

            context = {
                'lista': lista,
                'referenciais': Listimovel,
                'dados': pesquisa,
                'valor': valorAvaliacao,
                'media_metro2': media_m2,
                'area_construida': aC,
            }
            return render(request, 'portal/retorno_pesquisa.html', context=context)

        else:
            frase = "N??o existe referenciais para os dados acima"

            context = {
                'dados': pesquisa,
                'frase': frase,

            }
            return render(request, 'portal/retorno_pesquisa.html', context=context)


def duplicar_create(pesquisa, pk):
    pesquisa = get_object_or_404(Pesquisa, pk=pk)
    conservacao =pesquisa.estadoconser.id
    condominio = pesquisa.nomecondominio.id
    padrao = pesquisa.padrao.id
    tipo = pesquisa.padrao.id
    consultor = pesquisa.user_consultor.id

    if pesquisa:
        Pesquisa.objects.create(
        data = datetime.date.today(),
        uso=pesquisa.uso,
        idade=pesquisa.idade,
        aconstruida=pesquisa.aconstruida,
        atotal=pesquisa.atotal,
        bairro=pesquisa.bairro,
        cidade=pesquisa.cidade,
        estado=pesquisa.estado,
        estadoconser_id=conservacao,
        nomecondominio_id=condominio,
        padrao_id=padrao,
        tipo_id=tipo,
        user_consultor_id=consultor,
        status=pesquisa.status,
        valor_venda=0.00,
        valor_avaliacao=0.00,
    )
    pesquisa.save()
    return redirect('pesquisa_list')


class PesquisaUpdateView(LRM, UpdateView):
    model = Pesquisa
    form_class = PesquisaForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



def imovel_edit(request, imovel_pk):
    imovel = get_object_or_404(Imovel, pk=imovel_pk)
    form = ImovelForm(instance=imovel)

    if (request.method == 'POST'):
        form = ImovelForm(request.POST, instance=imovel)

        if (form.is_valid()):
            imovel = form.save(commit=False)
            imovel.save()
            return redirect('imoveis')
        else:
            return render(request, '', {'form': form, 'post': imovel})

    elif (request.method == 'GET'):
        return render(request, 'portal/', {'form': form, 'post': imovel})


class ImovelListView(LRM, ListView):
    model = Imovel

    def get_queryset(self):
        user = self.request.user.username
        queryset = Imovel.objects.all()  # noqa E501
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labels'] = (
            'Data',
            'Tipo',
            'Condom??nio',
            'Bairro',
            'Cidade',
            'AC',
            'Est??tus',
            'Padr??o',
            'EC',
            'Idade',
            'Valor',
        )
        return context



class ImovelMeusListView(LRM, ListView):
    model = Imovel


    def get_queryset(self):
        user = self.request.user.username
        queryset = Imovel.objects.filter(consultor__email=user)  # noqa E501
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labels'] = (
            'Data',
            'Tipo',
            'Condom??nio',
            'Bairro',
            'Cidade',
            'AC',
            'Est??tus',
            'Padr??o',
            'EC',
            'Idade',
            'Valor',
        )
        return context



class ImovelDetailView(LRM, DetailView):
    model = Imovel


class ImovelCreateView(LRM, CreateView):
    model = Imovel
    form_class = ImovelForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ImovelUpdateView(LRM, UpdateView):
    model = Imovel
    form_class = ImovelForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


def ross(request):
    ross = Tabelarossheideck.objects.all()
    context = {
        'ross': ross
    }
    return render(request, 'portal/tabela_ross.html', context=context)


def vida_util(request):
    util = Vidautil.objects.all()
    context = {
        'lista': util
    }
    return render(request, 'portal/vida_util.html', context)


def imovel_add(request):
    form = ImovelForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'portal/imovel_form.html', context)


def imovel_delete(request, imovel_pk):
    imovel = Imovel.objects.get(pk=imovel_pk)
    imovel.delete()
    return redirect('imoveis')


def padrao(request):
    padrao = Padrao.objects.all()
    context = {
        'padrao': padrao
    }
    return render(request, 'portal/padrao.html', context)



def padrao_add(request):
    form = PadraoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('padrao')

    context = {
        'form': form,
    }
    return render(request, 'portal/padrao_add.html', context)


def condominio (request):
    condominio = Nomecondominio.objects.all()
    context = {
        'condominio': condominio
    }
    return render(request, 'portal/condominio.html', context)


def cond_add(request):
    form = NomecondominioForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('condominio')

    context = {
        'form': form,
    }
    return render(request, 'portal/cond_add.html', context)


def cond_edit(request, cond_pk):
    condominio = Nomecondominio.objects.get(pk=cond_pk)
    form = NomecondominioForm(request.POST or None, instance=condominio)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('condominio')

    context = {
        'form': form,
    }
    return render(request, 'portal/cond_edit.html', context)


def cond_delete(request, cond_pk):
    condominio = Nomecondominio.objects.get(pk=cond_pk)
    condominio.delete()
    return redirect('condominio')


def estadoConserv (request):
    estadoConservacao = Estadoconser.objects.all()
    context = {
        'estadoCons': estadoConservacao
    }
    return render(request, 'portal/estadoConservacao.html', context)


def estadoConserv_add(request):
    form = EstadoconserForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('estadoConservacao')

    context = {
        'form': form,
    }
    return render(request, 'portal/estadoConservacao_add.html', context)


def tipo(request):
    tipos = Tipo.objects.all()
    context = {
        'tipos': tipos
    }
    return render(request, 'portal/tipo.html', context)


def tipo_add(request):
    form = TipoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('tipo')

    context = {
        'form': form,
    }

    return render(request, 'portal/tipo_add.html', context)


class ProprietarioCreateView(LRM, CreateView):
    model = Proprietario
    form_class = ProprietarioForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ProprietarioUpdateView(LRM, UpdateView):
    model = Proprietario
    form_class = ProprietarioForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class ProprietarioListView(LRM, ListView):
    model = Imovel

    def get_queryset(self):
        user = self.request.user.username
        queryset = Imovel.objects.filter(consultor__email=user)  # noqa E501
        return queryset


def proprietario_delete(request, proprietario_pk):
    proprietario = Proprietario.objects.get(pk=proprietario_pk)
    proprietario.delete()

    return redirect('home')