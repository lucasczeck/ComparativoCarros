from django.shortcuts import render, redirect
from django.views import View

import BO.admin.admin


class Home(View):

    def get(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('admin.login')
        elif not self.request.user.is_staff:
            return redirect('login')

        cars_for_approval = BO.admin.admin.Admin().get_cars_for_approval()

        context = {'cars': cars_for_approval}

        return render(self.request, 'homeAdmin.html', context)
