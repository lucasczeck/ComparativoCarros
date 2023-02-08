from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class Login:

    def fazer_login(self, username, password, request):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            return False


class Cadastro:

    def fazer_cadastro(self, username, email, password, request):
        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.save()

        login(request, user)

        return True
