import comparativo.models


class Admin:

    @staticmethod
    def get_cars_for_approval():
        cars = comparativo.models.CarrosPendentes.objects.filter(status=False, is_reprovado=False).all()

        return cars

    @staticmethod
    def get_last_approvals():
        last_approvals = comparativo.models.CarrosPendentes.objects.filter(status=True, is_reprovado=False).all()

        return last_approvals
