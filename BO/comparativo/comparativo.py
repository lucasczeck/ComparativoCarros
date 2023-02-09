import comparativo.models


class Comparar:

    def get_infos_car(self, car):
        car_filter = car
        if car_filter['versao'] is None:
            car_filter.pop('versao')

        carro = comparativo.models.Carro.objects.filter(**car_filter).first()

        carro.preco = self.format_brl(carro.preco)

        info = {
            'marca': carro.marca_id,
            'modelo': carro.modelo,
            'versao': carro.versao,
            'motor': carro.motor,
            'cambio': carro.cambio,
            'comprimento': carro.comprimento,
            'largura': carro.largura,
            'altura': carro.altura,
            'entre-eixos': carro.entre_eixos,
            'peso': carro.peso,
            'preco': carro.preco,
            'img_path': str(carro.path),
            'bg': carro.cor_fundo,
            'bg_specs': carro.cor_specs,
            'bg_btn': carro.cor_botao,
        }
        return info

    @staticmethod
    def get_dict_filter(modelos=None, marcas=None, anos=None, versoes=None):
        carro1 = {}
        carro2 = {}

        if modelos:
            carro1['modelo'] = modelos[0]
            carro2['modelo'] = modelos[1]

        if marcas:
            carro1['marca'] = marcas[0]
            carro2['marca'] = marcas[1]

        if anos:
            carro1['ano'] = anos[0]
            carro2['ano'] = anos[1]

        if versoes:
            carro1['versao'] = versoes[0]
            carro2['versao'] = versoes[1]

        return carro1, carro2

    @staticmethod
    def format_brl(valor):
        valor = '{:,.2f}'.format(float(valor))
        valor = valor.replace(',', 'v')
        valor = valor.replace('.', ',')
        return valor.replace('v', '.')


class Home:

    @staticmethod
    def get_brands():
        brands = comparativo.models.Marca.objects.filter(status=True).values_list('nome', flat=True)

        return brands

    @staticmethod
    def get_car_models():
        car_models = comparativo.models.Carro.objects.all().values('modelo', 'marca_id', 'nm_descritivo')

        return car_models

    @staticmethod
    def get_model_years():
        years = comparativo.models.Carro.objects.all().values('modelo', 'ano')

        return years

    @staticmethod
    def get_countries():
        countries = comparativo.models.Pais.objects.all().values_list('nome', flat=True)

        return countries


class Cadastros:

    @staticmethod
    def save_brand(pais=None, marca=None):

        new_brand = comparativo.models.Marca()

        new_brand.nome = marca
        new_brand.pais_origem_id = pais
        new_brand.status = False
        new_brand.save()

        return True

    @staticmethod
    def save_car(marca=None, modelo=None, ano=None):

        new_car = comparativo.models.CarrosPendentes()

        new_car.marca_id = marca
        new_car.modelo = modelo
        new_car.ano = ano
        new_car.save()

        return True
