from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login


class Login(View):

    def get(self, *args, **kwargs):
        return render(self.request, 'login.html')

    def post(self, *args, **kwargs):

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            # Redirecionar o usuário para a página desejada
            return redirect('home')
        else:
            # Mostrar uma mensagem de erro
            return HttpResponse("Nome de usuário ou senha inválidos.")
