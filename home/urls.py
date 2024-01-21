from django.urls import path
#Import relativo para o App home
from . import views

# DEFININDO OS PATHS (CAMINHOS)
urlpatterns = [
    path('', views.home)
]