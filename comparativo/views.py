from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

import BO.comparativo.comparativo


class Comparacao(View):

    def get(self, *args, **kwargs):
        if not self.request.user.pk:
            return redirect('login')
        modelos = [self.request.GET.get('model1'), self.request.GET.get('model2')]
        marcas = [self.request.GET.get('brand1'), self.request.GET.get('brand2')]
        anos = [self.request.GET.get('year1'), self.request.GET.get('year2')]
        versoes = [self.request.GET.get('versao1'), self.request.GET.get('versao2')]

        carro1, carro2 = BO.comparativo.comparativo.Comparar.\
            get_dict_filter(modelos=modelos, marcas=marcas, anos=anos, versoes=versoes)

        car_infos1 = BO.comparativo.comparativo.Comparar().get_infos_car(car=carro1)
        car_infos2 = BO.comparativo.comparativo.Comparar().get_infos_car(car=carro2)

        context = {'car1': car_infos1,
                   'car2': car_infos2}

        return render(self.request, 'comparacao.html', context=context)


class Comparar(View):

    def get(self, *args, **kwargs):
        if not self.request.user.pk:
            return redirect('login')

        car_models = BO.comparativo.comparativo.Home().get_car_models()
        brands = BO.comparativo.comparativo.Home().get_brands(cars=car_models.values_list('marca_id', flat=True))
        years = BO.comparativo.comparativo.Home().get_model_years()

        context = {'brands': list(brands),
                   'models': list(car_models),
                   'years': list(years)}

        return render(request=self.request, template_name='home.html', context=context)


class CadastrarCarro(View):

    def get(self, *args, **kwargs):
        if not self.request.user.pk:
            return redirect('login')
        marcas = BO.comparativo.comparativo.Home.get_brands()
        paises = BO.comparativo.comparativo.Home.get_countries()

        context = {'marcas': marcas,
                   'paises': paises}

        return render(self.request, 'cadastrar_carro.html', context)

    def post(self, *args, **kwargs):
        marca = self.request.POST.get('marca')
        modelo = self.request.POST.get('modelo')
        ano = self.request.POST.get('ano')

        status = BO.comparativo.comparativo.Cadastros\
            .save_car(marca=marca, modelo=modelo, ano=ano, user=self.request.user.pk)

        if status:
            return redirect('/comparativo')
        else:
            return HttpResponse('Erro ao cadastrar carro')


class CadastrarMarca(View):

    def post(self, *args, **kwargs):
        marca = self.request.POST.get('marca')
        pais = self.request.POST.get('pais')

        status = BO.comparativo.comparativo.Cadastros.save_brand(marca=marca, pais=pais)

        if status:
            return redirect("/comparativo/cadastrar")
        else:
            return HttpResponse("Erro ao cadastrar marca")
