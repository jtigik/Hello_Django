
from django.urls import path
#Import relativo para o App blog
from . import views

# DEFININDO OS PATHS (CAMINHOS)
urlpatterns = [
    #url está sendo completada pelo 'include' (url aninhada)
    #Trecho previamente preenchido com 'blog/'
    path('', views.blog)
]
