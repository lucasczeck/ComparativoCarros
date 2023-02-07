from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
]
