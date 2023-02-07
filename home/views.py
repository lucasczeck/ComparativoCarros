from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

import BO.home.home


class Login(View):

    def get(self, *args, **kwargs):
        context = {}

        return render(self.request, "login.html", context=context)
