from django.contrib.auth.views import LogoutView
from django.urls import path
from portal.accounts import views as v


urlpatterns = [
    # path('login/', v.CustomLoginView.as_view(), name='login'),  # noqa E501
    path('login/', v.custom_login, name='login'),  # noqa E501
    path('logout/', LogoutView.as_view(), name='logout'),  # noqa E501
    path('proprietario/avaliador/add/', v.proprietario_avaliador_add, name='proprietario_avaliador_add'),   # noqa E501

]
