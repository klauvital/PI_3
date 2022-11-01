from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages import constants
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse_lazy
from portal.models import Proprietario
from .services import proprietario_avaliador_create
from portal.services import has_group
from .forms import ProprietarioAvaliadorForm


def proprietario_avaliador_add(request):
    template_name = 'accounts/proprietario_avaliador_add.html'
    form = ProprietarioAvaliadorForm(request.POST or None)
    success_url = reverse_lazy('login')

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            proprietario_avaliador_create(form, user)
            msg = 'Cadastrado com sucesso! Faça seu Login'
            messages.add_message(request, constants.SUCCESS, msg)
            return redirect(success_url)

    context = {'form': form}

    return render(request, template_name, context)


def custom_login(request):
    template_name = 'accounts/login.html'
    form = AuthenticationForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autentica
        user_auth = authenticate(username=username, password=password)

        if user_auth:
            # Faz login
            auth_login(request, user_auth)
            # return redirect(resolve_url(settings.LOGIN_REDIRECT_URL))
            user = user_auth
            return redirect(resolve_url('home'))


        # Caso não esteja autenticado.
        messages.add_message(request, constants.ERROR, 'Usuário ou senha não conferem !')  # noqa E501
        return redirect(resolve_url(settings.LOGIN_REDIRECT_URL))

    return render(request, template_name, context)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_default_redirect_url(self):
        user = self.request.user



