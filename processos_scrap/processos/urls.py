from django.urls import path
from . import views

urlpatterns = [
    path('processos/', views.lista_processos, name='lista_processos'),
    path('processos/<int:processo_id>/', views.detalhe_processo, name='detalhe_processo'),
]
