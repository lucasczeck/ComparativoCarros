from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('cadastro', views.Cadastro.as_view(), name='cadastro'),
    path('logout', views.Logout.as_view(), name='logout'),
]
