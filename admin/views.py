from django.shortcuts import render, redirect, HttpResponse
from django.views import View

import BO.admin.admin


class Home(View):

    def get(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('admin.login')
        elif not self.request.user.is_staff:
            return redirect('login')

        admin = BO.admin.admin.Admin()

        cars_for_approval = admin.get_cars_for_approval()
        last_approvals = admin.get_last_approvals()

        context = {'cars': cars_for_approval,
                   'last_approvals': last_approvals}

        return render(self.request, 'homeAdmin.html', context)


class Aprovacao(View):

    def post(self, *args, **kwargs):
        brand = self.request.POST.get('carBrand')
        model = self.request.POST.get('carModel')
        year = self.request.POST.get('carYear')
        engine = self.request.POST.get('engine')
        gearbox = self.request.POST.get('gearbox')
        lenght = self.request.POST.get('length')
        width = self.request.POST.get('width')
        height = self.request.POST.get('height')
        wheelbase = self.request.POST.get('wheelbase')
        weigth = self.request.POST.get('wigth')
        price = self.request.POST.get('price')
        background_color = self.request.POST.get('background-color')
        button_color = self.request.POST.get('button-color')
        specs_color = self.request.POST.get('specs-color')
        image = self.request.FILES.get('image')
        path = self.request.FILES.get('image').name
        user = self.request.user
        id = self.request.POST.get("carId")

        return redirect('admin.home')
