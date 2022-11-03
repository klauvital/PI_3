from django.urls import path, include
from portal import views as v


imovel_urlpatterns = [

    path('', v.ImovelListView.as_view(), name='imovel_list'),  # noqa E501
    path('<int:pk>/', v.ImovelDetailView.as_view(), name='imovel_detail'),  # noqa E501
    path('add/', v.ImovelCreateView.as_view(), name='imovel_add'),  # noqa E501
    path('<int:pk>/edit/', v.ImovelUpdateView.as_view(), name='imovel_edit'),  # noqa E501
    #path('<int:pk>/delete/', v.imovel_delete, name='medicamento_delete'),  # noqa E501
]


urlpatterns = [
    path('imovel/', include(imovel_urlpatterns)),
    path('home/', v.home, name='home'),
    path('retorno/', v.TesteRetorno, name='retorno'),
    path('avaliacao', v.filtraCondominio, name='avaliacao'),
    path('referenciais/', v.referenciais, name='referenciais'),
    #path('imovel_list/', v.ImovelListView.as_view(), name='imovel'),
    path('vida_util/', v.vida_util, name='util'),
    path('tabela/ross/', v.ross, name='ross'),
    #path('imovel/add/', views.imovel_add, name='imovel_add'),
    #path('imovel/edit/<int:imovel_pk>/', views.imovel_edit, name='editar'),
    #path('imovel/delete/<int:imovel_pk>/', views.imovel_delete, name='imovel_delete'),
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
    path('proprietario/add/', v.ProprietarioCreateView.as_view(), name='proprietario_form'),
    path('<int:pk>/edit/', v.ProprietarioUpdateView.as_view(), name='proprietario_edit'),
    #path('<int:pk>/edit/', views.ProprietarioUpdateView.as_view(), name='edit'),
    path('proprietario/delete/<int:proprietario_pk>/', v.proprietario_delete, name='proprietario_delete'),
    path('', v.index, name='index'),  # noqa E501
]
