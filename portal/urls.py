from django.urls import path, include
from portal import views as v


imovel_urlpatterns = [

    path('', v.ImovelListView.as_view(), name='imovel_list'),  # noqa E501
    path('<int:pk>/', v.ImovelDetailView.as_view(), name='imovel_detail'),  # noqa E501
    path('add/', v.ImovelCreateView.as_view(), name='imovel_add'),  # noqa E501
    path('<int:pk>/edit/', v.ImovelUpdateView.as_view(), name='imovel_edit'),  # noqa E501
    path('pesquisa/', v.pesquisa_imovel, name='pesquisa'),  # noqa E501
    path('<int:pk>/delete/', v.imovel_delete, name='imovel_delete'),  # noqa
]

proprietario_urlpatterns = [

    #path('', v.ProprietarioListView.as_view(), name='proprietario_list'),  # noqa E501
    path('<int:pk>/', v.ProprietarioDetailView.as_view(), name='proprietario_detail'),  # noqa E501
    path('add/', v.ProprietarioCreateView.as_view(), name='proprietario_add'),  # noqa E501
    path('<int:pk>/edit/', v.ProprietarioUpdateView.as_view(), name='proprietario_edit'),  # noqa E501
    #path('<int:pk>/delete/', v.imovel_delete, name='medicamento_delete'),  # noqa E501
]

urlpatterns = [
    path('imovel/', include(imovel_urlpatterns)),
    path('proprietario/', include(proprietario_urlpatterns)),
    path('home/', v.home, name='home'),
    path('retorno/', v.TesteRetorno, name='retorno'),
    path('avaliacao', v.filtraCondominio, name='avaliacao'),
    path('referenciais/', v.referenciais, name='referenciais'),
    path('vida_util/', v.vida_util, name='util'),
    path('tabela/ross/', v.ross, name='ross'),
    path('estadoConservacao/', v.estadoConserv, name='estadoConservacao'),
    path('estadoConserv/add', v.estadoConserv_add, name='estadoConserv_add'),
    path('condominio/', v.condominio, name='condominio'),
    path('cond/add', v.cond_add, name='cond_add'),
    path('cond/edit/<int:cond_pk>/', v.cond_edit, name='cond_edit'),
    path('cond/delete/<int:cond_pk>/', v.cond_delete, name='cond_delete'),
    path('tipo/', v.tipo, name='tipo'),
    path('tipo/add', v.tipo_add, name='tipo_add'),
    path('padrao/', v.padrao, name='padrao'),
    path('padrao/add', v.padrao_add, name='padrao_add'),

    path('<int:pk>/edit/', v.ProprietarioUpdateView.as_view(), name='proprietario_edit'),
    #path('<int:pk>/edit/', views.ProprietarioUpdateView.as_view(), name='edit'),
    path('proprietario/delete/<int:proprietario_pk>/', v.proprietario_delete, name='proprietario_delete'),
    path('', v.index, name='index'),  # noqa E501
]
