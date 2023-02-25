import comparativo.models


class Admin:

    def get_cars_for_approval(self):
        cars = comparativo.models.CarrosPendentes.objects.filter(status=False, is_reprovado=False).all()

        return cars
