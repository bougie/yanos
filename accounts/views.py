from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import django.contrib.auth

from lib.renderer import request_render
from lib.response import JsonResponse
from .forms import LoginForm, PasswordForm, RegisterForm
from .core.register import coreRegister
from .core.login import coreLogin
from .core.logout import coreLogout
from .core.password import corePassword


@login_required
def index(request):
    tpl_vars = {
        'page_title': '\_o<~ KOIN KOIN ACCOUNT'
    }
    return request_render(request, 'accounts/index.j2', tpl_vars)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = coreLogin(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                django.contrib.auth.login(request, user)
            except:
                json = {
                    'success': False,
                    'msg': 'Utilisateur ou mot de passe incorrect'
                }
            else:
                json = {
                    'success': True,
                    'msg': 'Vous etes maintenant connecté',
                    'redirect': request.GET.get('next', reverse('index'))
                }
        else:
            json = {
                'success': False,
                'msg': 'Veuillez à remplir correctement le formulaire'
            }

        if request.is_ajax():
            return JsonResponse(content=json)
        else:
            if json['success']:
                messages.add_message(request, messages.SUCCESS, json['msg'])
            else:
                messages.add_message(request, messages.ERROR, json['msg'])

            return redirect(json['redirect'])
    else:
        form = LoginForm()

    tpl_vars = {
        'page_title': '\_o<~ KOIN KOIN LOGIN',
        'form': form,
        'ajax': request.is_ajax(),
        'redirect_url': request.GET.get('next', reverse('index'))
    }
    if request.is_ajax():
        return request_render(request, 'accounts/login_ajax.j2', tpl_vars)
    else:
        return request_render(request, 'accounts/login.j2', tpl_vars)


def logout(request):
    coreLogout(request)
    messages.add_message(
        request,
        messages.SUCCESS,
        'Vous etes maintenant deconnecté')

    return redirect('index')


def password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            try:
                username = ''
                corePassword(
                    username=username,
                    old_password=form.cleaned_data['old_password'],
                    password=form.cleaned_data['password'],
                    password2=form.cleaned_data['password2']
                )
            except:
                pass
                # Error will be displayed by the form
            else:
                return redirect('accounts_index')
    else:
        form = PasswordForm()

    tpl_vars = {
        'page_title': '\_o<~ KOIN KOIN PASSWORD',
        'form': form
    }
    return request_render(request, 'accounts/password.j2', tpl_vars)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                coreRegister(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    password2=form.cleaned_data['password2']
                )
            except:
                json = {
                    'success': False,
                    'msg': 'Utilisateur existant ou mots de passes incoherents'
                }
            else:
                json = {
                    'success': True,
                    'msg': 'Compte crée avec succes',
                    'redirect': reverse('accounts_login')
                }
        else:
            json = {
                'success': False,
                'msg': 'Veuillez remplir correctement le formulaire'
            }

        if request.is_ajax():
            return JsonResponse(content=json, status=200)
        else:
            if json['success']:
                messages.add_message(request, messages.SUCCESS, json['msg'])
            else:
                messages.add_message(request, messages.ERROR, json['msg'])

            return redirect('index')
    else:
        form = RegisterForm()

    tpl_vars = {
        'page_title': '\_o<~ KOIN KOIN REGISTER',
        'form': form,
        'ajax': request.is_ajax()
    }

    if request.is_ajax():
        return request_render(
            request,
            'accounts/register_ajax.j2',
            tpl_vars)
    else:
        return request_render(request, 'accounts/register.j2', tpl_vars)
