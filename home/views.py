from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout

import BO.autenticacao.login


class Login(View):

    def get(self, *args, **kwargs):
        return render(self.request, 'login.html')

    def post(self, *args, **kwargs):

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = BO.autenticacao.login.Login().fazer_login(request=self.request, username=username,
                                                         password=password)
        if user:
            return redirect('/comparativo')
        else:
            return HttpResponse("Nome de usuário ou senha inválidos.")


class Cadastro(View):

    def get(self, *args, **kwargs):
        return render(self.request, 'cadastro.html')

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')

        user = BO.autenticacao.login.Cadastro().fazer_cadastro(username=username, email=email,
                                                               password=password, request=self.request)

        if user:
            return redirect('/comparativo')
        else:
            return HttpResponse('Erro ao cadastrar conta')


class Logout(View):

    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect("login")
