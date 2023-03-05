from django.urls import path
from admin import views

urlpatterns = [
    path('', views.Home.as_view(), name='admin.home'),
    path('login', views.Home.as_view(), name='admin.login'),
    path('aprovar', views.Aprovacao.as_view(), name='admin.aprovar'),
]
