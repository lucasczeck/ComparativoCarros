from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

import BO.comparativo.comparativo


class Comparacao(View):

    def get(self, *args, **kwargs):
        modelos = [self.request.GET.get('model1'), self.request.GET.get('model2')]
        marcas = [self.request.GET.get('brand1'), self.request.GET.get('brand2')]
        anos = [self.request.GET.get('year1'), self.request.GET.get('year2')]
        versoes = [self.request.GET.get('versao1'), self.request.GET.get('versao2')]

        carro1, carro2 = BO.comparativo.comparativo.Comparar.\
            get_dict_filter(modelos=modelos, marcas=marcas, anos=anos, versoes=versoes)

        car_infos1 = BO.comparativo.comparativo.Comparar().get_infos_car(car=carro1)
        car_infos2 = BO.comparativo.comparativo.Comparar().get_infos_car(car=carro2)

        context = {
            'car1': car_infos1,
            'car2': car_infos2
        }

        return render(self.request, 'comparacao.html', context=context)


class Comparar(View):

    def get(self, *args, **kwargs):
        brands = BO.comparativo.comparativo.Home().get_brands()
        car_models = BO.comparativo.comparativo.Home().get_car_models()
        years = BO.comparativo.comparativo.Home().get_model_years()

        context = {
            'brands': list(brands),
            'models': list(car_models),
            'years': list(years),
        }

        return render(request=self.request, template_name='home.html', context=context)
